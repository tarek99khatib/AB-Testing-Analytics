import os
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy import text

# -------- paths --------
ROOT = Path(__file__).resolve().parents[1]  # repo root: ab_testing_analytics/
RAW_DIR = ROOT / "data" / "raw"
AB_CSV = RAW_DIR / "ab_data.csv"
COUNTRIES_CSV = RAW_DIR / "countries.csv"

# -------- connection (env or defaults) --------
load_dotenv(ROOT / ".env")
PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_DB   = os.getenv("PG_DB",   "ab_testing2")
PG_USER = os.getenv("PG_USER", "ab_user")
PG_PASS = os.getenv("PG_PASS", "")

DB_URL = f"postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}"
engine = create_engine(DB_URL, future=True)

print("➡️  Reading CSVs (no cleaning)…")
ab_df = pd.read_csv(AB_CSV)
countries_df = pd.read_csv(COUNTRIES_CSV)

print("\n📄 ab_data.csv — first 5 rows:")
print(ab_df.head())
print("\n🧾 ab_data.csv — columns:")
print(list(ab_df.columns))

print("\n📄 countries.csv — first 5 rows:")
print(countries_df.head())
print("\n🧾 countries.csv — columns:")
print(list(countries_df.columns))

print("\n⬆️  Loading to PostgreSQL as raw tables (replace)…")
# will CREATE the tables with columns exactly as in CSV (no renaming, no casting)
ab_df.to_sql(
    "raw_ab_data",
    engine,
    if_exists="replace",   # overwrite if exists
    index=False,
    method="multi",
    chunksize=10000,
)

countries_df.to_sql(
    "raw_countries",
    engine,
    if_exists="replace",
    index=False,
    method="multi",
    chunksize=10000,
)

# quick counts quick counts
with engine.begin() as conn:
    n_ab = conn.execute(text("SELECT COUNT(*) FROM raw_ab_data")).scalar_one()
    n_ct = conn.execute(text("SELECT COUNT(*) FROM raw_countries")).scalar_one()

print(f"\n✅ Done. Rows loaded → raw_ab_data: {n_ab:,} | raw_countries: {n_ct:,}")
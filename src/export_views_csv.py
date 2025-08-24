import os
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# paths
ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# connection
load_dotenv(ROOT / ".env")
PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_DB   = os.getenv("PG_DB",   "ab_testing2")
PG_USER = os.getenv("PG_USER", "ab_user")
PG_PASS = os.getenv("PG_PASS", "")

DB_URL = f"postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}"
engine = create_engine(DB_URL, future=True)

# export views
views = ["daily_stats", "ab_user_country"]

for v in views:
    df = pd.read_sql(f"SELECT * FROM {v}", engine)
    out_path = PROCESSED_DIR / f"{v}.csv"
    df.to_csv(out_path, index=False)
    print(f"✅ Exported {v} → {out_path}")
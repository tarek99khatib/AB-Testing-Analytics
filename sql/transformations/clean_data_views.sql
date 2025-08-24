CREATE OR REPLACE VIEW public.ab_data_clean AS
SELECT
  user_id::bigint                         AS user_id,
  "timestamp"                             AS ts,
  LOWER(TRIM("group"))                    AS group_name,
  LOWER(TRIM(landing_page))               AS landing_page,
  converted::int                          AS converted
FROM raw_ab_data;

CREATE OR REPLACE VIEW public.countries_clean AS
SELECT user_id::bigint AS user_id,
       UPPER(TRIM(country)) AS country
FROM raw_countries;

SELECT table_name, table_type
FROM information_schema.tables
WHERE table_schema = 'public'; -- This will show the newly created views in the public schema
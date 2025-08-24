CREATE OR REPLACE VIEW public.ab_user_country AS
SELECT
  a.user_id, a.ts, a.group_name, a.landing_page, a.converted,
  c.country
FROM ab_data_clean a
LEFT JOIN countries_clean c USING (user_id);


SELECT table_name, table_type
FROM information_schema.tables
WHERE table_schema = 'public'; -- This will show the newly created views in the public schema
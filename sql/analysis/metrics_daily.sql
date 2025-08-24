DROP VIEW IF EXISTS public.daily_stats;
CREATE OR REPLACE VIEW public.daily_stats AS
SELECT auc.ts::date as date,
auc.group_name,
COUNT(*) AS total_users_in_group,
COUNT(CASE WHEN auc.converted = 1 THEN 1 END) AS converted_users_in_group,
ROUND(COUNT(CASE WHEN auc.converted = 1 THEN 1 END) * 100.0 / COUNT(*),2) AS conversion_rate

FROM public.ab_user_country as auc
GROUP BY auc.ts::date, auc.group_name
ORDER BY auc.ts::date, auc.group_name;

SELECT * FROM public.daily_stats

ORDER BY date, group_name;
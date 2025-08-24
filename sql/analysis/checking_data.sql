SELECT current_database() AS db, current_user AS usr, current_schema() AS sch;

-- tables size
select count(*) as ab_data_count from raw_ab_data; -- 294478 rows
select count(*) as countries_count from raw_countries; -- 290584 rows

-- columns and data types
select column_name, data_type
from information_schema.columns
where table_name = 'raw_ab_data'
ORDER BY 1;
-- need to adjust the data type of the "timestamp" column
-- need to adjust the data type of the "converted" column
-- need to adjust the data type of user_id column

select column_name, data_type
from information_schema.columns
where table_name = 'raw_countries'
ORDER BY 1;
-- need to adjust the data type of user_id column



-- print the first 10 rows of the ab_data table
select * from raw_ab_data LIMIT 10;
-- print the first 10 rows of the countries table
select * from raw_countries LIMIT 10;


-- print all the countries in the countries table
select distinct country from raw_countries order by country; -- 3 countries

-- print all the landing pages in the ab_data table
select distinct landing_page from raw_ab_data order by landing_page; -- 2 landing pages, old and new


-- see the distribution of users in the groups
SELECT lower(trim("group")) as grp, count(*) as cnt
FROM raw_ab_data
group BY grp 
ORDER BY cnt DESC;

-- see the distribution of users in landing page
SELECT lower(trim("landing_page")) as pag, count(*) as cnt
FROM raw_ab_data
group BY pag
ORDER BY cnt DESC;


-- see if there is other value than 0,1 in the converted column
SELECT distinct converted
FROM raw_ab_data
WHERE converted NOT IN (0, 1);


-- check for duplicates in the ab_data table
SELECT user_id, COUNT(*) AS cnt
FROM raw_ab_data
GROUP BY user_id
HAVING COUNT(*) > 1
ORDER BY cnt DESC
LIMIT 20;


-- checking thae date range of the data
SELECT MIN("timestamp") AS min_date, MAX("timestamp") AS max_date
FROM raw_ab_data; -- 02/01/2017 to 24/01/2017



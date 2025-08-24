
DROP TABLE IF EXISTS ab_data;
DROP TABLE IF EXISTS countries;

CREATE TABLE ab_data (
  user_id       BIGINT,
  "timestamp"   TIMESTAMP NULL,
  group_name    TEXT,
  landing_page  TEXT,
  converted     INT
);

CREATE TABLE countries (
  user_id BIGINT,
  country TEXT
);
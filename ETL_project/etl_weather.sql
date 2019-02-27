CREATE DATABASE weather_db;

USE weather_db;

-- CREATE TABLE customer_name (
--   id INT PRIMARY KEY,
--   first_name TEXT,
--   last_name TEXT
-- );


CREATE TABLE ca_results (
 id INT PRIMARY KEY,
  measurement VARCHAR(30) NOT NULL,
  Avg INT,
  yr INT,
  State VARCHAR(30) NOT NULL
);

CREATE TABLE or_results (
 id INT PRIMARY KEY,
  measurement VARCHAR(30) NOT NULL,
  Avg INT,
  yr INT,
  State VARCHAR(30) NOT NULL
);

CREATE TABLE wa_results (
 id INT PRIMARY KEY,
  measurement VARCHAR(30) NOT NULL,
  Avg INT,
  yr INT,
  State VARCHAR(30) NOT NULL
);



CREATE DATABASE weather_db;

USE weather_db;


CREATE TABLE ca_sqlresults (
 id INT PRIMARY KEY,
  measurement VARCHAR(30) NOT NULL,
  Avg INT,
  yr INT,
  State VARCHAR(30) NOT NULL
);

CREATE TABLE or_sqlesults (
 id INT PRIMARY KEY,
  measurement VARCHAR(30) NOT NULL,
  Avg INT,
  yr INT,
  State VARCHAR(30) NOT NULL
);

CREATE TABLE wa_sqlresults (
 id INT PRIMARY KEY,
  measurement VARCHAR(30) NOT NULL,
  Avg INT,
  yr INT,
  State VARCHAR(30) NOT NULL
);


CREATE TABLE newdf15_sql (
 id INT PRIMARY KEY,
  State VARCHAR(30) NOT NULL,
  Count_symptoms INT,
  Count_no_symptoms INT,
  yr INT
);

CREATE TABLE newdf16_sql (
 id INT PRIMARY KEY,
  State VARCHAR(30) NOT NULL,
  Count_symptoms INT,
  Count_no_symptoms INT,
  yr INT
);

CREATE TABLE newdf17_sql (
 id INT PRIMARY KEY,
  State VARCHAR(30) NOT NULL,
  Count_symptoms INT,
  Count_no_symptoms INT,
  yr INT
);

SELECT*FROM ca_sqlresults;
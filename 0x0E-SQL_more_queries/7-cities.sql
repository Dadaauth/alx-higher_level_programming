-- @DB1: hbtn_0d_usa
-- @TB1: cities
-- Creates a DATABASE @DB1 with a TABLE @TB1
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the DATABASE
USE hbtn_0d_usa;
-- Create the TABLE
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id), 
	FOREIGN KEY (state_id) REFERENCES states(id)
);

-- @DB1: hbtn_0d_usa
-- @TB1: states

-- Creates the DATABASE @DB1
-- And the TABLE @TB1 in the database @DB1
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the DATABASE
USE hbtn_0d_usa;
-- Create the TABLE
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL
PRIMARY KEY, name VARCHAR(256));

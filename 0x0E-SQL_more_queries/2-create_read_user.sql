-- This script creates a new database and a new user
-- It also grants the new user 'user_0d_2' with SELECT privilege alone.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- CREATE a new user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0D_2_pwd';
-- GRANT only the SELECT privilege to the user
GRANT SELECT ON hbtn_0d_2.* to 'user_0d_2'@'localhost' WITH GRANT OPTION;

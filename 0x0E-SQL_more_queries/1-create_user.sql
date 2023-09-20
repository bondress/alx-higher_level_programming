-- This script creates the MySQL user 'user_0d_1', and doesn't fail if it already exists.
-- The user_0d_1 should have all privileges on the MySQL server
-- and its password should be set to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

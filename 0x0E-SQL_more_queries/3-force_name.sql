-- This script creates the table force_name and does not fail if table already exists.
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);

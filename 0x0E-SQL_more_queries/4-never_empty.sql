-- This script creates the table id_not_null and doesn't fail if it already exists.
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));

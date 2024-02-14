-- Create a table named users with the following attriutes:
-- id: integer, auto increment, primary key
-- email: string (255 chars), never null, unique
-- name: string (255 chars)
-- country: enumeration of the countries US, CO and TN, never null, default US
-- If the table already exists, do not throw an error.
CREATE TABLE IF NOT EXISTS users (
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);

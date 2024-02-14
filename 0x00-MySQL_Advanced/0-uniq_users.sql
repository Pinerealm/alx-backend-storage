-- Create a table named users with the following attributes:
-- id: integer, never null, auto increment and primary key
-- email: string (255 chars), never null, unique
-- name: string (255 chars)
-- If the table already exists, do not throw an error.
CREATE TABLE IF NOT EXISTS users (
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);

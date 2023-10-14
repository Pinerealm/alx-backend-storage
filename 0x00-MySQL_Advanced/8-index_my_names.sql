-- Create an index, idx_name_first, on the names table and the
-- first letter of name
CREATE INDEX idx_name_first ON names (name(1));

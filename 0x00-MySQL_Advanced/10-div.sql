-- Create a function, SafeDiv, that divides the first by the
-- second number. If the second number is 0, return 0.
DELIMITER && ;
DROP FUNCTION IF EXISTS SafeDiv&&
CREATE FUNCTION SafeDiv (a int, b int) RETURNS VARCHAR(255) DETERMINISTIC
    BEGIN
        DECLARE res1 INT DEFAULT 0;
        DECLARE res2 DOUBLE;
        IF b = 0 THEN
            RETURN CONCAT(res1);
        ELSE
            IF a % b = 0 THEN
                SET res1 = a / b;
                RETURN CONCAT(res1);
            ELSE
                SET res2 = a / b;
                RETURN CONCAT(res2);
            END IF;
        END IF;
    END&&

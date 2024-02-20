-- Create a stored procedure, AddBonus, that adds a new correction for
-- a student.
-- AddBonus takes 3 arguments:
--     user_id, a users.id value
--     project_name, a projects.name value
--     score, a correction score
DELIMITER $$
DROP PROCEDURE IF EXISTS AddBonus$$
CREATE 
    PROCEDURE AddBonus(user_id INT, project_name VARCHAR (255), score INT)
    BEGIN
        IF (SELECT project_name FROM projects WHERE name = project_name) IS NULL THEN
            INSERT INTO projects (name) VALUES (project_name);
        END IF;
        INSERT INTO corrections (user_id, project_id, score) 
            VALUES (user_id, 
                    (SELECT id FROM projects WHERE name = project_name), 
                    score);
    END $$
DELIMITER ;

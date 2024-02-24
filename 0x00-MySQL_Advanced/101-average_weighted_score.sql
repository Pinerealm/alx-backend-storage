-- Create a stored procedure, ComputeAverageWeightedScoreForUsers, that
-- computes and stores the average weighted score for all students.
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers $$
CREATE
    PROCEDURE ComputeAverageWeightedScoreForUsers ()
    BEGIN
        DECLARE done INT DEFAULT FALSE;
        DECLARE user_id INT;
        DECLARE total_score FLOAT DEFAULT 0;
        DECLARE total_weight INT DEFAULT 0;
        DECLARE avg_score FLOAT;
        DECLARE cur CURSOR FOR SELECT id FROM users;
        DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
        
        OPEN cur;
        
        read_loop: LOOP
            FETCH cur INTO user_id;
            IF done THEN
                LEAVE read_loop;
            END IF;
            
            SELECT SUM(score * weight), SUM(weight)
            INTO total_score, total_weight
            FROM corrections AS c
            JOIN projects AS p ON c.project_id = p.id
            WHERE c.user_id = user_id;
            
            SET avg_score = total_score / total_weight;
            
            UPDATE users
            SET average_score = avg_score
            WHERE id = user_id;
        END LOOP;
        
        CLOSE cur;
    END $$
DELIMITER ;

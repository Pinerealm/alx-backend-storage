-- Create a stored procedure, ComputeAverageWeightedScoreForUser, that
-- computes and stores the average weighted score for a student.
DELIMITER $$ ;
CREATE
    PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
    BEGIN
        DECLARE total_score FLOAT;
        DECLARE total_weight INT;
        DECLARE avg_score FLOAT;
        
        SET total_score = 0;
        SET total_weight = 0;
        
        SELECT SUM(score * weight), SUM(weight)
        INTO total_score, total_weight
        FROM corrections AS c
        JOIN projects AS p ON c.project_id = p.id
        WHERE c.user_id = user_id;
        
        SET avg_score = total_score / total_weight;
        
        UPDATE users
        SET average_score = avg_score
        WHERE id = user_id;
    END$$

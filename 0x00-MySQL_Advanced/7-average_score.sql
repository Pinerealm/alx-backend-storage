-- Create a stored procedure, ComputeAverageScoreForUser, that computes
-- and stores the average score for a student.
-- ComputeAverageScoreForUser takes 1 argument:
--     user_id, a users.id value
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE 
    PROCEDURE ComputeAverageScoreForUser(user_id INT)
    UPDATE users SET average_score = (SELECT AVG(score) 
                                      FROM corrections AS c
                                      WHERE c.user_id = user_id) 
    WHERE id = user_id;

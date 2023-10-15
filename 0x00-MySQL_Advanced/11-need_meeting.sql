-- Create a view, need_meeting, that lists all students that have a score
-- under 80 and have not had a meeting yet OR had a meeting more than 
-- 30 days ago.
CREATE VIEW need_meeting AS
    SELECT name
    FROM students
    WHERE score < 80 AND (last_meeting IS NULL OR 
                          last_meeting < DATE_SUB(NOW(), INTERVAL 30 DAY));

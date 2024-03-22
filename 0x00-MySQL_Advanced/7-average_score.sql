-- creates a stored procedure ComputeAverageScoreForUser
-- it computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
delimiter //
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	DECLARE avrg FLOAT;

	SELECT AVG(score) INTO avrg
	FROM corrections av
	WHERE av.user_id = user_id;

	UPDATE users SET average_score = IFNULL(avrg, 0) WHERE id = user_id;
END //
delimiter ;

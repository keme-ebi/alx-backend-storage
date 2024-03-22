-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- it computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
delimiter //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
	DECLARE weighted_avrg FLOAT;

	SELECT SUM(cor.score * pro.weight) / SUM(pro.weight) INTO weighted_avrg
	FROM users AS u
	JOIN corrections AS cor ON u.id = cor.user_id
	JOIN projects AS pro ON cor.project_id = pro.id
	WHERE cor.user_id = user_id;

	UPDATE users SET average_score = weighted_avrg WHERE id = user_id;
END //
delimiter ;

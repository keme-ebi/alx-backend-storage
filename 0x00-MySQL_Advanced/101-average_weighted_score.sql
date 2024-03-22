-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- it computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
delimiter //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
	DECLARE weighted_avrg FLOAT;
	DECLARE num_users INT;
	DECLARE user_id INT DEFAULT 1;
	SELECT count(id) INTO num_users FROM users;

	WHILE num_users > 0 DO
		SELECT SUM(cor.score * pro.weight) / SUM(pro.weight) INTO weighted_avrg
		FROM users AS u
		JOIN corrections AS cor ON u.id = cor.user_id
		JOIN projects AS pro ON cor.project_id = pro.id
		WHERE cor.user_id = user_id;
		
		UPDATE users SET average_score = weighted_avrg
		WHERE id = user_id;
		SET user_id = user_id + 1;
		SET num_users = num_users - 1;
	END WHILE;
END //
delimiter ;

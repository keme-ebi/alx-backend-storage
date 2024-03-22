-- creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER //
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name CHAR(255), IN score INT)
BEGIN
	DECLARE tmp INT;

	-- check if no project name
	IF NOT EXISTS(SELECT * FROM projects WHERE name = project_name)
		THEN INSERT INTO projects (name) VALUES (project_name);
	END IF;

	SELECT id INTO tmp
	FROM projects
	WHERE name = project_name;
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, tmp, score);
END //
DELIMITER ;

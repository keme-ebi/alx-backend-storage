-- creates a trigger that resets the attribute valid_email
-- when the email has been changed
delimiter //
CREATE TRIGGER changed_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;//
delimiter ;

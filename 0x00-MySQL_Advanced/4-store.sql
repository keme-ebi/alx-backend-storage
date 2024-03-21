-- creates a trigger that decreases the quantity of an item
-- after adding a new order
delimiter //
CREATE TRIGGER update_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	DECLARE leftover INT;
	
	-- Retrieve the name of the item
	SELECT quantity INTO leftover
	FROM items
	WHERE name = NEW.item_name;

	-- Update the quantity left
	UPDATE items
	SET quantity = leftover - NEW.number
	WHERE name = NEW.item_name;
END;//
delimiter ;

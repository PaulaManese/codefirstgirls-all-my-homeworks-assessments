USE shop;

UPDATE SALES1
SET SalesPerson = "Annette"
WHERE SalesPerson = "Inga" AND SalesAmount < 50;

-- Comment: Nice! Aliasing SALES1 would've been the cream on the cake!
-- But functionally makes no difference.
-- 5/5

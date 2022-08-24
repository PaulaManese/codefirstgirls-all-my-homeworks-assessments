USE shop;

SELECT Store,COUNT(Store) as Sales
FROM SALES1
WHERE Store = "London";

-- Comment: Nice aliasing for the column name too! Extranious data
-- with the store name is creeping in a little.
-- 4/5

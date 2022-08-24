USE shop;

SELECT SalesPerson,SUM(SalesAmount) As Total_Sales,COUNT(SalesAmount) As Number_Of_Sales
FROM SALES1
GROUP BY SalesPerson
HAVING Total_Sales <= 300
ORDER By SalesPerson ASC;

-- Comment: Smashed it, again! Just be careful about selecting extranious columns.
-- It's definitely worth keeping during development of a query and it's good
-- practice to remove it when you're done.
-- 4/5

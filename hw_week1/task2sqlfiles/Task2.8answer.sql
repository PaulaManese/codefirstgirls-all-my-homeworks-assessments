USE shop;

SELECT SalesPerson,COUNT(SalesAmount) As Number_Of_Sales
FROM SALES1
GROUP BY SalesPerson
HAVING  Number_Of_Sales < 3;

-- Comment: Nice use of HAVING here. I don't often use it but this is a nice 
-- use case.
-- 5/5

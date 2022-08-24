USE shop;

SELECT DISTINCT(SalesPerson), Day, CONCAT('£',Sum(SalesAmount)) as 'Total_Sales'
FROM SALES1
GROUP BY SalesPerson, Day;

-- Comment: Brilliant! Getting tougher now! Lovely formatting again.
-- 5/5

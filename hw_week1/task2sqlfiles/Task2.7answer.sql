USE shop;

SELECT 
    Store,
    CONCAT('£',ROUND((AVG(SalesAmount)),2)) AS Ave_Sales
FROM SALES1
Group by Store;

-- Comment: Nice! Great use of a built in functions there too.
-- 5/5

USE shop;

SELECT 
    Store,
    SUM(SalesAmount) As Total_Number_Of_Sale,
    COUNT(SalesAmount) As Number_Of_Sale,
    CONCAT('£',ROUND((AVG(SalesAmount)),2)) AS Ave_Sales,
    CONCAT('£',MIN(SalesAmount)) AS Min_Sales,
    CONCAT('£',MAX(SalesAmount)) AS Max_Sales

FROM SALES1
GROUP by Store
ORDER by Store ASC;

-- Comment: Lovely complex query. Perfect. Nice inclusion of the ROUND function.
-- 5/5

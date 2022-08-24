USE shop;

SELECT CONCAT('Week ',Week) as 'Week', Day, CONCAT('£',sum(SalesAmount)) As Sales
FROM SALES1
GROUP BY Month,Week,Day
ORDER BY Week, Day ASC;

-- Comment: Absolutely smashed it! Typically the SUM function is ommited
-- because it doesn't impact the results in this dataset but nicely done
-- with some great formatting too!
-- 5/5

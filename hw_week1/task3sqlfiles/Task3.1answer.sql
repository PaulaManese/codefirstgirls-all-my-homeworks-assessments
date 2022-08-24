USE Parts;

SELECT DISTINCT p.P_ID AS PARTID ,p.COLOUR AS 'Colour',s.SNAME AS 'Supplier Name'
FROM SUPPLIER AS s,part  AS p
WHERE s.SNAME like '%S' and s.CITY <> 'LONDON'
ORDER BY p.P_ID ASC;

-- Comment: This gives deceptive results that look close! Ultimately if you FROM 
-- multiple tables like this it turns out its effectively a CROSS JOIN which is why
-- you're results come in pairs. All in all the query isn't right but you understand the
-- tables and have the correct WHERE and general approach.
-- 1/5

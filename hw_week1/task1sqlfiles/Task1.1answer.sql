USE Parts;

SELECT 
   PNAME, WEIGHT
FROM 
   Part
WHERE 
    WEIGHT > 14
ORDER BY WEIGHT ASC, PNAME;

-- Comment: Nice! Very minor but the select was supposed to return 
-- only the name, not a problem here but could be in big queries.
-- 4/5
USE Parts;

SELECT DISTINCT s.SNAME AS 'Supplier Name',p.PNAME AS 'Parts Name',pr.JNAME AS 'Project Name'
FROM supplier AS s
INNER JOIN supply AS su ON  su.S_ID= s.S_ID
INNER JOIN part AS p ON p.P_ID = su.P_ID
INNER JOIN project  AS pr ON pr.J_ID = su.J_ID
ORDER BY s.SNAME ASC;

-- Comment: This question only needed one answer and this query is by far the
-- closest. If you include the correct WHERE for checking the suppliers,
-- project and part cities are the same, you get the results you're looking for
-- e.g. WHERE s.CITY = p.CITY AND p.CITY= pr.CITY. You did the hard part and
-- this one time I'll overlook a double submission for the question.
-- 3/5

-- Overall
-- Great start! Keep up the hard work. It was only task 3.1 that really
-- stumped you a little but other than that your queries were clean, well
-- written and nicely formatted. Just keep an eye on extranious data in your
-- SELECTs. If there's no need to return it don't. Great job and keep it up!
-- 55/65 - 85%

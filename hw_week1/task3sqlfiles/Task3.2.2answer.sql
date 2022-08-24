Use Parts;

SELECT DISTINCT s.SNAME AS 'Supplier Name',p.PNAME AS 'Parts Name',pr.JNAME AS 'Project Name', s.CITY AS 'Supplier City', p.CITY AS 'Parts City', pr.CITY AS 'Project City'
FROM supplier AS s
INNER JOIN part AS p ON p.CITY = s.CITY
INNER JOIN project  AS pr ON pr.CITY = s.CITY
ORDER BY s.SNAME ASC;
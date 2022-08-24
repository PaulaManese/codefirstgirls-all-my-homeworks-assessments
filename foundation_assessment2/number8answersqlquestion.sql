SELECT * FROM BookStore.Authors;

SELECT t2.author_name, sum(t1.sold_copies) as sold
FROM books t1
LEFT JOIN authors t2
ON t1.book_name = t2.book_name
GROUP BY t2.author_name
ORDER BY sold DESC
LIMIT 3
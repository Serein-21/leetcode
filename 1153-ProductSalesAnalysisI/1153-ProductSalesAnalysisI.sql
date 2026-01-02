-- Last updated: 1/2/2026, 12:17:42 PM
SELECT P.product_name, S.year, S.price
FROM Sales S
JOIN Product P ON S.product_id = P.product_id;


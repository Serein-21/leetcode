-- Last updated: 1/2/2026, 12:17:58 PM
SELECT name, population, area
FROM (
  SELECT name, population, area,
    CASE 
      WHEN area >= 3000000 THEN 'BIG'
      WHEN population >= 25000000 THEN 'BIG'
      ELSE 'SMALL'
    END AS result
  FROM World
) AS t
WHERE result = 'BIG';

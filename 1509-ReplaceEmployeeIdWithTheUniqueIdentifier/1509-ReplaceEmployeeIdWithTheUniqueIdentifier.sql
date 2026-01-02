-- Last updated: 1/2/2026, 12:17:37 PM
SELECT EUNI.unique_id, E.name
FROM Employees E
LEFT JOIN EmployeeUNI EUNI
ON E.id = EUNI.id;

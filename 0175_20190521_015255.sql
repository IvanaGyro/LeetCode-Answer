# Write your MySQL query statement below
SELECT P.FirstName, P.LastName, A.City, A.State 
FROM Address A
RIGHT JOIN Person P 
ON A.PersonId = P.PersonId;
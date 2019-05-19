# Write your MySQL query statement below
SELECT b.Id FROM Weather AS a INNER JOIN Weather AS b ON (DATEDIFF(b.RecordDate, a.RecordDate) = 1 AND b.Temperature > a.Temperature);
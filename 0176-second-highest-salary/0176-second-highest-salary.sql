# # Write your MySQL query statement below
# Select salary as SecondHighestSalary from Employee Order by salary DESC LIMIT 1 OFFSET 1;


SELECT (
    SELECT DISTINCT salary FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
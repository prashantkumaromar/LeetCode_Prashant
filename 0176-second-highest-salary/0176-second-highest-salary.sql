# Write your MySQL query statement below
select (Select DISTINCT salary from Employee Order by salary DESC LIMIT 1 OFFSET 1) as SecondHighestSalary;













# SELECT (
#     SELECT DISTINCT salary FROM Employee
#     ORDER BY salary DESC
#     LIMIT 1 OFFSET 1
# ) AS SecondHighestSalary;
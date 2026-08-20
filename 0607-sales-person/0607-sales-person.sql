# Write your MySQL query statement below
SELECT SalesPerson.name
FROM SalesPerson
WHERE NOT EXISTS (
SELECT 1
FROM Orders
JOIN Company
ON Orders.com_id=Company.com_id
WHERE Orders.sales_id=SalesPerson.sales_id
AND Company.name='RED')
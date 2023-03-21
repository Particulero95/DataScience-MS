SELECT A.Name as Product, SUM(LineTotal) AS TotalRevenue
FROM Production.Product AS A 
INNER JOIN Sales.SalesOrderDetail AS B 
    ON A.ProductID=B.ProductID
WHERE A.ListPrice > 1000
GROUP BY A.Name
HAVING SUM(LineTotal) > 20000
ORDER BY TotalRevenue DESC





SELECT TOP 1 * 
FROM Production.Product


SELECT TOP 1 * 
FROM Sales.SalesOrderDetail




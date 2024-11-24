SELECT 
    c.FirstName,
    SUM(fis.TaxAmt) AS TotalTaxAmt,
    AVG(fis.SalesAmount) AS AverageSalesAmount,
    AVG(fis.TotalProductCost) AS AverageTotalProductCost
FROM 
    FactInternetSales AS fis
INNER JOIN 
    DimCustomer c ON fis.CustomerKey = c.CustomerKey
INNER JOIN 
    DimProduct p ON fis.ProductKey = p.ProductKey
WHERE 
    DATENAME(WEEKDAY, fis.OrderDate) = 'Sunday'  -- Filter for Sunday sales
    AND p.Color = 'Silver'                      -- Filter for silver products
    AND p.Size IS NOT NULL                      -- Filter for products with size information
    AND p.Weight > 10                           -- Filter for products with weight > 10
    AND c.YearlyIncome > 100000.0               -- Filter for high-income customers
    AND c.NumberChildrenAtHome > 1             -- Filter for customers with more than 1 child
GROUP BY 
    c.CustomerKey, c.FirstName                  -- Grouping by CustomerKey and FirstName
ORDER BY 
    c.FirstName ASC                             -- Sorting by FirstName in ascending order;

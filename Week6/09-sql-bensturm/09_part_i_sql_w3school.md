# Challenge Set 9
## Part I: W3Schools SQL Lab 

*Introductory level SQL*

--

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.

1. Which customers are from the UK?
```SQL
SELECT * FROM Customers
	WHERE Country ='UK';
```
```
CustomerID	CustomerName	ContactName	Address	City	PostalCode	Country
4	Around the Horn	Thomas Hardy	120 Hanover Sq.	London	WA1 1DP	UK
11	B's Beverages	Victoria Ashworth	Fauntleroy Circus	London	EC2 5NT	UK
16	Consolidated Holdings	Elizabeth Brown	Berkeley Gardens 12 Brewery	London	WX1 6LT	UK
19	Eastern Connection	Ann Devon	35 King George	London	WX3 6FW	UK
38	Island Trading	Helen Bennett	Garden House Crowther Way	Cowes	PO31 7PJ	UK
53	North/South	Simon Crowther	South House 300 Queensbridge	London	SW7 1RZ	UK
72	Seven Seas Imports	Hari Kumar	90 Wadhurst Rd.	London	OX15 4NB	UK
```

2. What is the name of the customer who has the most orders?
```SQL
SELECT CustomerName, COUNT(*) AS OrderCount 
FROM Customers
JOIN Orders ON Orders.CustomerID = Customers.CustomerID
GROUP BY Customers.CustomerName
ORDER BY OrderCount DESC
LIMIT 1;
```
```
CustomerName	OrderCount
Ernst Handel	10
```

3. Which supplier has the highest average product price?
```SQL
SELECT SupplierName, AVG(Price) AS AveragePrice FROM Products
JOIN Suppliers ON Suppliers.SupplierID = Products.SupplierID
GROUP BY Suppliers.SupplierID
ORDER BY AveragePrice DESC
LIMIT 1;
```
```
SupplierName	AveragePrice
Aux joyeux ecclésiastiques	140.75
```

4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)
```SQL
SELECT DISTINCT Country FROM Customers;
```
```
Country
Germany
Mexico
UK
Sweden
France
Spain
Canada
Argentina
Switzerland
Brazil
Austria
Italy
Portugal
USA
Venezuela
Ireland
Belgium
Norway
Denmark
Finland
Poland
```

5. What category appears in the most orders?
```SQL
SELECT
    c.CategoryName, 
    COUNT(*) AS Count
FROM
    OrderDetails as o
  JOIN
    Products as p
  JOIN
    Categories AS c
  ON
      o.ProductID = p.ProductID
    AND
      p.CategoryID = c.CategoryID
GROUP BY
    c.CategoryName
ORDER BY
    Count DESC
LIMIT 1;
```
```
Dairy Products	100
```

6. What was the total cost for each order?
```SQL
SELECT
    o.OrderID,
    SUM(o.Quantity * p.Price) as Total
FROM
    OrderDetails as o
  JOIN
    Products as p
  ON
    o.ProductID = p.ProductID
GROUP BY
    o.OrderID
ORDER BY
    Total DESC;
```
```
OrderID	Total
10372	15353.6
10424	14366.5
10417	14104
10353	13427
10360	9244.250000000002
10324	7698.45
10440	7246.01
10430	7245
10351	7103.599999999999
10329	6025.12
10305	5197.25
10267	5040
10401	4837.02
10252	4662.5
10359	4572.2
10339	4330.4
10393	4135.6
10298	3909.5
10400	3829.59
10286	3772
10345	3662
...
```

7. Which employee made the most sales (by total price)?
```SQL
SELECT
    e.FirstName,
    e.LastName,
    SUM(op.Quantity * p.Price) as Total
FROM
    Employees as e
  JOIN
    Orders as o
  JOIN
    OrderDetails as op
  JOIN
    Products as p
  ON
      e.EmployeeID = o.EmployeeID
    AND
      o.OrderID = op.OrderID
    AND
      op.ProductID = p.ProductID
GROUP BY
    e.EmployeeID
ORDER BY
    Total DESC;
```
```
FirstName	LastName	Total
Margaret	Peacock	105696.49999999999
Nancy	Davolio	57690.38999999999
Janet	Leverling	42838.350000000006
Robert	King	39772.3
Laura	Callahan	39309.380000000005
Andrew	Fuller	32503.16
Steven	Buchanan	27480.8
Michael	Suyama	25399.25
Anne	Dodsworth	15734.099999999999
```

8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)
```SQL
SELECT
    *
FROM 
    Employees 
WHERE 
    Notes 
LIKE 
    '%BS%';
```
```
Leverling	Janet
Buchanan	Steven
```
9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)
```SQL
SELECT
    SupplierName,
    COUNT(*) as NumProducts,
    AVG(p.Price) as MeanPrice
FROM
    Suppliers AS s
  JOIN
    Products AS p
  ON
    s.SupplierID = p.SupplierID
GROUP BY
    s.SupplierID
HAVING
    NumProducts >= 3
ORDER BY
    MeanPrice DESC;
```
```
SupplierName	NumProducts	MeanPrice
Tokyo Traders	3	46
Plutzer Lebensmittelgroßmärkte AG	5	44.678000000000004
Pavlova, Ltd.	5	35.57
Grandma Kelly's Homestead	3	31.666666666666668
G'day, Mate	3	30.933333333333334
Heli Süßwaren GmbH & Co. KG	3	29.709999999999997
Specialty Biscuits, Ltd.	4	28.175
Leka Trading	3	26.483333333333334
Formaggi Fortini s.r.l.	3	26.433333333333334
New Orleans Cajun Delights	4	20.35
Norske Meierier	3	20
Svensk Sjöföda AB	3	20
Karkki Oy	3	18.083333333333332
Exotic Liquid	3	15.666666666666666
Bigfoot Breweries	3	15.333333333333334
Mayumi's	3	14.916666666666666
```

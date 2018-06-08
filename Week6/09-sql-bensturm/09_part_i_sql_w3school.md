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
SELECT CategoryID, Count(*) AS CategoryCount FROM Products
JOIN OderDetails ON OrderDetails.ProductID = Products.ProductID
GROUP BY OrderDetails.OrderID
ORDER BY CategoryCount DESC
LIMIT 1;
```

6. What was the total cost for each order?

7. Which employee made the most sales (by total price)?

8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)

9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)

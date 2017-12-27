
# MySQL Notes
Howard J, 12/22/2017  
Main reference: work of Jana Schaich Borg


### Database Normalization
**3NF**  
* Do not replicate data. Instead, reference data; point at data.  
* Use integers for keys and for references
* Add a special 'key' column to each table, which you will make references to.

**Three Kinds of Keys**  
*Primary Key:* generally an integer auto-increment field
*Logical Key:* what the outside world uses for lookup  
*Foreign Key:* generally an integer key pointing to a row in another table  
The best practice: never use your logical key as the primary key.

*Example:* in a table called *Album*  
Name | Example | Type
---  | --- | ---
Primary Key | album_id | numeric
Logical Key | title | string
Foreign Key | artist_id | numeric


---
## Data Types
Sometimes empty strings are registered as non-NULL values.    
`WHERE breed_group IS NOT NULL AND breed_group!="None" AND breed_group!=""`

In Jupyter Notebook 'NULL' values are shown as 'None'.


## Naming Convention

Use underscores where you would naturally include a space in the name.  

**Database** name is a singular noun comprising one or more words, in lowercase joined with underscore `_`, e.g., dognitiondb.  

**Table** name is a plural noun comprising one or more words, in lowercase joined with underscore `_`, e.g., complete_tests, dogs. Do not prefix with *tbl* or any other such descriptive prefix or Hungarian notation. Avoid, where possible, concatenating two table names together to create the name of a relationship table. Rather than *cars_mechanics* prefer *services*. It is preferable not to use plural.      

**Alias**. Use camel case.

**Junction table** created to support many-to-many relationship between two tables may include both the table name, (e.g., *suppliers_products*, *moives_actors*) or an action verbs (e.g., *writes* (author writes books)).  



*MySQL displays database names and table names in lowercase, but column names in its original case.*  

It is a good practice NOT to include special characters, especially blank, in names. Avoid reserved words. Backquote the names, if they contain special characters, or are SQL reserved words, e.g., *date*, *order*, *Customer ID*. It is a good practice to always backquote the names in script.

---

## Exploratory
Database:  
`SHOW TABLES`

Table:  
`DESCRIBE tableName`
`SHOW COLUMNS FROM tableName`

Limit output:
`LIMIT 10 OFFSET 5`
`LIMIT 5, 10`

---

## Formatting Selected Data
### Alias
**for column**  
`SELECT dog_guid, created_at AS time_stamp`  
`SELECT dog_guid, created_at AS "time stamp"`   

**for table**  
`FROM complete_tests AS tests`  

### DISTINCT
Useful for:  
* Duplicate rows.    
* Multiple instances of the same value in a column.    

```SQL
SELECT DISTINCT breed
FROM dogs
```
![Distinct Value](sql_figures/SQL3_distinct1.png)  

```SQL
SELECT DISTINCT breed
FROM dogs
GROUP BY breed
```  
![Distinct Value](sql_figures/SQL3_distinct2.png)  

* When the `DISTINCT` clause is used with multiple columns, we get the combination of all the columns.  
```SQL
SELECT DISTINCT test_name, subcategory_name
FROM complete_tests
```
![Distinct Value](sql_figures/SQL3_distinct3.png)  


### Difference between `DISTINCT column_name`, `COUNT(DISTINCT column_name)` and `GROUP BY column_name`
If you want to infer the number of distinct entries from the results of a query using `JOIN` and `GROUP BY` clauses, remember to include an `IS NOT NULL` clause to ensure you are not counting 'NULL' values.  

* Include 'NULL' value:
```SQL
SELECT DISTINCT dog_guid
FROM complete_tests
```
![Distinct Value](sql_figures/SQL8_join_distinct1.png)  
```SQL
SELECT dog_guid
FROM complete_tests
GROUP BY dog_guid
```
![Distinct Value](sql_figures/SQL8_join_distinct3.png)  

* Exclude 'NULL' values:
```SQL
SELECT COUNT(DISTINCT dog_guid)
FROM complete_tests
```
![Distinct Value](sql_figures/SQL8_join_distinct2.png)  

### (Select and) Count Multiple Distinct Columns
Using subquery, we can count multiple distinct columns.  
```SQL
SELECT COUNT(*)
FROM (SELECT DISTINCT test_name, subcategory_name
      FROM complete_tests) AS distinct_tests
```
![Distinct Value](sql_figures/SQL8_join_distinct4.png)  


### ORDER BY
You include all the fields (or aliases) by which you want to sort the results after the ORDER BY clause, separated by commas, in the order you want them to be used for sorting.   
```sql
SELECT DISTINCT user_guid, state, membership_type
FROM users
WHERE country="US" AND state IS NOT NULL and membership_type IS NOT NULL
ORDER BY state ASC, membership_type ASC
```
![Distinct Value](sql_figures/SQL3_distinct4.png)  


### Jupyter Notebook Export
*Example:*  
`breed_list = %sql SELECT DISTINCT breed FROM dogs ORDER BY breed`  
`breed_list.csv('breed_list.csv')`  

### SQL string fuctions
*Example:*  
```SQL
SELECT DISTINCT breed,
REPLACE(breed,'-','') AS breed_fixed
FROM dogs
ORDER BY breed_fixed
```
```SQL
SELECT DISTINCT breed,
TRIM(LEADING '-' FROM breed) AS breed_fixed
FROM dogs
ORDER BY breed_fixed
```

---

## Summarise (aggregate)
Common aggregate functions, on a variable, across all observations:  
`AVG`, `COUNT`, `MAX`, `MIN`, `SUM`  

`COUNT` is used to report how many rows. When a column is included in a count function, null values are ignored in the count. When an asterisk is included in a count function, nulls are included in the count..

Two different counting scopes:  
* count the number of rows in a certain column, `COUNT(column_name)`  
* count the number of rows, `COUNT(*)`, which might take much longer time   

We can use it as a method to quickly know how many NULL values in a certain column.  

`COUNT(*) = COUNT(column_name) + SUM(ISNULL(column_name))`   

*Example:*  
```SQL
SELECT SUM(ISNULL(exclude))
FROM dogs
```

*Example:* Using `COUNT` and `SUM` to do the same thing. How many of these negative Duration entries are there?  
```SQL
SELECT COUNT(TIMESTAMPDIFF(MINUTE, start_time, end_time))
FROM exam_answers
WHERE TIMESTAMPDIFF(MINUTE, start_time, end_time) < 0
```
```SQL
SELECT SUM(TIMESTAMPDIFF(MINUTE, start_time, end_time) < 0)
FROM exam_answers
```


## Group By
### `GROUP BY` Clause
As a strong rule of thumb, if you are grouping by a column, you should also include that column in the SELECT statement. We can group by multiple columns or derived fields and MySQL allows you to use aliases in a group by clause
* To ensure the output is ordered in a way you intend, add an `ORDER BY` clause to your grouped query
* MySQL, allow you to use numbers in place of field names in the GROUP BY or ORDER BY fields to reduce the overall length of the queries.  
* Can query subsets of aggregated groups using the `HAVING` clause. Only computable at the aggregated group level

*Example:* examine the number of tests completed only during the winter holiday months of November and December. (Limits non-aggregated data.)
```SQL
SELECT test_name, MONTH(created_at) AS Month, COUNT(created_at) AS Num_Completed_Tests
FROM complete_tests
WHERE MONTH(created_at)=11 OR MONTH(created_at)=12
GROUP BY 1, 2
ORDER BY 3 DESC;
```

### Common `GROUP BY` mistake
MySQL allows user to mix grouped aggregated and non-aggregated data. The only way to be sure how the MySQL database will summarize a set of data in a SELECT clause is to tell it how to do so with an aggregate function.

*Example:* common mistake.
```SQL
SELECT test_name, MONTH(created_at) AS test_month, COUNT(created_at) AS test_count
FROM complete_tests
GROUP BY test_month
ORDER BY test_month ASC, test_name ASC
```

---

## Join
Without telling how the tables are related, *Cartesian product* will be performed. In other words, every single row of the dogs table will get paired with every single row of the reviews table.    

To prevent this from happening, tell the database how to relate the tables.    

### `INNER JOIN` or `JOIN`
* 'Equijoin' syntax:   
```SQL
FROM dogs d, reviews r
WHERE d.dog_guid = r.dog_guid AND d.user_guid = r.user_guid
```  
* Traditional syntax:  
```SQL
FROM dogs d JOIN reviews r
ON d.dog_guid = r.dog_guid AND d.user_guid = r.user_guid
```

### `LEFT/RIGHT OUTER JOIN` or `LEFT/RIGHT JOIN`
In this case, it becomes important to use the common variable from which table to select or group by.

*Example:*  it is very interesting to see that in *dogs* table all the *dog_guid* values `IS NULL`. After *users* table `LEFT JOIN` *dogs*, there are some `NULL` values in *dog_guid*.   

This example can also be used to calculate number of distinct fields that were in the left table, but not the right table.   

```SQL
SELECT dog_guid AS dDogID, breed
FROM dogs
WHERE dog_guid IS NULL
```
![Left and Right Variable](sql_figures/SQL8_join_1.png)  

```SQL
SELECT u.user_guid AS uUserID, d.user_guid AS dUserID, d.dog_guid AS dDogID, d.breed
FROM users u LEFT JOIN dogs d
ON u.user_guid = d.user_guid
WHERE d.dog_guid IS NULL
```
![Left and Right Variable](sql_figures/SQL8_join_2.png)  



### Duplicate Row / Field Values
*Cartesian product* applies. Each one of the rows in one table get paired up with each row in anther table that had the same field values.  

*Example:* Because of Cartesian product, the duplicate rows become $502 \times 1819 = 913138$. Since the duplicates for that field in this example exist in both tables, `JOIN` or `LEFT/RIGHT JOIN` produce the same Cartesian product result for that field.  

```SQL
SELECT COUNT(*)
FROM users
WHERE user_guid = 'ce7b75bc-7144-11e5-ba71-058fbc01cf0b'
```
![Duplicate](sql_figures/SQL8_join_duplicate1.png)  

```SQL
SELECT COUNT(*)
FROM dogs
WHERE user_guid = 'ce7b75bc-7144-11e5-ba71-058fbc01cf0b'
```
![Duplicate](sql_figures/SQL8_join_duplicate2.png)  

```SQL
SELECT u.user_guid AS uUserID, COUNT(*) AS rowCount
FROM users u LEFT JOIN dogs d
ON u.user_guid=d.user_guid
GROUP BY u.user_guid
ORDER BY rowCount DESC
```
![Duplicate](sql_figures/SQL8_join_duplicate3.png)  

```SQL
SELECT u.user_guid AS uUserID, COUNT(*) AS rowCount
FROM users u JOIN dogs d
ON u.user_guid=d.user_guid
GROUP BY u.user_guid
ORDER BY rowCount DESC
```
![Duplicate](sql_figures/SQL8_join_duplicate4.png)  


---

## Logical operators
Expressions that use logical operators return a result of "true" or "false", which is usually used to determine which, if any, subsequent parts of your query will be run.  


### IF
`IF` expressions are used to return one of two results based on whether inputs to the expressions meet the conditions you specify. They are frequently used in SELECT statements as a compact way to rename values in a column.   

`IF([your conditions],[result you want if conditions are met],[result you want if conditions are NOT met]) (AS [column name])`  

*Example:* a subquery with an IF statement to retrieve a list of unique $user_guid$ with their classification as either an early or late user. Notice that `IF` expression creates a new non-aggregated column.    
```SQL
SELECT cleaned_users.user_guid as UserID,
       IF(cleaned_users.first_account<'2014-06-01','early_user','late_user') AS user_type
FROM (SELECT user_guid, MIN(created_at) AS first_account
      FROM users
      GROUP BY user_guid) AS cleaned_users
```

*Example:* use `GROUP BY` statement to aggregate the output column from `IF`    
```SQL
SELECT IF(cleaned_users.first_account<'2014-06-01','early_user','late_user') AS user_type, COUNT(cleaned_users.first_account)
FROM (SELECT user_guid, MIN(created_at) AS first_account
      FROM users
      GROUP BY user_guid) AS cleaned_users
GROUP BY user_type
```

The `IF` function is not supported by all database platforms, and some spell the function as `IIF`.  


### CASE  
The main purpose of `CASE` expressions is to return a singular value based on one or more conditional tests. You can think of `CASE` expressions as an efficient way to write a set of `IF` and `ELSEIF` statements.  

If an `ELSE` expression is omitted, `NULL` values will be outputted for all rows that do not meet any of the conditions stated explicitly in the expression `CASE` expressions can be used anywhere in a SQL statement, including in `GROUP BY`, `HAVING`, and `ORDER BY` clauses or the `SELECT` column list. You will find that `CASE` statements are useful in many contexts. For example, they can be used to rename or revise values in a column.  

**If you need to manipulate values in a current column of your data:**  
```
CASE
  WHEN [condition set 1] THEN [result you want when the conditions in set 1 are met]
  WHEN [condition set 2] THEN [result you want when the conditions in set 2 are met]
  WHEN [condition set 3] THEN [result you want when the conditions in set 3 are met]
  ELSE [result you want when none of the condition sets are met]
END (AS [column name])
```
*Example:*  
```SQL
SELECT CASE WHEN cleaned_users.country="US" THEN "In US"
            WHEN cleaned_users.country="N/A" THEN "Not Applicable"
            ELSE "Outside US"
            END AS US_user,
      count(cleaned_users.user_guid)   
FROM (SELECT DISTINCT user_guid, country
      FROM users
      WHERE country IS NOT NULL) AS cleaned_users
GROUP BY US_user
```

**If you need to manipulate values in a current column of your data:**  
```
CASE [column name or expression]
  WHEN [value 1] THEN [result you want when value 1]
  WHEN [value 2] THEN [result you want when value 2]
  WHEN [value 3] THEN [result you want when value 3]
  ELSE [result you want when none of the rows equals to any of the specified values]
END (AS [column name])
```
*Example:*  
```SQL
SELECT CASE cleaned_users.country
            WHEN "US" THEN "In US"
            WHEN "N/A" THEN "Not Applicable"
            ELSE "Outside US"
            END AS US_user,
      count(cleaned_users.user_guid)   
FROM (SELECT DISTINCT user_guid, country
      FROM users
      WHERE country IS NOT NULL) AS cleaned_users
GROUP BY US_user
```


**`CASE` and `IF` are equivalent, when conditional logic to output two groups**  
```SQL
SELECT dog_guid, exclude,
    CASE exclude
        WHEN "1" THEN "exclude"
        ELSE "keep"
    END AS exclude_cleaned
FROM dogs
```
```SQL
SELECT dog_guid, exclude,
     IF(exclude = '1','exclude', 'keep') AS exclude_cleaned
FROM dogs
```


**the order of operations within logical expressions:**  
1: `NOT`  
2: `AND`  
3: `OR`  

*Example:* compare the following two queries.  
```SQL
SELECT COUNT(DISTINCT dog_guid),
CASE WHEN exclude!='1' AND breed_group='Sporting' OR breed_group='Herding' THEN "group 1"
     ELSE "everything else"
     END AS group_name
FROM dogs
GROUP BY group_name
```
```SQL
SELECT COUNT(DISTINCT dog_guid),
CASE WHEN exclude!='1' AND (breed_group='Sporting' OR breed_group='Herding') THEN "group 1"
     ELSE "everything else"
     END AS group_name
FROM dogs
GROUP BY group_name
```

## JOIN

**Equijoin syntax Vs traditional join syntax**  
*Example:* write a query to output the dog_guid, breed group, state of the owner, and zip of the owner for each distinct dog in the Working, Sporting, and Herding breed groups.  
```SQL
SELECT DISTINCT d.dog_guid, d.breed_group, u.state, u.zip
FROM dogs d, users u
WHERE d.user_guid = u.user_guid
AND d.breed_group in ('Working', 'Sporting', 'Herding')
```

```SQL
SELECT DISTINCT d.dog_guid, d.breed_group, u.state, u.zip
FROM dogs d JOIN users u
  ON d.user_guid = u.user_guid
WHERE d.breed_group in ('Working', 'Sporting', 'Herding')
```


## Subqueries and Derived Tables
### Introduction
**Subqueries**, which are also sometimes called *inner queries* or *nested queries*, are queries that are embedded within the context of another query. The output of a subquery is incorporated into the queries that surround it. Subqueries can be used in `SELECT`, `WHERE`, and `FROM` clauses. When they are used in `FROM` clauses they create what are called *derived tables*.  

**The main reasons:**  
* Sometimes they are the most logical way to retrieve the information.  
* Sometimes they run faster than joins.  
* They can be used to isolate each logical part of a statement, which can be helpful for troubleshooting long and complicated queries.     

**Uniqueness:**  
* Must be enclosed in parentheses.  
* ORDER BY phrases cannot be used in subqueries (although ORDER BY phrases can still be used in outer queries that contain subqueries).
* Subqueries in SELECT or WHERE clauses that return more than one row must be used in combination with operators that are explicitly designed to handle multiple values, such as the IN operator. Otherwise, subqueries in SELECT or WHERE statements can output no more than 1 row.

### On the fly calculations
This allows you to use a summary calculation in your query without having to enter the value outputted by the calculation explicitly. A situation when this capability would be useful is if you wanted to see all the records that were greater than the average value of a subset of your data.

The subquery: calculating the average amount of time it took customers to complete all of the tests in the exam_answers table, excluding negative durations. Then compare TIMESTAMPDIFF to the singular average value outputted by the subquery surrounded by parentheses.  

*Example:* used in `WHERE` clause  
```SQL
SELECT *
FROM exam_answers
WHERE TIMESTAMPDIFF(minute,start_time,end_time) >
    (SELECT AVG(TIMESTAMPDIFF(minute,start_time,end_time)) AS AvgDuration
     FROM exam_answers
     WHERE TIMESTAMPDIFF(minute,start_time,end_time)>0);
```

### Testing membership
Useful for assessing whether groups of rows are members of other groups of rows, with `IN`, `NOT IN`, `EXISTS`, and `NOT EXISTS` operators. `IN`, `NOT IN`: a condensed way of writing a sequence of OR statements.  

**`IN` vs `EXISTS`**  
* `EXISTS` and `NOT EXISTS` can only be used in subqueries.  
* `EXISTS` and `NOT EXISTS` are not preceded by a column name or any other expression.
* `EXISTS` and `NOT EXISTS` are logical statements, returning a value of TRUE or FALSE. As a practical consequence, the subqueries after EXISTS statements are often written `WHERE EXISTS (SELECT * ...)`  

*Example:*  For each row from $users$ table, check if there exists a row in the $dogs$ table that meets the condition `u.user_guid =d.user_guid`. When you find the first matching row, stop right there - the `WHERE EXISTS` has been satisfied. The subquery is executed for each table row of the outer query.  
```SQL
SELECT DISTINCT u.user_guid AS uUserID
FROM users u
WHERE EXISTS (SELECT *
              FROM dogs d
              WHERE u.user_guid =d.user_guid);
```

*Example:* Use a NOT EXISTS clause to examine all the users in the dogs table that are not in the users table.  
```SQL
SELECT d.user_guid, d.dog_guid
FROM dogs d
WHERE NOT EXISTS (SELECT *
                 FROM users u
                 WHERE u.user_guid = d.user_guid)
```



### Accurate logical representations of desired output and Derived Tables
A third situation in which subqueries can be useful is when they simply represent the logic of what you want better than joins.  

*Queries that include subqueries always run the innermost subquery first, and then run subsequent queries sequentially in order from the innermost query to the outermost query*. Since the subquery is in the `FROM` statement, it actually creates a temporary table, called a **derived table**, that is then incorporated into the rest of the query.

First, an alias of *DistinctUUsersID* is used to name the results of the subquery. *We are required to give an alias to any derived table we create in subqueries within FROM statements*.  

Second, we need to use this alias every time we want to execute a function that uses the derived table.  

Third, relatedly, aliases used within subqueries can refer to tables outside of the subqueries. However, outer queries cannot refer to aliases created within subqueries unless those aliases are explicitly part of the subquery output.

Another thing to take note of is that when you use subqueries in FROM statements, the temporary table you create can have multiple columns in the output (unlike when you use subqueries in outside SELECT statements). But for that same reason, subqueries in FROM statements can be very computationally intensive. Therefore, it's a good idea to use them sparingly, especially when you have very large data sets.


*Example:* wanted a list of each dog that a user in the $users$ table owns, with its accompanying breed information whenever possible.  
```SQL
SELECT u.user_guid AS uUserID, d.user_guid AS dUserID, d.dog_guid AS dDogID, d.breed
FROM users u LEFT JOIN dogs d
  ON u.user_guid=d.user_guid
```

![Exploding Rows](sql_figures/SQL9_Subqueries_and_Derived_Tables_exploding_rows1.png)


*Example:* to find out how many duplications:
```SQL
SELECT u.user_guid AS uUserID, d.user_guid AS dUserID, count(*) AS numrows
FROM users u LEFT JOIN dogs d
  ON u.user_guid=d.user_guid
GROUP BY u.user_guid
ORDER BY numrows DESC
```
![Exploding Rows](sql_figures/SQL9_Subqueries_and_Derived_Tables_exploding_rows2.png)

*Example:* take a look the duplicate data:
```SQL
SELECT DistictUUsersID.user_guid AS userid, d.breed, d.weight, count(*) AS numrows
FROM (SELECT DISTINCT u.user_guid
      FROM users u) AS DistictUUsersID
LEFT JOIN dogs d
  ON DistictUUsersID.user_guid=d.user_guid
GROUP BY DistictUUsersID.user_guid
HAVING numrows>10
ORDER BY numrows DESC;
```
![Exploding Rows](sql_figures/SQL9_Subqueries_and_Derived_Tables_exploding_rows6.png)


*Example:* We could simply join the distinct $user_guid$ from the $users$ table in the first place:  
```SQL
SELECT DistinctUUsersID.user_guid AS uUserID, d.user_guid AS dUserID, count(*) AS numrows
FROM (SELECT DISTINCT u.user_guid
      FROM users u) AS DistinctUUsersID
LEFT JOIN dogs d
  ON DistinctUUsersID.user_guid=d.user_guid
GROUP BY DistinctUUsersID.user_guid
ORDER BY numrows DESC
```
![Exploding Rows](sql_figures/SQL9_Subqueries_and_Derived_Tables_exploding_rows3.png)


*Example:* also select the distinct $user_guid$ from the $dogs$ table:  
```SQL
SELECT DistinctUUsersID.user_guid AS uUserID, DistinctDUserID.user_guid AS dUserID, count(*) AS numrows
FROM (SELECT DISTINCT u.user_guid
      FROM users u) AS DistinctUUsersID
LEFT JOIN (SELECT DISTINCT d.user_guid
           FROM dogs d) AS DistinctDUserID
  ON DistinctUUsersID.user_guid=DistinctDUserID.user_guid
GROUP BY DistinctUUsersID.user_guid
ORDER BY numrows DESC;
```
![Exploding Rows](sql_figures/SQL9_Subqueries_and_Derived_Tables_exploding_rows4.png)

*Example:* now we are ready to extract data as we know no duplicate row exists:
```SQL
SELECT DistinctUUsersID.user_guid AS uUserID, DistictDUsersID.user_guid AS dUserID,
DistictDUsersID.dog_guid AS DogID, DistictDUsersID.breed AS breed
FROM (SELECT DISTINCT u.user_guid
      FROM users u
      LIMIT 100) AS DistinctUUsersID
LEFT JOIN (SELECT DISTINCT d.user_guid, d.dog_guid, d.breed
            FROM dogs d) AS DistictDUsersID
  ON DistinctUUsersID.user_guid=DistictDUsersID.user_guid
GROUP BY DistinctUUsersID.user_guid;
```
![Exploding Rows](sql_figures/SQL9_Subqueries_and_Derived_Tables_exploding_rows5.png)

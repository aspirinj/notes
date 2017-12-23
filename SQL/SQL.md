
# MySQL Notes
Howard J, 12/22/2017  
Based on work of Jana Schaich Borg


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

First, an alias of "DistinctUUsersID" is used to name the results of the subquery. *We are required to give an alias to any derived table we create in subqueries within FROM statements*.  

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

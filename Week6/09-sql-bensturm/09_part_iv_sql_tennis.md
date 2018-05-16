# Challenge Set 9
## Part IV: Tennis Data

*Intermediate - Advanced level SQL*

---

### Acquire data ###

Let's get some data and start playing with it!

We'll be using tennis data from [here](https://archive.ics.uci.edu/ml/datasets/Tennis+Major+Tournament+Match+Statistics).


Assuming you are working on your AWS instance, execute the following from the BASH (shell) terminal:

```bash
mkdir -p tennis/data
cd tennis/data
wget http://archive.ics.uci.edu/ml/machine-learning-databases/00300/Tennis-Major-Tournaments-Match-Statistics.zip
```

You may not have `unzip` installed on your AWS instance:

```bash
sudo apt-get install unzip
unzip Tennis-Major-Tournaments-Match-Statistics.zip
```

Before we start using SQL, open up the files with your favorite command line text editor and poke around!


### Prepare the data ###

The data has a mix of missing entries and entries that are the string `NA`. We'll use the command line program `sed` to fix that:

```bash
sed -i.bak s/NA//g AusOpen-women-2013.csv
```

Repeat this for each CSV file in the data set.

### Import the data into PostgreSQL ###

Now we start working in PostgreSQL. The remaining commands are executed from the SQL prompt.

You can create a new database with `CREATE DATABASE tennis;` -- if we use `\d`, we see there are not yet any tables (relations) in the database. So let's create one.

We have to specify the schema of our table, with detail about [data types](http://www.postgresql.org/docs/9.3/static/datatype.html).

```sql
CREATE TABLE  aus_ladies_2013 (
      player1 VARCHAR(255),
      player2 VARCHAR(255),
      round INT,
      result INT,
      fnl1 DOUBLE PRECISION,
      fnl2 DOUBLE PRECISION,
      fsp_1 DOUBLE PRECISION,
      fsw_1 DOUBLE PRECISION,
      ssp_1 DOUBLE PRECISION,
      ssw_1 DOUBLE PRECISION,
      ace_1 INT,
      dbf_1 INT,
      wnr_1 INT,
      ufe_1 INT,
      bpc_1 INT,
      bpw_1 INT,
      npa_1 INT,
      npw_1 INT,
      tpw_1 INT,
      st1_1 INT,
      st2_1 INT,
      st3_1 INT,
      st4_1 INT,
      st5_1 INT,
      fsp_2 DOUBLE PRECISION,
      fsw_2 DOUBLE PRECISION,
      ssp_2 DOUBLE PRECISION,
      ssw_2 DOUBLE PRECISION,
      ace_2 INT,
      dbf_2 INT,
      wnr_2 INT,
      ufe_2 INT,
      bpc_2 INT,
      bpw_2 INT,
      npa_2 INT,
      npw_2 INT,
      tpw_2 INT,
      st1_2 INT,
      st2_2 INT,
      st3_2 INT,
      st4_2 INT,
      st5_2 INT);
```

Now load data from a CSV file into this table:

```sql
COPY 
      aus_ladies_2013
FROM 
      '/home/my_user_name/tennis/data/AusOpen-women-2013.csv'
DELIMITER 
      ','
CSV HEADER;
```

Repeat this process for all of the other tables. *Hint:* You can make a new table with the same schema as an existing table. For example:

```sql
CREATE TABLE 
      aus_men_2013 
(LIKE 
      aus_ladies_2013);
```

Extension: Can you make the tennis data tidy?


### Some practice SQL queries ###

The following SQL commands can be used to explore the data. To maximize understanding of the syntax, type these rather than copying and pasting.

```sql
SELECT 
      player1, player2, result 
FROM 
      us_men_2013 
LIMIT 5;


SELECT
      player1, result 
FROM 
      us_men_2013 
WHERE 
      player1 = 'Richard Gasquet';


SELECT 
      player1, player2, result
FROM
      us_men_2013 
WHERE 
      player1 = 'Richard Gasquet';


SELECT
      player1, player2, result 
FROM 
      us_men_2013 
WHERE 
      player1 = 'Richard Gasquet' OR player2 = 'Richard Gasquet';


SELECT 
      COUNT(*)
FROM
      us_men_2013;


SELECT
      player1, COUNT(*) 
FROM 
      us_men_2013 
GROUP BY 
      player1;


SELECT 
      player1, AVG(result) 
FROM 
      us_men_2013 
GROUP BY
      player1;


SELECT 
      player1, player2, result 
FROM 
      us_men_2013 
WHERE 
      result = 1 
LIMIT 5;


SELECT 
      COUNT(*) 
FROM 
      us_men_2013 
WHERE 
      result = 1;


SELECT 
      player1, player2, result 
FROM 
      french_men_2013 
WHERE 
      result = 1 
LIMIT 5;


SELECT 
      us_men_2013.player1, us_men_2013.tpw_1, french_men_2013.tpw_1 
FROM 
      us_men_2013, french_men_2013 
WHERE 
      us_men_2013.player1 = french_men_2013.player1;


SELECT 
      us_men_2013.player1, 
      SUM(us_men_2013.tpw_1) AS us_points, 
      SUM(french_men_2013.tpw_1) AS french_points
FROM 
      us_men_2013, french_men_2013 
WHERE 
      us_men_2013.player1 = french_men_2013.player1 
GROUP BY 
      us_men_2013.player1;


SELECT
      us_men_2013.player1, 
      SUM(us_men_2013.tpw_1) AS us_points, 
      SUM(french_men_2013.tpw_1) AS french_points, 
      SUM(us_men_2013.tpw_1 + french_men_2013.tpw_1) AS total_points 
FROM
      us_men_2013, french_men_2013 
WHERE 
      us_men_2013.player1 = french_men_2013.player1
GROUP BY
      us_men_2013.player1;
```


## The challenges!

This challenge uses only SQL queries. Please submit answers in a markdown file.

1. Using the same tennis data, find the number of matches played by
   each player in each tournament. (Remember that a player can be
   present as both player1 or player2).

2. Who has played the most matches total in all of US Open, AUST Open, 
   French Open? Answer this both for men and women.

3. Who has the highest first serve percentage? (Just the maximum value
   in a single match.)

4. What are the unforced error percentages of the top three players
   with the most wins? (Unforced error percentage is % of points lost
   due to unforced errors. In a match, you have fields for number of
   points won by each player, and number of unforced errors for each
   field.)


*Hint:* `SUM(double_faults)` sums the contents of an entire column. For each row, to add the field values from two columns, the syntax `SELECT name, double_faults + unforced_errors` can be used.


*Special bonus hint:* To be careful about handling possible ties, consider using [rank functions](http://www.sql-tutorial.ru/en/book_rank_dense_rank_functions.html).

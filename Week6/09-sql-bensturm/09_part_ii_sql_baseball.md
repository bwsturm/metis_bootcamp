# Challenge Set 9
## Part II: Baseball Data

*Introductory - Intermediate level SQL*

--

Please complete this exercise via SQLalchemy and Jupyter notebook.

We will be working with the Lahman baseball data we uploaded to your AWS instance in class. 


1. What was the total spent on salaries by each team, each year?

2. What is the first and last year played for each player? *Hint:* Create a new table from 'Fielding.csv'.

3. Who has played the most all star games?

4. Which school has generated the most distinct players? *Hint:* Create new table from 'CollegePlaying.csv'.

5. Which players have the longest career? Assume that the `debut` and `finalGame` columns comprise the start and end, respectively, of a player's career. *Hint:* Create a new table from 'Master.csv'. Also note that strings can be converted to dates using the [`DATE`](https://wiki.postgresql.org/wiki/Working_with_Dates_and_Times_in_PostgreSQL#WORKING_with_DATETIME.2C_DATE.2C_and_INTERVAL_VALUES) function and can then be subtracted from each other yielding their difference in days.

6. What is the distribution of debut months? *Hint:* Look at the `DATE` and [`EXTRACT`](https://www.postgresql.org/docs/current/static/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT) functions.

7. What is the effect of table join order on mean salary for the players listed in the main (master) table? *Hint:* Perform two different queries, one that joins on playerID in the salary table and other that joins on the same column in the master table. You will have to use left joins for each since right joins are not currently supported with SQLalchemy.

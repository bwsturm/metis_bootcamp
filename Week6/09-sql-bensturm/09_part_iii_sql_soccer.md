# Challenge Set 9
## Part III: Soccer Data

*Introductory - Intermediate level SQL*

--

Please complete this exercise using sqlite3 and Jupyter notebook.

Download the [SQLite database](https://www.kaggle.com/hugomathien/soccer/downloads/soccer.zip) and load in your notebook using the sqlite3 library. 

1. Which team scored the most points when playing at home?  

2. Did this team also score the most points when playing away?  

3. How many matches resulted in a tie?  

4. How many players have Smith for their last name? How many have 'smith' anywhere in their name?

5. What was the median tie score? Use the value determined in the previous question for the number of tie games. *Hint:* PostgreSQL does not have a median function. Instead, think about the steps required to calculate a median and use the [`WITH`](https://www.postgresql.org/docs/8.4/static/queries-with.html) command to store stepwise results as a table and then operate on these results. 

6. What percentage of players prefer their left or right foot? *Hint:* Calculate either the right or left foot, whichever is easier based on how you setup the problem.

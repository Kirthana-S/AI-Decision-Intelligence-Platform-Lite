# Sprint 4 - SQL Analytics & Backend Development

## Sprint Goal

The objective of Sprint 4 is to strengthen the backend analytics layer of the AI Decision Intelligence Platform by introducing SQL-based analytics. This sprint focuses on building reusable SQL objects, answering business questions through SQL, and learning advanced SQL concepts commonly used by Data Analysts.

---

# Task 1 - SQLite Environment Setup

## Objective

Set up a local SQLite database to simulate a production analytics database.

### Activities Completed

- Installed SQLite extension in Visual Studio Code.
- Connected to the local SQLite database.
- Verified successful database connection.
- Explored the database using SQLite Explorer.

### Skills Learned

- SQLite
- Database connectivity
- Database exploration

---

# Task 2 - Database Schema Review

## Objective

Understand the structure of the analytics database.

### Tables Reviewed

### players

Contains player information including:

- Player ID
- Name
- Country
- Registration Date
- Age

### bets

Contains betting activity including:

- Bet ID
- Player ID
- Game
- Stake
- Result
- Payout
- Bet Date

### transactions

Contains financial transactions including:

- Transaction ID
- Player ID
- Transaction Type
- Amount
- Transaction Date

### Outcome

Understood how all tables relate through the Player ID field.

---

# Task 3 - SQL Views

## Objective

Create reusable business views that simplify reporting and future analytics.

### Views Created

### vw_country_revenue

Purpose

Aggregates revenue by country.

Measures

- Total Players
- Total Revenue
- Average Revenue

---

### vw_player_activity

Purpose

Summarises player betting behaviour.

---

### vw_transaction_summary

Purpose

Summarises deposits and withdrawals for financial analysis.

---

### vw_game_performance

Purpose

Summarises game-level betting performance.

Measures

- Total Bets
- Total Stake
- Total Payout
- Average Stake

---

### Testing

Each SQL view was executed and verified successfully within SQLite.

---

# Task 4 - Business SQL Queries

## Objective

Answer business questions using SQL rather than simple data retrieval.

A new SQL file named:

database/sql/business_queries.sql

was created to store reusable analytical SQL queries.

---

## Query 1

### Top 10 Players by Total Stake

Business Question

Which players contribute the highest betting volume?

Concepts Used

- JOIN
- GROUP BY
- SUM
- ORDER BY
- LIMIT

---

## Query 2

### Country-wise Betting Summary

Business Question

Which countries generate the highest betting activity?

Concepts Used

- JOIN
- COUNT
- SUM
- AVG
- GROUP BY

---

## Query 3

### Win vs Loss by Game

Business Question

Which games have the highest number of wins and losses?

Concepts Used

- GROUP BY
- COUNT
- ORDER BY

---

## Query 4

### Deposit vs Withdrawal by Country

Business Question

Which countries deposit more money than they withdraw?

Concepts Used

- CASE
- SUM
- JOIN
- GROUP BY

---

### Testing

All business SQL queries were executed successfully and validated against the sample database.

---

### Advanced SQL - Common Table Expression (CTE)

Created the first Common Table Expression (CTE) to calculate total revenue by country.

Purpose:
- Improve query readability.
- Break complex SQL into reusable logical steps.
- Prepare for larger analytical queries.

Concepts Learned:
- WITH clause
- Temporary result sets
- Query organization

---

## Advanced SQL - Window Functions

Implemented SQL window functions to rank players based on total revenue.

Concepts Learned:
- RANK()
- DENSE_RANK()
- ROW_NUMBER()
- OVER() clause

Business Use Case:
Ranked players by revenue contribution to identify the highest-value players.

---

## Advanced SQL - Subqueries

Implemented nested SQL queries to identify players generating revenue above the overall average player revenue.

Concepts Learned:
- Subqueries
- HAVING clause
- Aggregate comparisons
- Nested SELECT statements

Business Use Case:
Identified high-value players whose revenue exceeded the average revenue across all players.

---

## Advanced SQL - Query Optimization

Implemented basic SQL performance optimization techniques.

Activities Completed:
- Used `EXPLAIN QUERY PLAN` to inspect query execution.
- Created an index on `bets(player_id)`.
- Created an index on `transactions(player_id)`.

Concepts Learned:
- Query execution plans
- Table scans
- Indexes
- Performance optimization

Business Value:
Indexes improve query performance by reducing the amount of data scanned during joins and filtering, especially for large datasets.

---


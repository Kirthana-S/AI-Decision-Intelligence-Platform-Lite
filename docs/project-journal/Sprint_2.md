# Sprint 2

## Step 4 – System Architecture

### What I built

Created the first high-level architecture for the AI Decision Intelligence Platform.

### Why I built it

To define how data flows through the platform before implementing databases, SQL, Python, and machine learning.

### What I learned

- The purpose of software architecture
- How each technology fits into the overall solution
- Why planning the system first makes implementation easier

### Challenges

None

---

## Step 5 – Data Architecture

### What I built

Designed the initial relational data model for the platform.

### Why I built it

To define the core business entities and their relationships before creating the database.

### What I learned

- What data architecture is
- Why relational databases are used
- How entity relationships support analytics

### Challenges

None

---

## Step 6 – Database Schema Design

### What I built

Designed the database schema by defining tables, columns, data types, primary keys, and foreign keys.

### Why I built it

To create a structured relational database that supports SQL analysis, machine learning, and Power BI reporting.

### What I learned

- Primary Keys
- Foreign Keys
- Data Types
- One-to-Many Relationships
- Database Normalization

### Challenges

None

---

## Step 7 – Sample Data Generation

### What I built

Developed Python scripts to generate realistic sample datasets for Players, Transactions, and Bets using the Faker library and random data generation.

### Why I built it

Since production iGaming data is confidential and unavailable, synthetic data was required to simulate real business scenarios for analytics, SQL, and dashboard development.

### What I learned

- Using the Faker library to generate realistic sample data
- Creating CSV files using Pandas
- Writing datasets to the project directory
- Structuring raw datasets for analytics projects

### Challenges

Initially, the data generation script did not execute because of incorrect file paths and project structure. After organizing the folders correctly and running the script from the project root, the datasets were generated successfully.

---

## Step 8 – SQLite Database Creation

### What I built

Created a local SQLite database and loaded the Players, Transactions, and Bets datasets into separate database tables using Pandas.

### Why I built it

To build a relational database that can be queried using SQL before moving into business analysis and dashboard development.

### What I learned

- Connecting Python with SQLite
- Loading CSV files into database tables
- Using `pandas.to_sql()`
- Managing relational datasets

### Challenges

While loading the data, SQLite returned an error stating that the Players table already existed. The issue was resolved by deleting the existing database file and recreating it before loading the data again.

---

## Step 9 – Database Validation

### What I built

Created validation scripts to verify that all datasets were successfully loaded into the SQLite database.

### Why I built it

To ensure the generated datasets were correctly stored before performing SQL analysis and KPI calculations.

### What I learned

- Querying SQLite using Pandas
- Executing SQL COUNT queries
- Validating database contents
- Basic database testing

### Challenges

Initially, only the Players table existed because the previous database loading process had failed midway. After rebuilding the database successfully, all three tables were validated with the expected record counts.

---

## Step 10 – SQL Business Analysis

### What I built

Created SQL queries to analyze player distribution by country and exported the results into the processed data folder.

### Why I built it

To transform raw transactional data into business-ready datasets that can later be consumed by Power BI dashboards.

### What I learned

- SQL aggregation using `GROUP BY`
- Sorting results with `ORDER BY`
- Exporting SQL results using Pandas
- Difference between raw data and processed data

### Challenges

No major implementation issues were encountered after rebuilding the database successfully.

---

## Step 11 – KPI Summary Generation

### What I built

Developed a KPI analysis script that calculates key business metrics including total players, total bets, total deposits, total withdrawals, and average bet value.

### Why I built it

KPIs provide a high-level overview of platform performance and form the foundation for executive dashboards and business reporting.

### What I learned

- Executing multiple SQL queries from Python
- Creating KPI summary tables
- Exporting processed analytical datasets
- Building reusable analytics scripts

### Challenges

The initial SQL query referenced a non-existent column named `bet_amount`. After inspecting the database schema using `PRAGMA table_info`, the query was corrected to use the existing `stake` column, allowing the KPI calculations to execute successfully.

---

## Sprint 2 Summary

### Overall Progress

Successfully established the backend foundation for the AI Decision Intelligence Platform by generating synthetic data, creating a relational database, validating the data, performing SQL analysis, and producing business KPIs.

### Deliverables

- System Architecture
- Data Architecture
- Database Schema
- Sample Data Generation
- SQLite Database
- Database Validation
- SQL Business Analysis
- Processed Data Layer
- KPI Summary Dataset

### Skills Practiced

- Python
- Pandas
- Faker
- SQLite
- SQL
- Data Validation
- Data Engineering Fundamentals
- Business KPI Development

### Next Sprint

- Prepare dashboard-ready datasets
- Build the Power BI data model
- Develop executive KPI dashboard
- Create player analytics dashboard
- Create country performance dashboard
- Begin predictive analytics module
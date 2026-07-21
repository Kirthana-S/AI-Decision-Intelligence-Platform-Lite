# Sprint 3 – Power BI Dashboard Development

## Sprint Goal

Build an interactive executive dashboard in Power BI using the datasets generated in previous sprints and organize the report into business-focused analytics pages.

---

# Objectives

- Import generated CSV datasets into Power BI
- Create reusable DAX measures
- Design executive KPI cards
- Build multiple analytics pages
- Apply consistent report formatting
- Add interactive slicers
- Prepare a recruiter-ready Power BI report

---

# Datasets Used

## KPI Summary

Contains overall business metrics.

Columns:

- Metric
- Value

---

## Players by Country

Contains player counts grouped by country.

Columns:

- Country
- Total Players

---

## Player Details

Generated using Python.

Contains:

- PlayerID
- Age
- Gender
- Country
- Registration Date
- VIP Level
- Deposit
- Withdrawal
- Revenue
- Total Bets

---

# Power BI Pages Created

## 1. Executive Dashboard

Purpose:

Provide an executive-level overview of platform performance.

Visuals:

- Average Bet KPI
- Total Players KPI
- Total Bets KPI
- Total Withdrawals KPI
- Total Deposits KPI
- Players by Country chart
- Country slicer

---

## 2. Player Analytics

Purpose:

Analyze player demographics and acquisition.

Visuals:

- Players by Age Group
- Players by Gender
- Players by VIP Level
- Players by Country
- Monthly Player Registrations
- Gender slicer
- VIP Level slicer

---

## 3. Financial Analytics

Purpose:

Understand platform financial performance.

Visuals:

- Average Deposit
- Average Withdrawal
- Total Deposits
- Total Withdrawals
- Revenue by Country
- Deposit vs Withdrawal by VIP Level
- Deposit by VIP Level
- Revenue by VIP Level
- Country slicer
- VIP Level slicer

---

## 4. Gaming Analytics

Purpose:

Analyze betting behaviour.

Visuals:

- Average Bet
- Total Bets
- Average Revenue
- Total Revenue
- Top Players by Revenue
- Revenue vs Total Bets (Scatter)
- Average Bet by VIP Level
- Bets by Country
- Country slicer
- VIP Level slicer

---

## 5. Country Analytics

Purpose:

Analyze geographic platform performance.

Visuals:

- Total Countries
- Total Players
- Total Revenue
- Average Revenue
- Map Visualization
- Revenue by Country
- Players by Country
- Deposits by Country
- VIP Level slicer

---

# DAX Measures Created

Examples:

Average Bet

```DAX
Average Bet =
CALCULATE(
    SUM(kpi_summary[Value]),
    kpi_summary[Metric] = "average_bet"
)
```

Similar measures were created for:

- Total Players
- Total Bets
- Total Deposits
- Total Withdrawals

Additional measures:

- Average Deposit
- Average Withdrawal
- Average Revenue
- Total Revenue
- Total Countries

---

# Dashboard Design Principles

The report follows a consistent layout across all pages.

Top section

- KPI Cards

Middle section

- Main analytical visuals

Bottom section

- Supporting visuals

Right panel

- Interactive slicers

Design choices:

- Minimal colour palette
- Consistent spacing
- Executive dashboard style
- Clean typography
- White-space focused layout

---

# Challenges Faced

## Git migration from macOS to Windows

The project was developed using:

- macOS
- Windows

GitHub was used as the central repository to synchronize both environments.

---

## Python Environment

Initially Python 3.10 caused dependency issues.

Resolved by:

- Installing Python 3.13
- Creating a fresh virtual environment
- Reinstalling project dependencies

---

## Missing data folders

Python script failed because:

```
data/raw/
```

did not exist.

Solution:

Created required folders before executing the data generation script.

---

## Power BI Date Formatting

Registration dates initially appeared as individual dates.

Resolved by:

- Converting to Date datatype
- Using Month hierarchy
- Building monthly registration visuals

---

## Shape Map Issues

Power BI Shape Map produced incorrect geographic rendering.

Alternative approach:

Used the standard Map visual for reliable country visualization.

---

# Skills Demonstrated

Python

- Data generation

SQL

- Data preparation

Power BI

- Data modelling
- DAX
- KPI Cards
- Interactive filters
- Dashboard design

Git

- Branch management
- Cross-device synchronization
- GitHub version control

Business Analytics

- Executive reporting
- Financial analysis
- Player analytics
- Geographic analysis

---

# Sprint Outcome

Sprint 3 successfully transformed raw gaming datasets into a fully interactive Power BI reporting solution.

The report now contains five analytics pages designed for executives and business stakeholders.

The project demonstrates practical skills across Python, SQL, Power BI, DAX, Git, and business intelligence dashboard development.

---

# Next Sprint

Sprint 4

Database Enhancement & Advanced SQL Analytics

Goals:

- Expand SQLite schema
- Create analytical SQL queries
- Build reusable SQL views
- Connect SQL directly to Power BI
- Replace CSV-based reporting with database-driven reporting
# Sprint 3 – Power BI Dashboard Development

## Sprint Goal

Build an interactive executive dashboard in Power BI using the datasets generated in previous sprints and organize the report into business-focused analytics pages.

---

# Objectives

- Import generated CSV datasets into Power BI
- Create reusable DAX measures
- Design executive KPI cards
- Build multiple analytics pages
- Apply consistent report formatting
- Add interactive slicers
- Prepare a recruiter-ready Power BI report

---

# Datasets Used

## KPI Summary

Contains overall business metrics.

Columns:

- Metric
- Value

---

## Players by Country

Contains player counts grouped by country.

Columns:

- Country
- Total Players

---

## Player Details

Generated using Python.

Contains:

- PlayerID
- Age
- Gender
- Country
- Registration Date
- VIP Level
- Deposit
- Withdrawal
- Revenue
- Total Bets

---

# Power BI Pages Created

## 1. Executive Dashboard

Purpose:

Provide an executive-level overview of platform performance.

Visuals:

- Average Bet KPI
- Total Players KPI
- Total Bets KPI
- Total Withdrawals KPI
- Total Deposits KPI
- Players by Country chart
- Country slicer

---

## 2. Player Analytics

Purpose:

Analyze player demographics and acquisition.

Visuals:

- Players by Age Group
- Players by Gender
- Players by VIP Level
- Players by Country
- Monthly Player Registrations
- Gender slicer
- VIP Level slicer

---

## 3. Financial Analytics

Purpose:

Understand platform financial performance.

Visuals:

- Average Deposit
- Average Withdrawal
- Total Deposits
- Total Withdrawals
- Revenue by Country
- Deposit vs Withdrawal by VIP Level
- Deposit by VIP Level
- Revenue by VIP Level
- Country slicer
- VIP Level slicer

---

## 4. Gaming Analytics

Purpose:

Analyze betting behaviour.

Visuals:

- Average Bet
- Total Bets
- Average Revenue
- Total Revenue
- Top Players by Revenue
- Revenue vs Total Bets (Scatter)
- Average Bet by VIP Level
- Bets by Country
- Country slicer
- VIP Level slicer

---

## 5. Country Analytics

Purpose:

Analyze geographic platform performance.

Visuals:

- Total Countries
- Total Players
- Total Revenue
- Average Revenue
- Map Visualization
- Revenue by Country
- Players by Country
- Deposits by Country
- VIP Level slicer

---

# DAX Measures Created

Examples:

Average Bet

```DAX
Average Bet =
CALCULATE(
    SUM(kpi_summary[Value]),
    kpi_summary[Metric] = "average_bet"
)
```

Similar measures were created for:

- Total Players
- Total Bets
- Total Deposits
- Total Withdrawals

Additional measures:

- Average Deposit
- Average Withdrawal
- Average Revenue
- Total Revenue
- Total Countries

---

# Dashboard Design Principles

The report follows a consistent layout across all pages.

Top section

- KPI Cards

Middle section

- Main analytical visuals

Bottom section

- Supporting visuals

Right panel

- Interactive slicers

Design choices:

- Minimal colour palette
- Consistent spacing
- Executive dashboard style
- Clean typography
- White-space focused layout

---

# Challenges Faced

## Git migration from macOS to Windows

The project was developed using:

- macOS
- Windows

GitHub was used as the central repository to synchronize both environments.

---

## Python Environment

Initially Python 3.10 caused dependency issues.

Resolved by:

- Installing Python 3.13
- Creating a fresh virtual environment
- Reinstalling project dependencies

---

## Missing data folders

Python script failed because:

```
data/raw/
```

did not exist.

Solution:

Created required folders before executing the data generation script.

---

## Power BI Date Formatting

Registration dates initially appeared as individual dates.

Resolved by:

- Converting to Date datatype
- Using Month hierarchy
- Building monthly registration visuals

---

## Shape Map Issues

Power BI Shape Map produced incorrect geographic rendering.

Alternative approach:

Used the standard Map visual for reliable country visualization.

---

# Skills Demonstrated

Python

- Data generation

SQL

- Data preparation

Power BI

- Data modelling
- DAX
- KPI Cards
- Interactive filters
- Dashboard design

Git

- Branch management
- Cross-device synchronization
- GitHub version control

Business Analytics

- Executive reporting
- Financial analysis
- Player analytics
- Geographic analysis

---

# Sprint Outcome

Sprint 3 successfully transformed raw gaming datasets into a fully interactive Power BI reporting solution.

The report now contains five analytics pages designed for executives and business stakeholders.

The project demonstrates practical skills across Python, SQL, Power BI, DAX, Git, and business intelligence dashboard development.

---

# Next Sprint

Sprint 4

Database Enhancement & Advanced SQL Analytics

Goals:

- Expand SQLite schema
- Create analytical SQL queries
- Build reusable SQL views
- Connect SQL directly to Power BI
- Replace CSV-based reporting with database-driven reporting
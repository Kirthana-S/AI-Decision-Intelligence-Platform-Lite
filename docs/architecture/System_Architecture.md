# System Architecture

## Overview

The AI Decision Intelligence Platform is designed as a modular analytics solution for an iGaming company. The platform collects player data, processes it, stores it in a structured database, analyzes business trends, predicts future outcomes, and presents insights through interactive dashboards.

---

## High-Level Architecture

Player Activity
(Deposits, Bets, Games, Sessions)
                │
                ▼
         Raw Data Files (CSV)
                │
                ▼
      Python Data Processing
     (Cleaning & Transformation)
                │
                ▼
        SQLite Database
                │
        ┌───────┴────────┐
        ▼                ▼
    SQL Analytics   Machine Learning
        │                │
        └───────┬────────┘
                ▼
        Power BI Dashboard
                │
                ▼
     Business Decision Making

---

## Components

### 1. Raw Data

Contains exported player information such as:

- Player details
- Deposits
- Withdrawals
- Game sessions
- Bets
- Revenue

---

### 2. Python Processing

Python will:

- Clean missing values
- Transform data
- Create calculated features
- Prepare datasets for analysis

---

### 3. SQLite Database

Stores structured and cleaned data.

The database will support:

- SQL queries
- Reporting
- Dashboard integration

---

### 4. SQL Analytics

SQL will answer business questions such as:

- Daily Revenue
- Active Players
- Retention Rate
- VIP Performance
- Country Analysis

---

### 5. Machine Learning

Machine Learning models will:

- Predict player churn
- Detect suspicious player behaviour

---

### 6. Power BI Dashboard

Power BI will present:

- Executive KPIs
- Marketing Insights
- Player Analytics
- Risk Monitoring

---

## Data Flow

Raw Data

↓

Python ETL

↓

SQLite Database

↓

SQL Analysis

↓

Machine Learning

↓

Power BI Dashboard

↓

Business Users

---

## Future Enhancements

The architecture has been designed so additional modules can be added later, including:

- Responsible Gambling Analytics
- AI Business Assistant
- Streamlit Web Application
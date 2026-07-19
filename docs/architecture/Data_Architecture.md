# Data Architecture

## Overview

The AI Decision Intelligence Platform stores business data in a relational database.

The first version of the platform includes six core entities that represent the most important activities within an iGaming business.

---

## Core Entities

### Players

Stores player information.

Examples:

- Player ID
- Name
- Country
- Registration Date

---

### Games

Stores game information.

Examples:

- Game ID
- Game Name
- Category

---

### Sessions

Tracks player login sessions.

Examples:

- Session ID
- Player ID
- Login Time
- Logout Time
- Device

---

### Deposits

Stores player deposits.

Examples:

- Deposit ID
- Player ID
- Deposit Amount
- Deposit Date

---

### Bets

Stores betting activity.

Examples:

- Bet ID
- Player ID
- Game ID
- Bet Amount
- Win Amount
- Bet Time

---

### Withdrawals

Stores player withdrawals.

Examples:

- Withdrawal ID
- Player ID
- Withdrawal Amount
- Withdrawal Date

---

## Entity Relationships

- One Player can have many Sessions.
- One Player can make many Deposits.
- One Player can place many Bets.
- One Player can request many Withdrawals.
- One Game can have many Bets.

---

## Why a Relational Database?

A relational database allows us to:

- Reduce duplicate data
- Maintain data consistency
- Perform efficient SQL analysis
- Support dashboard reporting
- Prepare data for machine learning
# Database Schema

## Players

| Column | Data Type | Key |
|---------|-----------|-----|
| PlayerID | INTEGER | Primary Key |
| FirstName | TEXT | |
| LastName | TEXT | |
| Country | TEXT | |
| RegistrationDate | DATE | |

---

## Games

| Column | Data Type | Key |
|---------|-----------|-----|
| GameID | INTEGER | Primary Key |
| GameName | TEXT | |
| Category | TEXT | |

---

## Sessions

| Column | Data Type | Key |
|---------|-----------|-----|
| SessionID | INTEGER | Primary Key |
| PlayerID | INTEGER | Foreign Key |
| LoginTime | DATETIME | |
| LogoutTime | DATETIME | |
| Device | TEXT | |

---

## Deposits

| Column | Data Type | Key |
|---------|-----------|-----|
| DepositID | INTEGER | Primary Key |
| PlayerID | INTEGER | Foreign Key |
| DepositAmount | REAL | |
| DepositDate | DATE | |

---

## Bets

| Column | Data Type | Key |
|---------|-----------|-----|
| BetID | INTEGER | Primary Key |
| PlayerID | INTEGER | Foreign Key |
| GameID | INTEGER | Foreign Key |
| BetAmount | REAL | |
| WinAmount | REAL | |
| BetTime | DATETIME | |

---

## Withdrawals

| Column | Data Type | Key |
|---------|-----------|-----|
| WithdrawalID | INTEGER | Primary Key |
| PlayerID | INTEGER | Foreign Key |
| WithdrawalAmount | REAL | |
| WithdrawalDate | DATE | |
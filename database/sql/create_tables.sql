-- ==========================================
-- AI Decision Intelligence Platform
-- Database Schema
-- Sprint 3 - Create Tables
-- ==========================================

CREATE TABLE Players (
    PlayerID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Country TEXT NOT NULL,
    RegistrationDate DATE NOT NULL
);

CREATE TABLE Games (
    GameID INTEGER PRIMARY KEY,
    GameName TEXT NOT NULL,
    Category TEXT NOT NULL
);

CREATE TABLE Sessions (
    SessionID INTEGER PRIMARY KEY,
    PlayerID INTEGER NOT NULL,
    LoginTime DATETIME NOT NULL,
    LogoutTime DATETIME NOT NULL,
    Device TEXT NOT NULL,
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID)
);

CREATE TABLE Deposits (
    DepositID INTEGER PRIMARY KEY,
    PlayerID INTEGER NOT NULL,
    DepositAmount REAL NOT NULL,
    DepositDate DATE NOT NULL,
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID)
);

CREATE TABLE Withdrawals (
    WithdrawalID INTEGER PRIMARY KEY,
    PlayerID INTEGER NOT NULL,
    WithdrawalAmount REAL NOT NULL,
    WithdrawalDate DATE NOT NULL,
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID)
);

CREATE TABLE Bets (
    BetID INTEGER PRIMARY KEY,
    PlayerID INTEGER NOT NULL,
    GameID INTEGER NOT NULL,
    BetAmount REAL NOT NULL,
    WinAmount REAL NOT NULL,
    BetTime DATETIME NOT NULL,
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
    FOREIGN KEY (GameID) REFERENCES Games(GameID)
);
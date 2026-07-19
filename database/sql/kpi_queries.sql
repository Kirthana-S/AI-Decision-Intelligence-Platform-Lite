-- Total Players
SELECT COUNT(*) AS Total_Players
FROM players;

-- Total Bets
SELECT COUNT(*) AS Total_Bets
FROM bets;

-- Total Transactions
SELECT COUNT(*) AS Total_Transactions
FROM transactions;

-- Players by Country
SELECT
    country,
    COUNT(*) AS Players
FROM players
GROUP BY country
ORDER BY Players DESC;

-- Players by Country
SELECT
    country,
    COUNT(*) AS total_players
FROM players
GROUP BY country
ORDER BY total_players DESC
LIMIT 10;


-- ==========================================
-- Executive KPI Queries
-- ==========================================

-- Total Players
SELECT COUNT(*) AS total_players
FROM players;

-- Total Bets
SELECT COUNT(*) AS total_bets
FROM bets;

-- Total Deposit Amount
SELECT SUM(amount) AS total_deposits
FROM transactions
WHERE transaction_type='Deposit';

-- Total Withdrawal Amount
SELECT SUM(amount) AS total_withdrawals
FROM transactions
WHERE transaction_type='Withdrawal';

-- Average Bet Amount
SELECT AVG(bet_amount) AS average_bet
FROM bets;
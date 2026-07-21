# Query 1: Top 10 Players by Total Stake

SELECT
    p.player_id,
    p.name,
    p.country,
    SUM(b.stake) AS TotalStake
FROM players p
JOIN bets b
ON p.player_id = b.player_id
GROUP BY
    p.player_id,
    p.name,
    p.country
ORDER BY TotalStake DESC
LIMIT 10;

# Query 2: Country-wise Betting Summary
SELECT
    p.country,
    COUNT(b.bet_id) AS TotalBets,
    SUM(b.stake) AS TotalStake,
    AVG(b.stake) AS AverageStake
FROM players p
JOIN bets b
ON p.player_id = b.player_id
GROUP BY p.country
ORDER BY TotalStake DESC;

# Query 3: Win vs Loss by Game
SELECT
    game,
    result,
    COUNT(*) AS TotalBets
FROM bets
GROUP BY
    game,
    result
ORDER BY
    game,
    result;

#Query 4: Deposit vs Withdrawal by Country
SELECT
    p.country,
    SUM(CASE
            WHEN t.transaction_type='Deposit'
            THEN t.amount
            ELSE 0
        END) AS Deposits,
    SUM(CASE
            WHEN t.transaction_type='Withdrawal'
            THEN t.amount
            ELSE 0
        END) AS Withdrawals
FROM players p
JOIN transactions t
ON p.player_id=t.player_id
GROUP BY p.country;
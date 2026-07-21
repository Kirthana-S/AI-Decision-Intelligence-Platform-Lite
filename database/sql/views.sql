CREATE VIEW IF NOT EXISTS vw_country_betting AS
SELECT
    p.country,
    COUNT(b.bet_id) AS TotalBets,
    SUM(b.stake) AS TotalStake,
    SUM(b.payout) AS TotalPayout,
    AVG(b.stake) AS AverageStake
FROM players p
JOIN bets b
ON p.player_id = b.player_id
GROUP BY p.country;


CREATE VIEW IF NOT EXISTS vw_player_activity AS
SELECT
    p.player_id,
    p.name,
    p.country,
    COUNT(b.bet_id) AS TotalBets,
    SUM(b.stake) AS TotalStake,
    SUM(b.payout) AS TotalPayout
FROM players p
LEFT JOIN bets b
ON p.player_id = b.player_id
GROUP BY
    p.player_id,
    p.name,
    p.country;

CREATE VIEW IF NOT EXISTS vw_transaction_summary AS
SELECT
    p.country,
    COUNT(t.transaction_id) AS TotalTransactions,
    SUM(CASE
            WHEN t.transaction_type='Deposit'
            THEN t.amount
            ELSE 0
        END) AS TotalDeposits,
    SUM(CASE
            WHEN t.transaction_type='Withdrawal'
            THEN t.amount
            ELSE 0
        END) AS TotalWithdrawals
FROM players p
JOIN transactions t
ON p.player_id=t.player_id
GROUP BY p.country;  



CREATE VIEW IF NOT EXISTS vw_game_performance AS
SELECT
    game,
    COUNT(*) AS TotalBets,
    SUM(stake) AS TotalStake,
    SUM(payout) AS TotalPayout,
    AVG(stake) AS AverageStake
FROM bets
GROUP BY game;
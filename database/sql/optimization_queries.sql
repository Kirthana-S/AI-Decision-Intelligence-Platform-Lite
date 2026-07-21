EXPLAIN QUERY PLAN
SELECT
    p.player_id,
    p.name,
    SUM(b.stake) AS TotalStake
FROM players p
JOIN bets b
ON p.player_id = b.player_id
GROUP BY
    p.player_id,
    p.name;
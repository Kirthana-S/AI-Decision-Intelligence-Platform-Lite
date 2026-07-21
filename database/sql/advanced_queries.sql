#-- CTE 1: Top 5 Countries by Revenue

WITH CountryRevenue AS
(
    SELECT
        p.country,
        SUM(b.payout) AS TotalRevenue
    FROM players p
    JOIN bets b
        ON p.player_id = b.player_id
    GROUP BY p.country
)

SELECT *
FROM CountryRevenue
ORDER BY TotalRevenue DESC
LIMIT 5;

-- Window Function: Rank Players by Revenue

SELECT
    player_id,
    SUM(payout) AS TotalRevenue,
    RANK() OVER (
        ORDER BY SUM(payout) DESC
    ) AS RevenueRank
FROM bets
GROUP BY player_id;

-- Subquery: Players Above Average Revenue

SELECT
    player_id,
    SUM(payout) AS TotalRevenue
FROM bets
GROUP BY player_id
HAVING SUM(payout) >
(
    SELECT
        AVG(PlayerRevenue)
    FROM
    (
        SELECT
            SUM(payout) AS PlayerRevenue
        FROM bets
        GROUP BY player_id
    )
);
import sqlite3
import pandas as pd

conn = sqlite3.connect("database/igaming_platform.db")

queries = {
    "total_players":
        "SELECT COUNT(*) AS value FROM players",

    "total_bets":
        "SELECT COUNT(*) AS value FROM bets",

    "total_deposits":
        """
        SELECT SUM(amount) AS value
        FROM transactions
        WHERE transaction_type='Deposit'
        """,

    "total_withdrawals":
        """
        SELECT SUM(amount) AS value
        FROM transactions
        WHERE transaction_type='Withdrawal'
        """,

    "average_bet":
        "SELECT AVG(stake) AS value FROM bets"
}

results = []

for metric, query in queries.items():
    value = pd.read_sql(query, conn).iloc[0,0]
    results.append({
        "Metric": metric,
        "Value": value
    })

kpi_df = pd.DataFrame(results)

print(kpi_df)

kpi_df.to_csv(
    "data/processed/kpi_summary.csv",
    index=False
)

conn.close()

print("KPI Summary Created!")

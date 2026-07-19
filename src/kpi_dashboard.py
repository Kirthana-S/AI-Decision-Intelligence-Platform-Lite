import sqlite3
import pandas as pd

conn = sqlite3.connect("database/igaming_platform.db")

queries = {
    "Total Players":
        "SELECT COUNT(*) FROM players",

    "Total Bets":
        "SELECT COUNT(*) FROM bets",

    "Total Transactions":
        "SELECT COUNT(*) FROM transactions"
}

print("\n===== EXECUTIVE KPI DASHBOARD =====\n")

for title, sql in queries.items():
    value = pd.read_sql(sql, conn).iloc[0, 0]
    print(f"{title}: {value}")

conn.close()
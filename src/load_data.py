import sqlite3
import pandas as pd

conn = sqlite3.connect("database/igaming_platform.db")

players = pd.read_csv("data/raw/players.csv")
transactions = pd.read_csv("data/raw/transactions.csv")
bets = pd.read_csv("data/raw/bets.csv")

players.to_sql("players", conn, if_exists="replace", index=False)
transactions.to_sql("transactions", conn, if_exists="replace", index=False)
bets.to_sql("bets", conn, if_exists="replace", index=False)

conn.close()

print("Database loaded successfully!")
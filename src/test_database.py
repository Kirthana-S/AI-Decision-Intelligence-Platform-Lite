import sqlite3
import pandas as pd

conn = sqlite3.connect("database/igaming_platform.db")

print(pd.read_sql("SELECT COUNT(*) AS players FROM players", conn))

print(pd.read_sql("SELECT COUNT(*) AS transactions FROM transactions", conn))

print(pd.read_sql("SELECT COUNT(*) AS bets FROM bets", conn))

conn.close()
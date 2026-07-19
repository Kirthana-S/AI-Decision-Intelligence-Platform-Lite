import sqlite3
import pandas as pd

conn = sqlite3.connect("database/igaming_platform.db")

query = """
SELECT COUNT(*) AS Total_Players
FROM players;
"""

result = pd.read_sql(query, conn)

print(result)

conn.close()
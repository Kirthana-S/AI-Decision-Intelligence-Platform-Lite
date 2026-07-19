import sqlite3
import pandas as pd

conn = sqlite3.connect("database/igaming_platform.db")

query = """
SELECT
    country,
    COUNT(*) AS total_players
FROM players
GROUP BY country
ORDER BY total_players DESC
LIMIT 10;
"""

result = pd.read_sql(query, conn)

# Save the result into processed folder
result.to_csv(
    "data/processed/players_by_country.csv",
    index=False
)

print(result)
print("Analysis saved successfully!")

conn.close()
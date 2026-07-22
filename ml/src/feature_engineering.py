import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("database/igaming_platform.db")

players = pd.read_sql("SELECT * FROM players", conn)
bets = pd.read_sql("SELECT * FROM bets", conn)
transactions = pd.read_sql("SELECT * FROM transactions", conn)

#print(players.head())
#print(bets.head())
#print(transactions.head())

bets["bet_date"] = pd.to_datetime(bets["bet_date"])

# Create win flag
bets["Win"] = bets["result"].apply(lambda x: 1 if x == "Win" else 0)

#active days
active_days = (
    bets.groupby("player_id")
    .agg(
        Active_Days=("bet_date", "nunique")
    )
    .reset_index()
)

# Player betting statistics
bet_features = (
    bets.groupby("player_id")
    .agg(
        Total_Bets=("bet_id", "count"),
        Total_Stake=("stake", "sum"),
        Average_Bet=("stake", "mean"),
        Total_Payout=("payout", "sum"),
        Win_Rate=("Win", "mean")
    )
    .reset_index()
)

# Deposits and Withdrawals
transaction_features = (
    transactions.pivot_table(
        index="player_id",
        columns="transaction_type",
        values="amount",
        aggfunc="sum",
        fill_value=0
    )
    .reset_index()
)

# Merge datasets
ml_dataset = players.merge(
    bet_features,
    on="player_id",
    how="left"
)

ml_dataset = ml_dataset.merge(
    transaction_features,
    on="player_id",
    how="left"
)

ml_dataset = ml_dataset.merge(
    active_days,
    on="player_id",
    how="left"
)

#Net Revenue
ml_dataset["Net_Revenue"] = (
    ml_dataset["Total_Payout"] - ml_dataset["Total_Stake"]
)

ml_dataset.fillna(0, inplace=True)
print(ml_dataset.head())

#save dataset
ml_dataset.to_csv(
    "ml/data/ml_dataset.csv",
    index=False
)

print("ML dataset created successfully!")

conn.close()

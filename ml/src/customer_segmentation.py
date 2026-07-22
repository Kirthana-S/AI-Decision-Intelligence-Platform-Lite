import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("ml/data/ml_dataset.csv")
features = [
    "Total_Bets",
    "Total_Stake",
    "Average_Bet",
    "Total_Payout",
    "Deposit",
    "Withdrawal",
    "Win_Rate",
    "Net_Revenue",
    "Active_Days"
]

scaler = StandardScaler()

X = scaler.fit_transform(df[features])

kmeans = KMeans(
    n_clusters=4,
    random_state=42
)

df["Cluster"] = kmeans.fit_predict(X)

cluster_summary = (
    df.groupby("Cluster")
    .agg(
        Players=("player_id", "count"),
        Avg_Stake=("Total_Stake", "mean"),
        Avg_Deposit=("Deposit", "mean"),
        Avg_Bets=("Total_Bets", "mean"),
        Avg_WinRate=("Win_Rate", "mean")
    )
)

print(cluster_summary)

cluster_names = {
    0: "Casual Players",
    1: "VIP Players",
    2: "Regular Players",
    3: "Dormant Players"
}

df["Segment"] = df["Cluster"].map(cluster_names)

print(df[["player_id", "Cluster"]].head(20))

df.to_csv(
    "ml/outputs/player_segments.csv",
    index=False
)

print("Customer segmentation completed!")


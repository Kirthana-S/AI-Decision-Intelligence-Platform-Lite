import pandas as pd

# Load prediction files
segments = pd.read_csv("ml/outputs/player_segments.csv")
vip = pd.read_csv("ml/outputs/vip_predictions.csv")
churn = pd.read_csv("ml/outputs/churn_predictions.csv")

# Keep only required columns
segments = segments[
    ["player_id", "Cluster", "Segment"]
]

vip = vip[
    ["player_id", "Predicted_VIP", "VIP_Probability"]
]

churn = churn[
    ["player_id", "Predicted_Churn", "Churn_Probability"]
]

# Merge everything
ai_predictions = (
    segments
    .merge(vip, on="player_id")
    .merge(churn, on="player_id")
)

# Save
ai_predictions.to_csv(
    "ml/outputs/ai_predictions.csv",
    index=False
)

print("AI predictions combined successfully!")
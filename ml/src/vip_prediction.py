import pandas as pd

# Load dataset
df = pd.read_csv("ml/data/ml_dataset.csv")

# Create VIP label
df["VIP"] = (
    (df["Total_Stake"] >= 3000) &
    (df["Deposit"] >= 5000)
).astype(int)

print(df[["player_id", "Total_Stake", "Deposit", "VIP"]].head())

print(df["VIP"].value_counts())

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

X = df[features]
y = df["VIP"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

probabilities = model.predict_proba(X_test)
vip_probability = probabilities[:, 1]

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy:.2%}")

results = df.loc[X_test.index, ["player_id", "name", "country"]].copy()

results = results.join(X_test)

results["Actual_VIP"] = y_test.values
results["Predicted_VIP"] = predictions
results["VIP_Probability"] = vip_probability


results.to_csv(
    "ml/outputs/vip_predictions.csv",
    index=False
)

print("VIP predictions exported successfully!")

importance.to_csv(
    "ml/outputs/vip_feature_importance.csv",
    index=False
)

import joblib

joblib.dump(model, "ml/models/vip_model.pkl")


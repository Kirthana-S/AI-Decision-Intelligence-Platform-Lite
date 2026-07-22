import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

df = pd.read_csv("ml/data/ml_dataset.csv")

df["Churn"] = (
    (df["Active_Days"] <= 42) &
    (df["Total_Bets"] <= 42)
).astype(int)

print(df["Churn"].value_counts())

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
y = df["Churn"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

probabilities = model.predict_proba(X_test)

churn_probability = probabilities[:,1]

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Accuracy: {accuracy:.2%}")

print(confusion_matrix(
    y_test,
    predictions
))

print(classification_report(
    y_test,
    predictions
))

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance)

results = df.loc[X_test.index, ["player_id", "name", "country"]].copy()

results = results.join(X_test)

results["Actual_Churn"] = y_test.values

results["Predicted_Churn"] = predictions

results["Churn_Probability"] = churn_probability

results.to_csv(
    "ml/outputs/churn_predictions.csv",
    index=False
)

importance.to_csv(
    "ml/outputs/churn_feature_importance.csv",
    index=False
)

joblib.dump(
    model,
    "ml/models/churn_model.pkl"
)

print("Churn prediction completed!")

from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

countries = [
    "Malta",
    "UK",
    "Germany",
    "Italy",
    "Spain",
    "Sweden",
    "India",
    "Canada",
    "Brazil",
    "Australia"
]

vip_levels = ["Bronze", "Silver", "Gold", "Platinum"]

players = []

for i in range(1,1001):

    deposit = random.randint(100,5000)
    withdrawal = random.randint(50,deposit)
    bets = random.randint(20,800)

    players.append({

        "PlayerID": i,
        "Country": random.choice(countries),
        "Age": random.randint(18,60),
        "Gender": random.choice(["Male","Female"]),
        "VIP_Level": random.choice(vip_levels),
        "Registration_Date": fake.date_between(
            start_date="-3y",
            end_date="today"
        ),
        "Deposit": deposit,
        "Withdrawal": withdrawal,
        "Total_Bets": bets,
        "Revenue": deposit-withdrawal

    })

df = pd.DataFrame(players)

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/player_details.csv",
    index=False
)

print(df.head())
print("\nDataset Created Successfully!")


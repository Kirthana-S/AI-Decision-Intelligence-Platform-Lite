import pandas as pd
import random
from faker import Faker

fake = Faker()

NUM_PLAYERS = 1000
NUM_TRANSACTIONS = 10000

# ------------------------
# Players
# ------------------------

players = []

for player_id in range(1, NUM_PLAYERS + 1):
    players.append({
        "player_id": player_id,
        "name": fake.name(),
        "country": fake.country(),
        "registration_date": fake.date_between(start_date="-3y", end_date="today"),
        "age": random.randint(18, 65)
    })

players_df = pd.DataFrame(players)
players_df.to_csv("data/raw/players.csv", index=False)

# ------------------------
# Transactions
# ------------------------

transactions = []

for transaction_id in range(1, NUM_TRANSACTIONS + 1):

    transactions.append({

        "transaction_id": transaction_id,

        "player_id": random.randint(1, NUM_PLAYERS),

        "transaction_type": random.choice([
            "Deposit",
            "Withdrawal"
        ]),

        "amount": round(random.uniform(10,1000),2),

        "transaction_date": fake.date_time_between(
            start_date="-1y",
            end_date="now"
        )

    })

transactions_df = pd.DataFrame(transactions)

transactions_df.to_csv(
    "data/raw/transactions.csv",
    index=False
)
# ------------------------
# Betting Activity
# ------------------------

NUM_BETS = 50000

games = [
    "Slots",
    "Blackjack",
    "Roulette",
    "Poker",
    "Sportsbook"
]

bet_results = [
    "Win",
    "Lose"
]

bets = []

for bet_id in range(1, NUM_BETS + 1):

    stake = round(random.uniform(1, 200), 2)

    result = random.choice(bet_results)

    if result == "Win":
        payout = round(stake * random.uniform(1.2, 5), 2)
    else:
        payout = 0

    bets.append({
        "bet_id": bet_id,
        "player_id": random.randint(1, NUM_PLAYERS),
        "game": random.choice(games),
        "stake": stake,
        "result": result,
        "payout": payout,
        "bet_date": fake.date_time_between(
            start_date="-1y",
            end_date="now"
        )
    })

bets_df = pd.DataFrame(bets)

bets_df.to_csv(
    "data/raw/bets.csv",
    index=False
)

print("Players:", len(players_df))
print("Transactions:", len(transactions_df))
print("Bets:", len(bets_df))
print("All datasets created successfully!")



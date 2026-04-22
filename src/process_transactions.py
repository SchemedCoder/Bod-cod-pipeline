import pandas as pd

txn = pd.read_csv("data/transactions.csv")

# Aggregate per account (ignoring date for simplicity)
txn_agg = txn.groupby("account_id", as_index=False)["amount"].sum()

txn_agg.columns = ["account_id", "daily_txn"]

txn_agg.to_csv("output/transactions_agg.csv", index=False)

print("Transactions processed")

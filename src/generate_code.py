import pandas as pd

bod = pd.read_csv("output/bod.csv")
txn = pd.read_csv("output/transactions_agg.csv")

df = pd.merge(bod, txn, on="account_id", how="left")
df["daily_txn"] = df["daily_txn"].fillna(0)

df["cod_balance"] = df["bod_balance"] + df["daily_txn"]

df.to_csv("output/cod.csv", index=False)

print("COD created")

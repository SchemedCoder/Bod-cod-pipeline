import pandas as pd
import os

# Check if COD exists
if os.path.exists("output/cod.csv"):
    cod = pd.read_csv("output/cod.csv")
    bod = cod[["account_id", "cod_balance"]]
    bod.columns = ["account_id", "bod_balance"]
else:
    initial = pd.read_csv("data/initial_balance.csv")
    bod = initial.rename(columns={"balance": "bod_balance"})

bod.to_csv("output/bod.csv", index=False)

print("BOD created")

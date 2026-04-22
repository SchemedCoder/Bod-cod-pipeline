BOD-COD Data Pipeline with ADF

I built a simple pipeline where BOD is derived from previous COD and transactions are applied to generate COD. I used ADF for orchestration logic.

What This Project Does
This project calculates:
- BOD (Beginning of Day balance)
- COD (Close of Day balance)

Logic:
- First run → BOD = Initial balance
- Next runs → BOD = Previous COD
- COD = BOD + daily transactions

---

 Simple Architecture

CSV Files → ADF Pipeline → Python Scripts → Output CSV

---

 Flow (Sequence)

1. Check if previous COD exists
2. If yes → use it as BOD
3. If no → use initial balance
4. Process transactions
5. Generate COD

---

How to Run

Step 1:
pip install -r requirements.txt

Step 2:
python src/bod_load.py  
python src/process_transactions.py  
python src/generate_cod.py  

---
output

I ran it locally and stored sample outputs / expected outputs in the repository to demonstrate the pipeline results and make the project easier to understand without running the code.

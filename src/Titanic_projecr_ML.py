import pandas as pd
import os
print("Working directory:", os.getcwd())

df = pd.read_csv("../data/Titanic-Dataset.csv")
print(df)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load a dataset
df = pd.read_csv("Tracker report.csv")

# 1. Summary
print(df.info())
# print(df.describe())

# 2. Missing values
#print(df.isnull().sum())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("churn.csv")

# Text analysis
print("Customer Churn Count:")
print(df["Churn"].value_counts())

print("\nChurn Percentage:")
print(df["Churn"].value_counts(normalize=True) * 100)

# 📊 ONE CHART
sns.countplot(x="Churn", data=df)

plt.title("Customer Churn (Yes vs No)")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.show()
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"data\HHS_Unaccompanied_Alien_Children_Program.csv")

df = df.dropna(subset=["Date", "Children in HHS Care"])

df["Children in HHS Care"] = (
    df["Children in HHS Care"]
    .astype(str)
    .str.replace(",", "")
    .astype(float)
)

df["Date"] = pd.to_datetime(df["Date"], format="%B %d, %Y")
df = df.sort_values("Date")

plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Children in HHS Care"])
plt.title("Children in HHS Care Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Children")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

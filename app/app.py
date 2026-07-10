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

df["Total System Load"] = (
    df["Children in CBP custody"] +
    df["Children in HHS Care"]
)
print(df[["Date", "Total System Load"]].head())
plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["Total System Load"])

plt.title("Total System Load Over Time")
plt.xlabel("Date")
plt.ylabel("Total Children Under Care")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df["Net Daily Intake"] = (
    df["Children transferred out of CBP custody"] -
    df["Children discharged from HHS Care"]
)

plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["Net Daily Intake"])
plt.title("Net Daily Intake Over Time")
plt.xlabel("Date")
plt.ylabel("Net Daily Intake")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df["Care Load Growth Rate"] = (
    df["Children in HHS Care"].pct_change() * 100
)

plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["Care Load Growth Rate"])
plt.title("Care Load Growth Rate")
plt.xlabel("Date")
plt.ylabel("Growth Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df["7-Day Rolling Average"] = (
    df["Children in HHS Care"]
    .rolling(window=7)
    .mean()
)

plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["7-Day Rolling Average"])
plt.title("7-Day Rolling Average")
plt.xlabel("Date")
plt.ylabel("Average Children")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df["14-Day Rolling Average"] = (
    df["Children in HHS Care"]
    .rolling(window=14)
    .mean()
)

plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["14-Day Rolling Average"])
plt.title("14-Day Rolling Average")
plt.xlabel("Date")
plt.ylabel("Average Children")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("========== KPI SUMMARY ==========")

print("Maximum HHS Care:", df["Children in HHS Care"].max())
print("Minimum HHS Care:", df["Children in HHS Care"].min())
print("Average HHS Care:", df["Children in HHS Care"].mean())

print("Maximum Total System Load:", df["Total System Load"].max())
print("Minimum Total System Load:", df["Total System Load"].min())

print("Average Net Daily Intake:", df["Net Daily Intake"].mean())

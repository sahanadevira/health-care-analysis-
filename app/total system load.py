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

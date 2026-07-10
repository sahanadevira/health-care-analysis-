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

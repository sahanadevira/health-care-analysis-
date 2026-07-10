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

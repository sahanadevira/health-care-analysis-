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

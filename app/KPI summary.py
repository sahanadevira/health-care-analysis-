print("========== KPI SUMMARY ==========")

print("Maximum HHS Care:", df["Children in HHS Care"].max())
print("Minimum HHS Care:", df["Children in HHS Care"].min())
print("Average HHS Care:", df["Children in HHS Care"].mean())

print("Maximum Total System Load:", df["Total System Load"].max())
print("Minimum Total System Load:", df["Total System Load"].min())

print("Average Net Daily Intake:", df["Net Daily Intake"].mean())

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(page_title="Care Load Analytics", layout="wide")

st.title("📊 System Capacity & Care Load Analytics for Unaccompanied Children")

# Find the project folder
BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "data" / "HHS_Unaccompanied_Alien_Children_Program.csv"

df = pd.read_csv(csv_path)

# Data Cleaning
df = df.dropna(subset=["Date", "Children in HHS Care"])

df["Date"] = pd.to_datetime(df["Date"])

numeric_cols = [
    "Children in CBP custody",
    "Children in HHS Care",
    "Children transferred out of CBP custody",
    "Children discharged from HHS Care"
]

for col in numeric_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna()

# Metrics
df["Total System Load"] = (
    df["Children in CBP custody"] +
    df["Children in HHS Care"]
)

df["Net Daily Intake"] = (
    df["Children transferred out of CBP custody"] -
    df["Children discharged from HHS Care"]
)

df["Care Load Growth Rate"] = (
    df["Children in HHS Care"].pct_change() * 100
)

df["7-Day Rolling Average"] = (
    df["Children in HHS Care"].rolling(7).mean()
)

df["14-Day Rolling Average"] = (
    df["Children in HHS Care"].rolling(14).mean()
)

# KPI Summary
st.header("📋 KPI Summary")

c1, c2, c3 = st.columns(3)

c1.metric("Maximum HHS Care", int(df["Children in HHS Care"].max()))
c2.metric("Maximum Total System Load", int(df["Total System Load"].max()))
c3.metric("Average Net Daily Intake", round(df["Net Daily Intake"].mean(), 2))

# Graph 1
st.subheader("Children in HHS Care Over Time")
fig, ax = plt.subplots(figsize=(12,5))
ax.plot(df["Date"], df["Children in HHS Care"])
ax.set_xlabel("Date")
ax.set_ylabel("Number of Children")
plt.xticks(rotation=45)
st.pyplot(fig)

# Graph 2
st.subheader("Total System Load Over Time")
fig, ax = plt.subplots(figsize=(12,5))
ax.plot(df["Date"], df["Total System Load"])
ax.set_xlabel("Date")
ax.set_ylabel("Total Children Under Care")
plt.xticks(rotation=45)
st.pyplot(fig)

# Graph 3
st.subheader("Net Daily Intake")
fig, ax = plt.subplots(figsize=(12,5))
ax.plot(df["Date"], df["Net Daily Intake"])
ax.set_xlabel("Date")
ax.set_ylabel("Net Daily Intake")
plt.xticks(rotation=45)
st.pyplot(fig)

# Graph 4
st.subheader("Care Load Growth Rate")
fig, ax = plt.subplots(figsize=(12,5))
ax.plot(df["Date"], df["Care Load Growth Rate"])
ax.set_xlabel("Date")
ax.set_ylabel("Growth Rate (%)")
plt.xticks(rotation=45)
st.pyplot(fig)

# Graph 5
st.subheader("7-Day Rolling Average")
fig, ax = plt.subplots(figsize=(12,5))
ax.plot(df["Date"], df["7-Day Rolling Average"])
ax.set_xlabel("Date")
ax.set_ylabel("Average Children")
plt.xticks(rotation=45)
st.pyplot(fig)

# Graph 6
st.subheader("14-Day Rolling Average")
fig, ax = plt.subplots(figsize=(12,5))
ax.plot(df["Date"], df["14-Day Rolling Average"])
ax.set_xlabel("Date")
ax.set_ylabel("Average Children")
plt.xticks(rotation=45)
st.pyplot(fig)

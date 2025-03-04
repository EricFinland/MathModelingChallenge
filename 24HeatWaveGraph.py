import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data from Given Spreadsheet
#https://docs.google.com/spreadsheets/d/118N_dH5Sc2MdxUvlKjng6OeuhmWRXXn-sNs5u8xneC4/edit?gid=0#gid=0
data = {
    "Time": ["12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM", "7 AM", "8 AM", "9 AM",
             "10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM",
             "8 PM", "9 PM", "10 PM", "11 PM"],
    "Temperature_F": [85, 85, 84, 83, 83, 83, 84, 88, 91, 94,
                      96, 97, 100, 100, 102, 102, 100, 99, 97, 94,
                      92, 91, 90, 89],
    "Humidity": [74, 74, 74, 77, 77, 77, 74, 67, 61, 56,
                 52, 51, 45, 43, 38, 38, 42, 43, 47, 51,
                 55, 59, 63, 65],
    "Wind Speed": [6, 5, 8, 5, 7, 8, 7, 9, 9, 10,
                   9, 5, 9, 8, 13, 16, 10, 10, 8, 6,
                   7, 8, 12, 12]
}


df = pd.DataFrame(data)

df["Time"] = pd.Categorical(df["Time"], categories=df["Time"], ordered=True)


sns.set_style("whitegrid")


fig, axes = plt.subplots(3, 1, figsize=(12, 12))

sns.lineplot(ax=axes[0], x=df["Time"], y=df["Temperature_F"], marker="o", color="red", linewidth=2)
axes[0].axhline(y=100, color='black', linestyle="dashed", label="Heat Wave Threshold (100°F)")
axes[0].set_title("24-Hour Temperature Changes During Memphis Heat Wave")
axes[0].set_xlabel("Time of Day")
axes[0].set_ylabel("Temperature (°F)")
axes[0].set_xticklabels(df["Time"], rotation=45)
axes[0].legend()
axes[0].grid(True)


sns.barplot(ax=axes[1], x=df["Time"], y=df["Humidity"], color="blue")
axes[1].set_title("Humidity Levels Over 24 Hours")
axes[1].set_xlabel("Time of Day")
axes[1].set_ylabel("Humidity (%)")
axes[1].set_xticklabels(df["Time"], rotation=45)
axes[1].grid(axis="y")

sns.lineplot(ax=axes[2], x=df["Time"], y=df["Wind Speed"], marker="s", color="green", linewidth=2)
axes[2].set_title("Wind Speed Variations During Heat Wave")
axes[2].set_xlabel("Time of Day")
axes[2].set_ylabel("Wind Speed (mph)")
axes[2].set_xticklabels(df["Time"], rotation=45)
axes[2].grid(True)


plt.tight_layout()
plt.show()

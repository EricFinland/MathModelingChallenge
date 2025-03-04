import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("whitegrid")


memphis_data = {
    "Year": [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012],
    "Consumption_kWh": [9768296000, 9800375000, 9672364000, 10208674000, 10604732000, 
                         10154668000, 10436626000, 10514853000, 10544122000, 10705452000, 10753992000]
}


monthly_data = {
    "Month": ["January", "February", "March", "April", "May", "June", "July", "August", 
              "September", "October", "November", "December"],
    "Consumption_kWh": [28750000000, 25300000000, 22950000000, 22150000000, 24820000000, 
                         27890000000, 31120000000, 31330000000, 27590000000, 24280000000, 
                         22800000000, 25350000000]
}


usage_comparison = {
    "Location": ["Memphis", "National"],
    "Average_Usage_kWh": [15172, 10791]
}


df_memphis = pd.DataFrame(memphis_data)
df_monthly = pd.DataFrame(monthly_data)
df_comparison = pd.DataFrame(usage_comparison)


fig, axes = plt.subplots(3, 1, figsize=(12, 14))


sns.lineplot(ax=axes[0], x=df_memphis["Year"], y=df_memphis["Consumption_kWh"], marker="o", color="blue", linewidth=2)
axes[0].set_title("Memphis Annual Electricity Consumption (2012-2022)")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Electricity Consumption (kWh)")
axes[0].invert_xaxis() 
axes[0].grid(True)


sns.barplot(ax=axes[1], x=df_monthly["Month"], y=df_monthly["Consumption_kWh"], color="green")
axes[1].set_title("Monthly Electricity Consumption (2024) - East South Central USA")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Electricity Consumption (kWh)")
axes[1].set_xticklabels(df_monthly["Month"], rotation=45)
axes[1].grid(axis="y")


sns.barplot(ax=axes[2], x=df_comparison["Location"], y=df_comparison["Average_Usage_kWh"], palette=["red", "gray"])
axes[2].set_title("Memphis vs. National Average Annual Electricity Usage")
axes[2].set_xlabel("Location")
axes[2].set_ylabel("Average Electricity Usage (kWh)")
axes[2].grid(axis="y")

plt.tight_layout()
plt.show()

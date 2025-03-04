import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data from Given SpreadSheet
#https://docs.google.com/spreadsheets/d/118N_dH5Sc2MdxUvlKjng6OeuhmWRXXn-sNs5u8xneC4/edit?gid=0#gid=0
data = {
    "Year": [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 
             2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 
             2003, 2002, 2001, 2000],
    "Temperature_F": [102, 102, 96, 97, 100, 97, 99, 100, 99, 100, 
                      98, 103, 106, 104, 100, 101, 106, 102, 100, 97, 
                      98, 98, 96, 107]
}

df = pd.DataFrame(data)

sns.set_style("whitegrid")


plt.figure(figsize=(10, 5))
sns.lineplot(x=df["Year"], y=df["Temperature_F"], marker='o', linewidth=2, color='red')
plt.xlabel("Year")
plt.ylabel("Temperature (°F)")
plt.title("Yearly Highest Temperatures in Memphis (2000-2023)")
plt.xticks(rotation=45) 
plt.grid(True)


plt.show()


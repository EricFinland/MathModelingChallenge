import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random


#this is my first try at it but not as good as the second try
#base paremeters
base_demand = 4350  
years = 20
simulations = 10000

#data from Government Utility Reports
population_growth_rate = 0.012  
temperature_increase_rate = 0.3  
urban_heat_multiplier = 1.02  
income_elasticity = -0.3  
price_elasticity = -0.2  
green_space_impact = -0.15 
solar_adoption_rate = 0.01  
ev_growth_rate = 0.05  
smart_home_efficiency = -0.005  


simulated_peaks = []

#monte Carlos Part
for _ in range(simulations):
    future_demand = base_demand
    population_factor = 1.0
    energy_price = 0.08  
    income_growth = 0.02  
    green_space_factor = 1.0
    solar_factor = 1.0
    ev_factor = 1.0
    efficiency_factor = 1.0

    for year in range(years):
        temp_rise = random.uniform(0.2, 0.5)  
        demand_change_temp = temp_rise * 50 
        

        population_factor *= (1 + population_growth_rate)  
        demand_change_pop = (future_demand * (population_factor - 1)) * 0.8  

        demand_change_urban = future_demand * (urban_heat_multiplier - 1)

        demand_change_income = (future_demand * income_growth) * income_elasticity

        demand_change_price = (future_demand * (energy_price - 0.08)) * price_elasticity

        green_space_factor *= (1 + 0.005)
        demand_change_green = future_demand * green_space_impact * green_space_factor

        solar_factor *= (1 + solar_adoption_rate)
        demand_change_solar = future_demand * (solar_adoption_rate * -1)

        ev_factor *= (1 + ev_growth_rate)
        demand_change_ev = future_demand * (ev_growth_rate * 0.5)  

        efficiency_factor *= (1 + smart_home_efficiency)
        demand_change_efficiency = future_demand * smart_home_efficiency

        future_demand += (demand_change_temp + demand_change_pop + demand_change_urban + 
                          demand_change_income + demand_change_price + demand_change_green + 
                          demand_change_solar + demand_change_ev + demand_change_efficiency)

    simulated_peaks.append(future_demand)

plt.figure(figsize=(10, 5))
sns.histplot(simulated_peaks, bins=50, kde=True, color="orange")
plt.axvline(np.mean(simulated_peaks), color='red', linestyle='dashed', label="Expected Peak Demand")
plt.xlabel("Peak Demand in MW")
plt.ylabel("Frequency")
plt.title("Monte Carlo Simulation: Future Peak Electricity Demand in Memphis")
plt.legend()
plt.grid()
plt.show()

expected_demand = np.mean(simulated_peaks)
print(f"📈 Expected Peak Demand in Memphis (2043): {expected_demand:.2f} MW")

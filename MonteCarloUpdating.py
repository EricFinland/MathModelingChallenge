#Working Code that utilizes a Monte Carlos Simulation to predict the future peak demand of Megawatts
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import matplotlib.animation as animation
import tkinter as tk
from collections import deque

#in for my Pc not to die the average will just be tracking from the previous 400 runs.  
#We run it 1 million times to see how much the values skew so that we can pin point it down to the closest we can.

base_demand = 4350
grid_capacity = 5000
years = 20
simulations = 10000
max_runs = 1_000_000  
rolling_window_size = 400
rolling_average_queue = deque(maxlen=rolling_window_size)

#Data from Government reports
population_growth_rate = np.random.normal(0.012, 0.002)
temperature_increase_rate = np.random.normal(0.3, 0.05)
urban_heat_multiplier = 1.015
income_elasticity = -0.25
price_elasticity = -0.15
green_space_impact = -0.10
solar_adoption_rate = 0.008
ev_growth_rate = np.random.normal(0.04, 0.005)
smart_home_efficiency = -0.004

fig, ax = plt.subplots(figsize=(10, 6))
running = True  
run_count = 0  
ani = None  

def generate_simulation():
    global run_count
    simulated_peaks = []

    for _ in range(simulations // 10):
        if run_count >= max_runs:
            stop_animation()  
            return simulated_peaks

        future_demand = base_demand
        population_factor = 1.0
        energy_price = 0.08
        income_growth = 0.02
        green_space_factor = 1.0
        solar_factor = 1.0
        ev_factor = 1.0
        efficiency_factor = 1.0

        for year in range(years):
            temp_rise = np.random.normal(0.3, 0.05)
            demand_change_temp = temp_rise * 45
            population_factor *= (1 + np.random.normal(0.012, 0.002))
            demand_change_pop = (future_demand * (population_factor - 1)) * 0.75
            demand_change_urban = future_demand * (urban_heat_multiplier - 1)
            demand_change_income = (future_demand * income_growth) * income_elasticity
            demand_change_price = (future_demand * (energy_price - 0.08)) * price_elasticity
            green_space_factor *= (1 + 0.004)
            demand_change_green = future_demand * green_space_impact * green_space_factor
            solar_factor *= (1 + solar_adoption_rate)
            demand_change_solar = future_demand * (solar_adoption_rate * -1)
            ev_factor *= (1 + np.random.normal(0.04, 0.005))
            demand_change_ev = future_demand * (ev_growth_rate * 0.4)
            efficiency_factor *= (1 + smart_home_efficiency)
            demand_change_efficiency = future_demand * smart_home_efficiency

            future_demand += (demand_change_temp + demand_change_pop + demand_change_urban +
                              demand_change_income + demand_change_price + demand_change_green +
                              demand_change_solar + demand_change_ev + demand_change_efficiency)

        simulated_peaks.append(future_demand)
        rolling_average_queue.append(future_demand)
        run_count += 1  

    return simulated_peaks

def update(frame):
    global ani
    if not running or run_count >= max_runs:
        if ani:
            ani.event_source.stop()  
        return

    ax.clear()
    simulated_peaks = generate_simulation()
    if len(simulated_peaks) == 0:
        return  

    mean_peak = np.mean(simulated_peaks)
    rolling_average = np.mean(rolling_average_queue) if len(rolling_average_queue) > 0 else mean_peak

    print(f"Peak Demand: {mean_peak:.2f} MW | Rolling Avg (Last {rolling_window_size}): {rolling_average:.2f} MW | Total Runs: {run_count}")

    sns.histplot(simulated_peaks, bins=40, kde=True, color="orange", ax=ax)
    ax.axvline(mean_peak, color='red', linestyle='dashed', linewidth=2, label=f"Expected Peak: {mean_peak:.2f} MW")
    ax.axvline(rolling_average, color='blue', linestyle='dashed', linewidth=2, label=f"Rolling Avg: {rolling_average:.2f} MW")
    ax.axhline(y=grid_capacity, color='black', linestyle='dotted', linewidth=2, label="Grid Capacity")

    ax.set_xlabel("Peak Demand in MW", fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    ax.set_title(f"Carlos: Memphis Power Demand (Run {run_count}/{max_runs})", fontsize=14)
    ax.set_xlim([4500, 7000])
    ax.set_ylim([0, max(100, len(simulated_peaks) // 10)])  
    ax.legend(fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.5)

def stop_animation():
    global running, ani
    running = False
    if ani:
        ani.event_source.stop() 
    print("End. Total Runs:", run_count)

def start_animation():
    global running
    running = True
    print("Start Yay.")

root = tk.Tk()
root.title("Monte Carlo Fancy")

stop_button = tk.Button(root, text="Stop ", command=stop_animation, font=("Arial", 12))
stop_button.pack(pady=5)

start_button = tk.Button(root, text="Start ", command=start_animation, font=("Arial", 12))
start_button.pack(pady=5)

ani = animation.FuncAnimation(fig, update, interval=200)  

plt.show(block=False)  

root.mainloop()

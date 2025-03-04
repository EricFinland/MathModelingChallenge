import matplotlib.pyplot as plt


def vulnerability_index(population, income, no_vehicle, houses, public_transport, total_working, minors, elderly):
    term1 = 40 * (29393**2 / income**2)  # Income effect
    term2 = 30 * (no_vehicle / houses)   # Households with no vehicle
    term3 = 30 * (public_transport / total_working)  # Reliance on public transport
    index = (population / 618000) * (term1 + term2 + term3) 
    return index


baseline_params = {
    'population': 12360,
    'income': 84277,
    'no_vehicle': 331,
    'houses': 4903,
    'public_transport': 42,
    'total_working': 5977,
    'minors': 1511,
    'elderly': 1699
}


def sensitivity_analysis(baseline_params, variation=0.05):
    baseline_index = vulnerability_index(**baseline_params)
    sensitivity_results = []

    for param in baseline_params:
        param_value = baseline_params[param]

        # Decrease parameter by specified variation
        decreased_params = baseline_params.copy()
        decreased_params[param] = param_value * (1 - variation)
        decreased_index = vulnerability_index(**decreased_params)
        decrease_effect = ((decreased_index - baseline_index) / baseline_index) * 100

        # Increase parameter by specified variation
        increased_params = baseline_params.copy()
        increased_params[param] = param_value * (1 + variation)
        increased_index = vulnerability_index(**increased_params)
        increase_effect = ((increased_index - baseline_index) / baseline_index) * 100

        sensitivity_results.append({
            'parameter': param,
            'decrease_effect': decrease_effect,
            'increase_effect': increase_effect
        })

    return sensitivity_results

# Perform sensitivity analysis
results = sensitivity_analysis(baseline_params)

# Plotting the sensitivity analysis results
parameters = [result['parameter'] for result in results]
decrease_effects = [result['decrease_effect'] for result in results]
increase_effects = [result['increase_effect'] for result in results]

x = range(len(parameters))

plt.figure(figsize=(10, 6))
plt.bar(x, decrease_effects, width=0.4, label='-5%', align='center', color='blue')
plt.bar(x, increase_effects, width=0.4, label='+5%', align='edge', color='orange')
plt.xlabel('Parameters')
plt.ylabel('Change in Vulnerability Index (%)')
plt.title('Sensitivity Analysis of Vulnerability Index')
plt.xticks(x, parameters, rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

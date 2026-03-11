import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

temperature = [-10, -12, -15, -18, -20, -22, -25, -28, -30, -32]
syrup_sales = [100, 120, 140, 160, 190, 220, 250, 280, 300, 330]

corr_coef, p_value = pearsonr(temperature, syrup_sales)
print(f'Pearson correlation: {corr_coef:.2f}, p-value: {p_value:.4f}')

alpha = 0.05
if p_value < alpha:
    print("Reject H0: Significant correlation")
else:
    print("Fail to reject H0: No significant correlation")

plt.scatter(temperature, syrup_sales)
plt.xlabel('Air Temperature (°C)')
plt.ylabel('Cough Syrup Sales (units)')
plt.title('Temperature vs. Cough Syrup Sales')
plt.grid(True)
plt.show()

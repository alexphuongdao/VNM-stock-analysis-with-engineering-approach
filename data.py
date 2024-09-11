import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
years = [2022, 2023]
consumption_per_capita = [18, 28]

# Forecast
forecast_years = np.linspace(2022, 2023.99, 24)
forecast_consumption_per_capita = np.linspace(18, 28 * (1 + 0.08), 24)

# Convert decimal years to month-year format
forecast_dates = [pd.to_datetime(year, format='%Y') for year in forecast_years]

# Create DataFrame
df = pd.DataFrame({'Date': forecast_dates,
                   'Milk Consumption per Capita (liters/person/year)': forecast_consumption_per_capita})

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Milk Consumption per Capita (liters/person/year)'], marker='o')
plt.title('Forecast of Milk Consumption per Capita in Vietnam')
plt.xlabel('Date')
plt.ylabel('Milk Consumption per Capita (liters/person/year)')
plt.grid(True)

# Export to Excel
df.to_excel('milk_consumption_forecast.xlsx', index=False)

# Show plot
plt.show()


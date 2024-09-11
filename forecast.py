import pandas as pd
import matplotlib.pyplot as plt

# Data
years = [2023, 2024]  # Updated years
consumption_per_capita = [18, 28]

# Forecast
forecast_years = list(range(2023, 2025))  # Updated forecast years
forecast_consumption_per_capita = [18, 28 * (1 + 0.08)]

# Create DataFrame
df = pd.DataFrame({'Year': years + forecast_years,
                   'Milk Consumption per Capita (liters/person/year)': consumption_per_capita + forecast_consumption_per_capita})

# Map decimal point of year to corresponding months
month_mapping = {
    0.25: 'March',
    0.5: 'June',
    0.75: 'September'
}

# Update Year column with month names
df['Year'] = df['Year'].map(lambda x: str(int(x)) + ' ' + month_mapping.get(x - int(x), ''))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Milk Consumption per Capita (liters/person/year)'], marker='o')
plt.title('Growth of Milk Consumption per Capita in Vietnam')
plt.xlabel('Year')
plt.ylabel('Milk Consumption per Capita (liters/person/year)')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.grid(True)

# Export to Excel
df.to_excel('milk_consumption_forecast.xlsx', index=False)

# Show plot
plt.show()

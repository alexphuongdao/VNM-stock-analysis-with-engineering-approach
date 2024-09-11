import pandas as pd

# Create a DataFrame with the provided data
data = {
    "BU": ["Milk beverage", "Powdered milk", "Condensed milk"],
    "SBU Market Share (%)": [50, 30, 75],
    "Competitors' Market Share (%)": [33, 24, 25],
    "Relative Market Share within Industry (%)": [1.52, 1.25, 3.00],
    "Industry Sales Volume Growth Rate (%)": [21, 23, 10],
    "Revenue (Thousand Billion VND)": [9296.55, 7702.86, 4515.47]
}

df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("market_data.xlsx", index=False)

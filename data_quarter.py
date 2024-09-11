import pandas as pd

# Define 
data= {
    "": ["Revenue", "NPAT-MI", "GPM", "EBITDA", "OPM", "NPM", "FCF/Sales", "EV/EBITDA", "P/E", "P/B", "ROE"],
    "2022": [59956, 8516, "39.9%", "20.2%", "16.3%", "14.2%", "14%", "10.5x", "19.1x", "4.4x", "27.1%"],
    "2023F": [60231, 8898, "41.0%", "21.1%", "16.7%", "14.8%", "14%", "9.9x", "18.0x", "4.2x", "29.4%"],
    "2024F": [63393, 9872, "42.5%", "22.5%", "18.2%", "15.6%", "15%", "8.9x", "16.2x", "4.1x", "31.7%"],
    "2025F": [66998, 10408, "42.6%", "22.5%", "18.3%", "15.5%", "14%", "8.4x", "15.4x", "4.0x", "32.5%"],
    "2026F": [70580, 11110, "42.6%", "22.7%", "18.4%", "15.7%", "15%", "7.9x", "14.4x", "3.8x", "33.8%"]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Write DataFrame to Excel file
excel_file = "table_data.xlsx"
df.to_excel(excel_file, index=False)

print(f"Excel file '{excel_file}' has been created successfully.")

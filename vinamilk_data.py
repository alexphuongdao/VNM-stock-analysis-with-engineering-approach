import pandas as pd

# Data for the table
data = {
    'Metric': ['Mean Deviation', 'Semi Deviation', 'Standard Deviation', 'Variance'],
    'Value': [0.7227, 0.7851, 0.9979, 0.9957]
}

# Create DataFrame
df = pd.DataFrame(data)

# Export DataFrame to Excel
df.to_excel('metrics_table.xlsx', index=False)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_excel("Beneficiaries_Distribution_Detailed_2023.xlsx")

# Data preview
print(data.head())

# Group data by Gender and Quarter
grouped_data = data.groupby(['Quarter', 'Gender'])['Count'].sum().reset_index()

# Create a pivot table for visualization
pivot_data = grouped_data.pivot('Quarter', 'Gender', 'Count')

# Plot the data
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_data, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Beneficiaries Distribution by Gender and Quarter (2023)")
plt.xlabel("Gender")
plt.ylabel("Quarter")
plt.show()
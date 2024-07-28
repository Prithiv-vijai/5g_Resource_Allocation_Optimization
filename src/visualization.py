import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset (assuming it's named 'dataset.csv')
df = pd.read_csv('preprocessed_augmented_dataset.csv')

# Create a directory to store the graphs if it doesn't exist
graphs_dir = 'graphs'
os.makedirs(graphs_dir, exist_ok=True)

# Visualize the average allocated bandwidth for each application type
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Application_Type', y='Allocated_Bandwidth', estimator='mean')
plt.title('Average Allocated Bandwidth for Each Application Type')
plt.xlabel('Application Type')
plt.ylabel('Average Allocated Bandwidth')
plt.savefig(os.path.join(graphs_dir, 'average_allocated_bandwidth.png'))
plt.close()

# Analyze the correlation of numeric features only
numeric_df = df.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Numeric Features')
plt.savefig(os.path.join(graphs_dir, 'correlation_matrix.png'))
plt.close()

# Visualize the average latency for each application type
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Application_Type', y='Latency', estimator='mean')
plt.title('Average Latency for Each Application Type')
plt.xlabel('Application Type')
plt.ylabel('Average Latency')
plt.savefig(os.path.join(graphs_dir, 'average_latency.png'))
plt.close()

# Plot values below and above 100 efficiency, denoting inefficiency
plt.figure(figsize=(10, 6))
sns.histplot(df['Efficiency'], bins=20, kde=True)
plt.axvline(100, color='red', linestyle='--', label='Efficiency = 100')
plt.title('Distribution of Efficiency Values')
plt.xlabel('Efficiency')
plt.ylabel('Frequency')
plt.legend()
plt.savefig(os.path.join(graphs_dir, 'efficiency_distribution.png'))
plt.close()

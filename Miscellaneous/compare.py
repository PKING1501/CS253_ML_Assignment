import pandas as pd

# Read the CSV files
df1 = pd.read_csv('Best (1).csv')
df2 = pd.read_csv('Best.csv')

# Compare the dataframes
differences = df1.compare(df2)

# Print the differences
print(differences)
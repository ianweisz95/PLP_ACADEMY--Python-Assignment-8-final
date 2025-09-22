import pandas as pd
import matplotlib.pyplot as plt

# Load the metadata CSV (assumes it is in the current directory)
df = pd.read_csv('metadata.csv')

# Show the shape (rows and columns)
print("Data shape:", df.shape)

# Show the first 5 rows
print(df.head())

# Information about columns and data types
print(df.info())

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values per column:")
print(missing_values[missing_values > 0])

# Convert publish_time to datetime format, coerce errors for invalid parsing
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract publication year for analysis
df['year'] = df['publish_time'].dt.year

# Basic statistics on year column
print("Publication years:")
print(df['year'].value_counts().sort_index())

# Plot the number of publications per year
year_counts = df['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.title('Publications by Year in CORD-19 Dataset')
plt.show()

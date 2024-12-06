import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('replika.csv')

# Convert the 'review_date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Sort the DataFrame by the 'review_date' column
df_sorted = df.sort_values(by='date')

# Save the sorted DataFrame back to a CSV file
df_sorted.to_csv('sorted_replika.csv', index=False)

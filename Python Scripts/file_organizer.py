
import csv
import os

# Input and output file paths
input_file = 'RawDataSets/zomato.csv'

output_file = 'ScannableData/zomato.txt'

# Ensure 'ScannableData' folder exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Open the CSV file for reading
with open(input_file, newline='', encoding='utf-8') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    # Skip the header row if it exists
    next(reader, None)
    
    # Open a new file for writing the extracted content
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Iterate through each row in the CSV file
        for row in reader:
            # Extract the content from the row
            content = row[2]  # Assuming content is in the fourth column, change index if needed
            # Write the content to the output file
            outfile.write(content + '\n')

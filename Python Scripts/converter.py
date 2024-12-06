import csv

# Open the input file
with open('sorted_crunchyroll.csv', 'r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Read the header

    # Find the index of the 'date' column
    date_index = header.index('date')

    # Open the output file
    with open('crunchyroll_modified.csv', 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)

        # Write the header to the output file
        writer.writerow(header[:date_index + 1])

        # Write rows with only columns up to 'date'
        for row in reader:
            writer.writerow(row[:date_index + 1])

print("Successfully modified the CSV file.")

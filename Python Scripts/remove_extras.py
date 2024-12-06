input_file = 'sorted_esewa.csv'

# Open the original file and create a new file to write the modified content
with open(input_file, 'r', encoding='utf-8') as original_file, open('newEsewa.csv', 'w', encoding='utf-8') as modified_file:
    lines = original_file.readlines()  # Read all lines into a list

    # Write lines from 0 to 599587 (excluding 599588)
    modified_file.writelines(lines[:2])

    # Write lines from 1310714 (excluding 1310713) to the end of the file
    modified_file.writelines(lines[19509:])

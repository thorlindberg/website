import sys
import os
import csv

# Check if the --input argument is provided
if len(sys.argv) < 3 or sys.argv[1] != "--input":
    print("Usage: python3 main.py --input <csv_file>")
    sys.exit(1)

csv_file_path = sys.argv[2]

# Read values from CSV file
placeholders = {}
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if len(row) == 2:
            key, value = row
            placeholders[key] = value

# Read template
with open('template.txt', 'r') as file:
    template = file.read()

# Format template with placeholders
formatted_string = template.format(**placeholders)

# Write formatted output to file
output_file_path = 'output.txt'
with open(output_file_path, 'w') as file:
    file.write(formatted_string)

# Delete output
print("Press Enter when ready to delete output")
input()
os.remove(output_file_path)
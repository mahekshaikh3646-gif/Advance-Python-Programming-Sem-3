import csv
import json

input_file = "students.csv"
output_file = "students.json"

with open(input_file, "r", newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

with open(output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON.")
print("JSON file created:", output_file)

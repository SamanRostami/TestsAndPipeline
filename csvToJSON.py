import csv
import json

with open('Data/profiles1.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

with open('Data/profiles1.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(rows, jsonfile, indent=2, ensure_ascii=False)
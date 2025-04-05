import json
import csv

json_name = input()
with open(json_name,"r", encoding='utf-8') as f:
    load_data = json.load(f)
    csv_name = list(load_data.keys())[0].lower() + ".csv"
    data = load_data[list(load_data.keys())[0]]

with open(csv_name,"w", encoding='utf-8') as f:
    writer = csv.writer(f, delimiter = ";")
    writer.writerow(list(data[0].keys()))
    for i in data:
        writer.writerow(list(i.values()))
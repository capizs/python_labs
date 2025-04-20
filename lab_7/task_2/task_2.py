import json

load_data = json.load(open("ex_2.json", "r", encoding="utf-8"))

res = {}
for dict in load_data:
    res[dict["name"]] = dict["phoneNumber"]
print(res)
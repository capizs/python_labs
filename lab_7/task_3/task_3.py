import json 

new_data = {'id': 3, 
            'total': 150.00, 
            'items': [
                {
                    'name': 'item 4', 
                    'quantity': 2, 
                    'price': 100.00
                }, 
                {
                    'name': 'item 2', 
                    'quantity': 1, 
                    'price': 50.0
                }
            ]
        }

with open("ex_3.json", "r", encoding="utf-8") as f:
    load_data = json.load(f)
    load_data["invoices"].append(new_data)

with open("ex_3.json", "w", encoding="utf-8") as f:
    json.dump(load_data, f)
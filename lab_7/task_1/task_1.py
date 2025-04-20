import jsonschema
import json

schema = {
    "type": "object",
    "properties": {
        "movies": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "year": {"type": "integer"},
                    "cast": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "role": {"type": "string"}
                            }
                        },
                        "required": ["name", "role"] 
                    }
                },
                "required": ["title", "year", "cast"]
            }
        }  
    }
}


right_data = json.load(open("ex_1.json","r", encoding='utf-8'))
wrong_data = json.load(open("wrong_ex_1.json","r", encoding='utf-8'))

for data in (right_data, wrong_data):
    try:
        jsonschema.validate(instance=data, schema=schema)
        print("Данные валидны")
    except jsonschema.exceptions.ValidationError as err:
        print(f"Ошибка валидации: {err.message}")
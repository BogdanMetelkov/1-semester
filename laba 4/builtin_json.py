import json


def test_json():
  print("--- JSON (Built-in) ---")
  data = {"course": "Python", "lab": 4}
  json_str = json.dumps(data)
  print(f"Серіалізований JSON: {json_str}")
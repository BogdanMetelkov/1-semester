from datetime import datetime


def test_datetime():
  print("--- Datetime (Built-in) ---")
  now = datetime.now()
  print(f"Поточна дата і час: {now.strftime('%Y-%m-%d %H:%M:%S')}")
import pandas as pd


def test_pandas():
  print("--- Pandas Library ---")
  df = pd.DataFrame({"Ім'я": ["Анна", "Богдан"], "Вік": [20, 22]})
  print(df)
import numpy as np


def test_numpy():
  print("--- NumPy Library ---")
  arr = np.array([1, 2, 3, 4, 5])
  print(f"Масив: {arr}, Середнє значення: {np.mean(arr)}")
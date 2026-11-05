from builtin_datetime import test_datetime
from builtin_json import test_json
from builtin_math import test_math
from builtin_os import test_os
from builtin_random import test_random
from lib_bs4 import test_bs4
from lib_colorama import test_colorama
from lib_jinja2 import test_jinja2
from lib_matplotlib import test_matplotlib
from lib_numpy import test_numpy
from lib_openpyxl import test_openpyxl
from lib_pandas import test_pandas
from lib_pillow import test_pillow
from lib_requests import test_requests
from lib_rich import test_rich


def main():
  print("========================================")
  print(" ЗАПУСК ЛАБОРАТОРНОЇ РОБОТИ №4")
  print("========================================\n")

  # Виклик зовнішніх бібліотек
  test_requests()
  print()
  test_colorama()
  print()
  test_rich()
  print()
  test_numpy()
  print()
  test_pandas()
  print()
  test_pillow()
  print()
  test_bs4()
  print()
  test_openpyxl()
  print()
  test_matplotlib()
  print()
  test_jinja2()
  print()

  # Виклик вбудованих бібліотек
  test_math()
  print()
  test_os()
  print()
  test_json()
  print()
  test_datetime()
  print()
  test_random()
  print()

if __name__ == "__main__":
  main()
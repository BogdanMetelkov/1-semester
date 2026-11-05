from colorama import Fore, Style, init


def test_colorama():
  init(autoreset=True)
  print("--- Colorama Library ---")
  print(Fore.GREEN + "Цей текст зелений!")
  print(Fore.RED + Style.BRIGHT + "Цей текст яскраво-червоний!")
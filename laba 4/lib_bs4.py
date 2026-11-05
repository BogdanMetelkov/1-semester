from bs4 import BeautifulSoup


def test_bs4():
  print("--- BeautifulSoup4 Library ---")
  html_doc = "<html><body><h1>Привіт, світ!</h1></body></html>"
  soup = BeautifulSoup(html_doc, "html.parser")
  print(f"Знайдений заголовок: {soup.h1.string}")
from PIL import Image


def test_pillow():
  print("--- Pillow Library ---")
  img = Image.new("RGB", (100, 100), color="red")
  print(f"Створено зображення розміром: {img.size}")
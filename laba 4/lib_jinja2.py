from jinja2 import Template


def test_jinja2():
  print("--- Jinja2 Library ---")
  template = Template("Привіт, {{ name }}!")
  result = template.render(name="Студент")
  print(result)
import openpyxl


def test_openpyxl():
  print("--- Openpyxl Library ---")
  wb = openpyxl.Workbook()
  ws = wb.active
  ws["A1"] = "Тест Excel"
  print(f"Активний лист Excel: {ws.title}, значення A1: {ws['A1'].value}")
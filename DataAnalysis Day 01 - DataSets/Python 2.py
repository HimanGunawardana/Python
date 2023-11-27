import pandas as pd

df = pd.read_excel(r"world_population_excel_workbook.xlsx" , sheet_name = "Sheet1")
print(df)

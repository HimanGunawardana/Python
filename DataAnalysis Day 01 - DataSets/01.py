import pandas as pd

#df = pd.read_csv(r"Path where the CSV file is stored\file_name.csv")      #defferences of serious and data frame
#reading csv file
df = pd.read_csv(r"countries of the world.csv")
df = pd.read_csv(r"countries of the world.csv",sep = '\t')
print(df)

#reading text fie
df = pd.read_table(r"countries of the world.csv.txt")
df = pd.read_json(r"json_sample.json")

df = pd.read_excel(r"world_population_exel_workbook.xlsx",sheet_name='Sheet1')

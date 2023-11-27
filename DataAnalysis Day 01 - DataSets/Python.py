import pandas as pd
'''
df = pd.read_csv(r"countries of the world.txt")
print(df) '''

'''
df = pd.read_csv(r"countries of the world.txt",sep ="\t")
print(df) '''


df = pd.read_table(r"countries of the world.txt",sep ="\t")
print(df)



import pandas as pd

file_id = "1iI8xuBdl4Ro_8ewssr62c46urvBnQK9ETyj4XlOTSp0"
csv_url = f"https://docs.google.com/spreadsheets/d/{file_id}/export?format=csv&gid=0"

df = pd.read_csv(csv_url)
# print(df.head())
# print('___')
# x = df['saldo']
#
#
# for a in x:
#     print(a)
#
# # print(x)
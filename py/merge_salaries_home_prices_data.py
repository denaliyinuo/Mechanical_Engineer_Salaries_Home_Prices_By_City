import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from openpyxl import load_workbook


path1 = '/Users/nathanoliver/Desktop/Python/Home_Prices_Engineer_Salaries/csv/home_prices.csv'
path2 = '/Users/nathanoliver/Desktop/Python/Home_Prices_Engineer_Salaries/csv/me_salaries.csv'

# call file function


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


# call file

df1 = call_file(path1)
df2 = call_file(path2)

df1["cbsa_code"] = pd.to_numeric(df1["cbsa_code"])

print(df1.columns)
print(df1.dtypes)


print(df2.columns)
print(df2.dtypes)

df3 = pd.merge(df1, df2, on="cbsa_code", how='inner')

path = '/Users/nathanoliver/Desktop/Python/Home_Prices_Engineer_Salaries/csv/salaries_home_prices_final.csv'

df3 = df3.replace(',', '', regex=True)
df3 = df3.replace('%', '', regex=True)

df3.to_csv(path)

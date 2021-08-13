import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

pd.set_option('display.max_rows', 500)

# call file function


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


# call file
path = '/Users/nathanoliver/Desktop/Python/Home_Prices_Engineer_Salaries/csv/salaries_home_prices_final.csv'
df = call_file(path)

df["A_MEDIAN"] = pd.to_numeric(df["A_MEDIAN"])

print(df.columns)
print(df.dtypes)

df['ratio'] = df['A_MEDIAN'] / df['2021.Ir']

df.sort_values(by=['2021.Ir'], ascending=False, inplace=True)

df_new = pd.DataFrame(
    zip(df['AREA_TITLE'], df['2021.Ir'], df['A_MEDIAN'], df['ratio']))

print(df_new)

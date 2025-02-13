import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_dataframe(path):
    df = pd.read_csv(path, sep=',')
    df.index = df['UNIQUE_ID'].astype(str) + '_' + df['POSITION_TITLE'].astype(str)
    return df
def get_min_values(df):
    print("---------------------------------")
    s = df.columns
    print(s)

def remove_column(df, column):
    df_new = df
    df_new = df_new.drop(column, axis=1)
    return df_new

def lowest_salaries (df, m, n):
    latest_empleyed = df.sort_values('HIRE_DATE').head(m)
    the_least_paid = latest_empleyed.sort_values('BASE_SALARY').head(n)
    return the_least_paid

def salaries_per_department(df):
    grouped = df.groupby(['GENDER', 'POSITION_TITLE']).agg({'BASE_SALARY': ['mean','median']})
    return grouped


dataframe = read_dataframe(str('employee.csv'))
print(dataframe)
new_one = remove_column(dataframe, 'UNIQUE_ID')

print(lowest_salaries(new_one,5,4))
print(salaries_per_department(dataframe))

# WYKRESY

maks_min = dataframe.groupby(['DEPARTMENT','EMPLOYMENT_TYPE']).agg({'BASE_SALARY':['max','min']})

maks_min.plot.bar()

plt.title("Wykres słupkowy ")
plt.legend(title = 'LEGENDA', loc = 'upper left')
plt.ylabel("SALARY")

plt.show()
print(get_min_values(dataframe))
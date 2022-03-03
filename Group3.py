import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Group3:
    Other_Countries = pd.read_excel('Country_Visitor.xlsx')
    df_Other_Countries = Other_Countries.iloc[0:120,30:35]
    print(df_Other_Countries)

    splitcolumn = Other_Countries['   '].str.split(' ', n=1, expand = True)
    Other_Countries = Other_Countries.assign(Year=splitcolumn[0])
    Other_Countries = Other_Countries.assign(Month=splitcolumn[1])
    Other_Countries.index = Other_Countries['   ']
    del Other_Countries['   ']
    print(Other_Countries)

    usaSum = df_Other_Countries[" USA "].sum()
    print("Sum of USA (US): ", usaSum)

    canadaSum = df_Other_Countries[" Canada "].sum()
    print("Sum of Canada (CA): ", canadaSum)

    australiaSum = df_Other_Countries[" Australia "].sum()
    print("Sum of Australia (AU): ", australiaSum)

    newzealandSum = df_Other_Countries[" New Zealand "].sum()
    print("Sum of New Zealand (NZ): ", newzealandSum)

    africaSum = df_Other_Countries[" Africa "].sum()
    print("Sum of Africa (AF): ", africaSum)

    panda_Country = pd.DataFrame(df_Other_Countries.loc[:].sum())
    panda_Country = panda_Country.rename(columns={0:'Total Visitors'})
    new_panda_Country = panda_Country.sort_values(by='Total Visitors', ascending=False)
    print(new_panda_Country)
    ax = new_panda_Country['Total Visitors'].plot(kind= 'bar', title='Amount of Visitors', figsize=(10,10), legend=True, fontsize=12, )
    myFig = ax.get_figure()
    myFig.savefig('TotalVisitors.png')
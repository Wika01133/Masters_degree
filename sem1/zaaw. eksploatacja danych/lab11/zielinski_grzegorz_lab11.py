import pandas as pd
import numpy as np
import os

ltcameroon = pd.read_csv('D:\studia\magisterka\magisterka\sem1\zaaw. eksploatacja danych\lab11\ltcameroon.csv')
ltpoland = pd.read_csv('D:\studia\magisterka\magisterka\sem1\zaaw. eksploatacja danych\lab11\ltpoland.csv')
nls97weeksworked = pd.read_csv('D:\studia\magisterka\magisterka\sem1\zaaw. eksploatacja danych\lab11/nls97weeksworked.csv')
nls97colenr = pd.read_csv('D:\studia\magisterka\magisterka\sem1\zaaw. eksploatacja danych\lab11/nls97colenr.csv')


#zadanie 1 
print(f"---Zadanie 1---")
#a
print("\na) nic sensownego do wyswietlenia")
ltall = pd.concat([ltcameroon, ltpoland])

#b
print("\nb)")
print(ltall['country'].value_counts())

#c
print("\nc) nic sensownego do wyswietlenia")
directory = 'D:\studia\magisterka\magisterka\sem1\zaaw. eksploatacja danych\lab11\dane/ltcountry'

#d
print("\nd)")
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        temp_df = pd.read_csv(os.path.join(directory, filename))
        ltall = pd.concat([ltall, temp_df])
        print(f'File: {filename}, Rows: {temp_df.shape[0]}')
        if set(temp_df.columns) != set(ltall.columns):
            print(f'Column differences in {filename}:', set(temp_df.columns).symmetric_difference(set(ltall.columns)))

#e
column_diff = set(ltcameroon.columns).symmetric_difference(set(ltpoland.columns))
print("\ne)")
print(f'Column differences: {column_diff}')

#f
print("\nf)")
print(ltall[['country', 'station', 'month', 'temperature', 'latitude']].sample(5))

#g
print("\ng)")
print(ltall['country'].value_counts().sort_index())

#h
print("\nh)")
stats = ltall.groupby('country')['temperature'].agg(['min', 'mean', 'max', 'count'])
print(stats)

#i
print("\ni) nic sensownego do wyswietlenia")
ltall.loc[ltall['country'] == 'Oman', 'latitude'] = ltall.loc[ltall['country'] == 'Oman', 'latitude']

#j
print("\nj)")
stats_updated = ltall.groupby('country')['temperature'].agg(['min', 'mean', 'max', 'count'])
print(stats_updated)

#zadanie 2
print("\n\n --- Zadanie 2 --- ")
#a
print("\na)")
print(nls97weeksworked.sample(5))
print(nls97colenr.sample(5))
print(nls97weeksworked.shape)
print(nls97colenr.shape)
print(nls97weeksworked['originalid'].nunique())
print(nls97colenr['originalid'].nunique())

#b
print("\nb)")
print(nls97weeksworked.duplicated(subset=['originalid', 'year']).sum())
print(nls97colenr.duplicated(subset=['originalid', 'year']).sum())

#c
print("\nc) nic sensownego do wyswietlenia")
def checkmerge(df1, df2, key):
    merge_df = df1.merge(df2, on=key, how='outer', indicator=True)
    only_df1 = merge_df[merge_df['_merge'] == 'left_only']
    only_df2 = merge_df[merge_df['_merge'] == 'right_only']
    both = merge_df[merge_df['_merge'] == 'both']
    return only_df1, only_df2, both

#d
print("\nd)")
only_weeksworked, only_colenr, both = checkmerge(nls97weeksworked, nls97colenr, ['originalid', 'year'])
print(only_weeksworked.shape)
print(only_colenr.shape)
print(both.shape)

#e
print("\ne)")
merged_df = nls97weeksworked.merge(nls97colenr, on=['originalid', 'year'], how='inner')

#f
print("\nf)")
print(merged_df.shape)
print(merged_df.sample(5))

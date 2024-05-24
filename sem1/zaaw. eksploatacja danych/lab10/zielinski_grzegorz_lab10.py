import pandas as pd
import numpy as np

coviddaily720 = pd.read_csv("coviddaily720.csv")
ltbrazil = pd.read_csv("ltbrazil.csv")



print("\n\n----------ZADANIE 1----------")
#a
coviddaily720 = coviddaily720.sort_values(by=['location', 'casedate'])
print("\na)")
print(coviddaily720.head())

#b
prevloc = 'ZZZ'
rowlist = []
casecnt = 0

for _, row in coviddaily720.iterrows():
    if row['location'] != prevloc:
        if prevloc != 'ZZZ':
            rowlist.append({'location': prevloc, 'casecnt': casecnt})
        casecnt = 0
        prevloc = row['location']
    casecnt += row['new_cases']

rowlist.append({'location': prevloc, 'casecnt': casecnt})

print("\nb) Długość rowlist:", len(rowlist))
print("Pierwsze 4 elementy rowlist:", rowlist[:4])

#c
covidtotals = pd.DataFrame(rowlist)
print(covidtotals.head())

#d
ltbrazil = ltbrazil.sort_values(by=['station', 'month'])

#e
ltbrazil = ltbrazil.dropna(subset=['temperature'])
    


print("\n\n----------ZADANIE 2----------")
#a
loclist = coviddaily720['location'].unique().tolist()
print("\na) nic do wyswietlenia")

#b
rowlist = []
covid_data = coviddaily720[['location', 'new_cases']].to_numpy()

for loc in loclist:
    cases = [row[1] for row in covid_data if row[0] == loc]
    rowlist.append(sum(cases))

print("\nb) Długość rowlist:", len(rowlist))
print("Długość loclist:", len(loclist))

#c
casetotals = pd.DataFrame(list(zip(loclist, rowlist)), columns=['location', 'casetotals'])
print("\nc)")
print(casetotals.head())



print("\n\n----------ZADANIE 3----------")
#a
print("\na) nic do wyswietlenia")
countrytots = coviddaily720.groupby('location').sum().reset_index()

#b
print("\nb)")
print(countrytots.iloc[:5, :5])

#c
print("\nc)")
print(countrytots.iloc[-5:, :5])

#d
print("\nd)")
print(countrytots[countrytots['location'] == 'Zimbabwe'].iloc[:5, :5])

#e
print("\ne)")
for name, group in countrytots.groupby('location'):
    if name in ['Malta', 'Kuwait']:
        print(f"Group: {name}")
        print(group.iloc[:5, :5])



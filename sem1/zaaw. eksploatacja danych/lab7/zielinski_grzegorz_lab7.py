import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


covidtotals = pd.read_csv("D:\studia\magisterka\\magisterka\sem1\zaaw. eksploatacja danych\lab7\covidtotals.csv")
nls = pd.read_csv("D:\studia\magisterka\magisterka\\sem1\zaaw. eksploatacja danych\lab7\\nls97.csv")
landtemps = pd.read_csv("D:\studia\magisterka\magisterka\\sem1\zaaw. eksploatacja danych\lab7\landtemps2019avgs.csv")

covidtotals.set_index('iso_code', inplace=True)
nls.set_index('personid', inplace=True)
landtemps.set_index('locationid', inplace=True)

pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 15)
pd.set_option('display.width', 100)
pd.set_option('float_format', '{:,.0f}'.format)

def exercise1():
    # Zadanie 1:
    print("exercise 1:\n")
    # a)
    print("\n a) \n")
    random_samples = landtemps.sample(10, random_state=42)[['station', 'country', 'latabs', 'elevation', 'avgtemp']]
    print(random_samples)

    # b)
    print("\n b) \n")
    mean_temp = landtemps['avgtemp']
    plt.hist(mean_temp, bins=20, alpha=0.7, color='green', edgecolor='black')
    plt.axvline(mean_temp.mean(), color='black', linestyle='dashed', linewidth=2)
    plt.title('Rozkład Średnich Temperatur w Stacjach Meteorologicznych')
    plt.xlabel('Średnia Temperatura')
    plt.ylabel('Liczba Stacji')
    plt.show()
    print("wykres")

    # c)
    print("\n c) \n")
    import scipy.stats as stats
    stats.probplot(mean_temp, dist="norm", plot=plt)
    plt.title('Q-Q plot dla Średnich Temperatur')
    plt.xlabel('Teoretyczne kwantyle')
    plt.ylabel('Uporządkowane wartości')
    plt.show()
    print("wykres")
    
    # d)
    print("\n d) \n")
    skewness = covidtotals['total_cases_pm'].skew()
    kurtosis = covidtotals['total_cases_pm'].kurtosis()
    print("Skośność: ", skewness)
    print("Kurtoza: ", kurtosis)

    # e)
    print("\n e) \n")
    regions = ['Oceania / Aus', 'East Asia', 'Southern Africa', 'Western Europe']
    fig, axes = plt.subplots(nrows=1, ncols=len(regions), figsize=(16, 4))
    for i, region in enumerate(regions):
        region_data = covidtotals[covidtotals['region'] == region]['total_cases_pm']
        axes[i].hist(region_data, bins=20, alpha=0.7, color='green', edgecolor='black')
        axes[i].set_title(region)
        axes[i].set_xlabel('Liczba przypadków na milion mieszkańców')
        axes[i].set_ylabel('Liczba krajów')
    plt.tight_layout()
    plt.show()
    print("wykres")

    # f)
    print("\n f) \n")
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
    for i, region in enumerate(regions):
        region_data = covidtotals[covidtotals['region'] == region]['total_cases_pm']
        row = i // 2
        col = i % 2
        axes[row, col].hist(region_data, bins=20, alpha=0.7, color='green', edgecolor='black')
        axes[row, col].set_title(region)
        axes[row, col].set_xlabel('Liczba przypadków na milion mieszkańców')
        axes[row, col].set_ylabel('Liczba krajów')
    plt.tight_layout()
    plt.show()
    print("wykres")

def exercise2():
    # Zadanie 2:
    print("\n\n Exercise 2:\n\n")
    # a) 
    print("\n a) \n")
    plt.figure(figsize=(8,6))
    nls['satverbal'].plot(kind='box', vert=False, patch_artist=True, flierprops=dict(marker='o', markersize=8, markerfacecolor='r', linestyle='none'))
    plt.title('Wyniki egzaminu SAT - Część Humanistyczna')
    plt.xlabel('Wyniki')
    plt.yticks([])
    plt.grid(True)
    quartiles = nls['satverbal'].quantile([0.25, 0.5, 0.75])
    plt.annotate('Q1', xy=(quartiles[0.25], 0.5), xytext=(quartiles[0.25] - 50, 0.5), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('Q2', xy=(quartiles[0.5], 0.5), xytext=(quartiles[0.5] - 50, 0.5), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('Q3', xy=(quartiles[0.75], 0.5), xytext=(quartiles[0.75] + 10, 0.5), arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()
    print("wykres")
    
    # b)
    print("\n b) \n")
    weeksworked = nls[['highestdegree', 'weeksworked16', 'weeksworked17']]
    print(weeksworked)
    
    # c)
    print("\n c) \n")
    plt.figure(figsize=(10, 6))
    plt.boxplot([weeksworked['weeksworked16'].dropna(), weeksworked['weeksworked17'].dropna()],
                labels=['Tygodnie przepracowane w 2016 roku', 'Tygodnie przepracowane w 2017 roku'],
                patch_artist=True, showfliers=True)
    plt.title('Liczba przepracowanych tygodni w roku 2016 i 2017')
    plt.ylabel('Liczba tygodni')
    plt.show()
    print("wykres")
    
    # d)
    print("\n d) \n")
    covidtotalsonly = covidtotals[['total_cases', 'total_deaths', 'total_cases_pm', 'total_deaths_pm']]
    totvarslabels = ['Liczba przypadków', 'Liczba zgonów', 'Liczba przypadków na milion mieszkańców', 'Liczba zgonów na milion mieszkańców']

    # e)
    print("\n e) \n")
    plt.figure(figsize=(10, 6))
    plt.boxplot([covidtotalsonly['total_cases_pm'].dropna(), covidtotalsonly['total_deaths_pm'].dropna()],
                labels=['Liczba przypadków na milion mieszkańców', 'Liczba zgonów na milion mieszkańców'],
                patch_artist=True, showfliers=True)
    plt.title('Liczba przypadków i zgonów na milion mieszkańców')
    plt.ylabel('Liczba na milion mieszkańców')
    plt.show()

    # f)
    print("\n f) \n")
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
    for i, var in enumerate(covidtotalsonly.columns):
        row = i // 2
        col = i % 2
        axes[row, col].boxplot(covidtotalsonly[var].dropna(), patch_artist=True, showfliers=True)
        axes[row, col].set_title(totvarslabels[i])
        axes[row, col].set_xticklabels([''])
        axes[row, col].set_ylabel('Liczba')
    plt.suptitle('Wykresy pudełkowe liczby przypadków i zgonów', fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def exercise3():
    # a)
    print("\n a) \n")
    def gettots(x):
        return x.describe().loc[['min', '25%', '50%', '75%', 'max', 'count']]

    # b)
    print("\n b) \n")
    stats_nls = nls.groupby('highestdegree')['weeksworked17'].apply(gettots).unstack()
    print(stats_nls)

    # c)
    print("\n c) \n")
    plt.figure(figsize=(10,6))
    nls.boxplot(column='weeksworked17', by='highestdegree', vert=False, patch_artist=True, showfliers=True, grid=True)
    plt.title('Liczba przepracowanych tygodni w 2017 roku w zależności od poziomu wykształcenia')
    plt.xlabel('Liczba tygodni')
    plt.ylabel('Poziom wykształcenia')
    plt.show()
    print("wykres")

    # d)
    print("\n d) \n")
    stats_covid = covidtotals.groupby('region')['total_cases_pm'].apply(gettots).unstack()
    print(stats_covid)
    
    # e)
    print("\n e) \n")
    plt.figure(figsize=(13,8))
    sns.boxplot(data=covidtotals, x='total_cases_pm', y='region', orient='h', showfliers=True, palette='Set2')
    sns.swarmplot(data=covidtotals, x='total_cases_pm', y='region', orient='h', color='k', alpha=0.5)
    plt.title('Liczba przypadków COVID-19 na milion mieszkańców w podziale na regiony')
    plt.xlabel('Liczba przypadków na milion mieszkańców')
    plt.ylabel('Region')
    plt.show()
    print("wykres")

    # f)
    print("\n f) \n")
    high_cases = covidtotals[covidtotals['total_cases_pm'] >= 14000]
    locations = high_cases[['location', 'total_cases_pm']]
    print(locations)
    
    # g)
    print("\n g) \n")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=high_cases, x='region', y='total_cases_pm', flierprops={'marker':'o', 'color':'red'})
    sns.swarmplot(data=high_cases, x='region', y='total_cases_pm', color='black', alpha=0.6)

    plt.xlabel("Region")
    plt.ylabel("Liczba przypadków na milion mieszkańców")
    plt.title("Rozkład liczby przypadków COVID-19 na milion mieszkańców w podziale na regiony bez wartości ekstremalnych")
    plt.show()
    print("wykres")

exercise1()
exercise2()
exercise3()
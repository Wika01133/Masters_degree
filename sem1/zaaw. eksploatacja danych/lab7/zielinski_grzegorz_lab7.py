import pandas as pd
import numpy as np

# Wczytanie plików do zmiennych
covidtotals = pd.read_csv("covidtotals.csv")
nls = pd.read_csv("nls97.csv")
landtemps = pd.read_csv("landtemps2019avgs.csv")

# Ustawienie odpowiednich indeksów
covidtotals.set_index('iso_code', inplace=True)
nls.set_index('personid', inplace=True)
landtemps.set_index('stationid', inplace=True)

# Ustawienie opcji wyświetlania ramki danych
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 15)
pd.set_option('display.width', 100)
pd.set_option('float_format', '{:,.0f}'.format)

def exervise1():
    # Zadanie 1:
    # a) Wybierz 10 losowych próbek danych dotyczących stacji meteorologicznych
    random_samples = landtemps.sample(10, random_state=42)[['stationname', 'country', 'latitude', 'elevation', 'avgtemp']]

    # b) Wygeneruj histogram przedstawiający rozkład średnich temperatur w stacjach meteorologicznych
    import matplotlib.pyplot as plt
    mean_temp = landtemps['avgtemp']
    plt.hist(mean_temp, bins=20, alpha=0.7, color='blue', edgecolor='black')
    plt.axvline(mean_temp.mean(), color='red', linestyle='dashed', linewidth=1)
    plt.title('Rozkład Średnich Temperatur w Stacjach Meteorologicznych')
    plt.xlabel('Średnia Temperatura')
    plt.ylabel('Liczba Stacji')
    plt.show()

    # c) Przeprowadź analizę kwantyl-kwantyl (qq-plot)
    import scipy.stats as stats
    stats.probplot(mean_temp, dist="norm", plot=plt)
    plt.title('Q-Q plot dla Średnich Temperatur')
    plt.xlabel('Teoretyczne kwantyle')
    plt.ylabel('Uporządkowane wartości')
    plt.show()

    # d) Oblicz skośność i kurtozę dla danych dotyczących liczby przypadków COVID-19 na milion mieszkańców
    skewness = covidtotals['total_cases_per_million'].skew()
    kurtosis = covidtotals['total_cases_per_million'].kurtosis()
    print("Skośność: ", skewness)
    print("Kurtoza: ", kurtosis)

    # e) Narysuj histogramy liczby przypadków COVID-19 na milion mieszkańców dla czterech wybranych regionów
    regions = ['Oceania / Australia', 'East Asia', 'Southern Africa', 'Western Europe']
    fig, axes = plt.subplots(nrows=1, ncols=len(regions), figsize=(16, 4))
    for i, region in enumerate(regions):
        region_data = covidtotals[covidtotals['region'] == region]['total_cases_per_million']
        axes[i].hist(region_data, bins=20, alpha=0.7, color='green', edgecolor='black')
        axes[i].set_title(region)
        axes[i].set_xlabel('Liczba przypadków na milion mieszkańców')
        axes[i].set_ylabel('Liczba krajów')
    plt.tight_layout()
    plt.show()

    # f) Przedstaw na jednym wykresie cztery histogramy liczby przypadków COVID-19 na milion mieszkańców dla czterech wybranych regionów
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
    for i, region in enumerate(regions):
        region_data = covidtotals[covidtotals['region'] == region]['total_cases_per_million']
        row = i // 2
        col = i % 2
        axes[row, col].hist(region_data, bins=20, alpha=0.7, color='orange', edgecolor='black')
        axes[row, col].set_title(region)
        axes[row, col].set_xlabel('Liczba przypadków na milion mieszkańców')
        axes[row, col].set_ylabel('Liczba krajów')
    plt.tight_layout()
    plt.show()

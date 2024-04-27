import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

covidmissing = pd.read_csv("covidtotalswithmissings.csv")
covidtotals = pd.read_csv("covidtotals.csv")

covidtotals.set_index("iso_code", inplace=True)
covidmissing.set_index("iso_code", inplace=True)

pd.set_option('display.width', 100)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 15)
pd.set_option('display.float_format', '{:.0f}'.format)

print(covidtotals)
print(covidmissing)

def exercise1():
    print("Exercise1")
   # a) 
    print("\nA)\n")
    totvars = ['location', 'total_cases', 'total_deaths', 'total_cases_pm', 'total_deaths_pm']
    demovars = [col for col in covidmissing.columns if col not in totvars]
    
    print(totvars)
    print(demovars)

    # b)
    print("\nB)\n")
    missing_demovars = covidmissing[demovars].isnull().sum()
    print("Liczba brakujących wartości w kolumnach demograficznych:")
    print(missing_demovars)

    # c)
    print("\nC)\n")
    rows_with_three_or_more_missing = covidmissing[demovars].isnull().sum(axis=1) >= 3
    num_rows_with_three_or_more_missing = rows_with_three_or_more_missing.sum()
    print("Liczba wierszy z co najmniej trzema brakującymi wartościami w kolumnach demograficznych:", num_rows_with_three_or_more_missing)
 
    # d)
    print("\nD)\n")
    rows_with_three_or_more_missing_indices = covidmissing[rows_with_three_or_more_missing].head().index
    print("Nazwy lokalizacji oraz wartości brakujących zmiennych demograficznych dla pięciu pierwszych wierszy:")
    print(covidmissing.loc[rows_with_three_or_more_missing_indices, demovars])

    print("Typ danych dla liczby brakujących wartości w kolumnach demograficznych:", type(num_rows_with_three_or_more_missing))

    # e) 
    print("\nE)\n")
    missing_totvars = covidmissing[totvars].isnull().sum()
    print("Liczba brakujących wartości w kolumnach totvars:")
    print(missing_totvars)

    # f)
    print("\nF)\n")
    rows_with_any_missing_totvars = covidmissing[totvars].isnull().any(axis=1)
    num_rows_with_any_missing_totvars = rows_with_any_missing_totvars.sum()
    print("Liczba wierszy z co najmniej jedną brakującą wartością w kolumnach totvars:", num_rows_with_any_missing_totvars)

    # g)
    print("\nG)\n")
    rows_with_any_missing_totvars_indices = covidmissing[rows_with_any_missing_totvars].index
    print("Dane dla wszystkich kolumn z wierszy, które mają co najmniej jedną brakującą wartość w totvars:")
    print(covidmissing.loc[rows_with_any_missing_totvars_indices])

    # h)
    print("\nH)\n")
    covidmissing['total_cases_pm'] = covidmissing['total_cases'] / (covidmissing['population'] / 1_000_000)
    covidmissing['total_deaths_pm'] = covidmissing['total_deaths'] / (covidmissing['population'] / 1_000_000)
    print(covidmissing['total_cases_pm'])
    print(covidmissing['total_deaths_pm'])


def exercise2():
    print("Exercise2")
    # a)
    print("\nA)\n")
    totvars = ['total_cases', 'total_deaths', 'total_cases_pm', 'total_deaths_pm']
    demovars = [col for col in covidtotals.columns if col not in totvars]

    # b)
    print("\nB)\n")
    pd.set_option('display.float_format', '{:.2f}'.format)

    # c)
    print("\nC)\n")
    quantiles = covidtotals[totvars].quantile(np.arange(0, 1.1, 0.1))
    print("Kwantyle od 0\% do 100% z krokiem co 10\% dla wartości kumulacyjnych:")
    print(quantiles)

    # d)
    print("\nD)\n")
    skewness = covidtotals[totvars].skew()
    print("Skośność (skewness) dla wartości kumulacyjnych:")
    print(skewness)

    # e)
    print("\nE)\n")
    kurtosis = covidtotals[totvars].kurtosis()
    print("Kurtoza (kurtosis) dla wartości kumulacyjnych:")
    print(kurtosis)

    # f)
    print("\nF)\n")
    import scipy.stats as stats
    def test_normalnosci(var, df):
       stat, p = stats.shapiro(df[var])
       return p
       
    print(test_normalnosci("total_cases",covidtotals))
    print(test_normalnosci("total_deaths", covidtotals))
    print(test_normalnosci("total_cases_pm", covidtotals))
    print(test_normalnosci("total_deaths_pm",covidtotals))

    # g)
    print("\nG)\n")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    for i, col in enumerate(['total_cases', 'total_cases_pm']):
        stats.probplot(covidtotals[col], dist="norm", plot=axes[i])
        axes[i].set_title(f'QQ plot dla {col}')
    plt.tight_layout()
    plt.show()

    # h)
    print("\nH)\n")
    def wyswietl_odstajace(data, column):
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        odstajace = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
        print("Wartości odstające dla kolumny", column)
        print(odstajace)
    wyswietl_odstajace(covidtotals, "total_cases")

    # i)
    print("\nI)\n")
    pop_density_quantiles = covidtotals["pop_density"].quantile([0.25, 0.5, 0.75])
    gdp_per_capita_quantiles = covidtotals["gdp_per_capita"].quantile([0.25, 0.5, 0.75])

    print("Kwantyle dla zmiennej 'pop_density':")
    print(pop_density_quantiles)

    print("Kwantyle dla zmiennej 'gdp_per_capita':")
    print(gdp_per_capita_quantiles)


    # j)
    print("\nJ)\n")
    covidtotals_log = covidtotals.copy()
    covidtotals_log[['total_cases_log', 'total_deaths_log', 'total_cases_pm_log', 'total_deaths_pm_log']] = covidtotals[['total_cases', 'total_deaths', 'total_cases_pm', 'total_deaths_pm']].apply(np.log1p)
    print(covidtotals_log)

    # k)
    print("\nK)\n")
    from seaborn import histplot
    plt.figure(figsize=(8,6))
    histplot(covidtotals_log['total_cases_log'], bins=20, color='black')
    plt.title('Histogram dla logarytmicznej liczby przypadków')
    plt.xlabel('Logarytmiczna liczba przypadków')
    plt.ylabel('Liczebność')
    plt.show()


exercise1()
exercise2()
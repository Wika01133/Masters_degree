import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

def exercise3():
    print("Exercise3")

    totvars = ['total_cases', 'total_deaths', 'total_cases_pm', 'total_deaths_pm']
    demovars = [col for col in covidtotals.columns if col not in totvars]
    # a)
    print("\nA)\n")
    numeric_columns = [col for col in covidtotals.columns if pd.api.types.is_numeric_dtype(covidtotals[col])]
    correlation_matrix = covidtotals[numeric_columns].corr()
    print("Macierz korelacji:")
    print(correlation_matrix)

    # b)
    print("\nB)\n")
    covidtotalsonly = covidtotals.loc[:, totvars]
    print(covidtotalsonly)
    
    # c)
    print("\nC)\n")
    covidtotalsonly['total_cases_q'] = pd.qcut(covidtotalsonly['total_cases'], q=5, labels=['very low', 'low', 'medium', 'high', 'very high'], precision=0)
    print(covidtotalsonly['total_cases_q'])
    
    # d)
    print("\nD)\n")
    covidtotalsonly['total_deaths_q'] = pd.qcut(covidtotalsonly['total_deaths'], q=5, labels=['very low', 'low', 'medium', 'high', 'very high'], precision=0)
    print(covidtotalsonly['total_deaths_q'])
    
    # e)
    print("\nE)\n")
    pivot_table = pd.pivot_table(covidtotalsonly, index='total_cases_q', columns='total_deaths_q', aggfunc=len, fill_value=0, observed=False)
    print("Tabela przestawna:")
    print(pivot_table)
    
    # f) 
    print("\nF)\n")
    selected_rows = covidtotals.loc[(covidtotalsonly['total_cases_q'] == 'very high') & (covidtotalsonly['total_deaths_q'] == 'medium')]
    selected_rows_transposed = selected_rows.T
    print("Wiersze po selekcji i transpozycji:")
    print(selected_rows_transposed)
    
    # g)
    print("\nG)\n")
    selected_rows_g = covidtotals.loc[(covidtotalsonly['total_cases_q'] == 'low') & (covidtotalsonly['total_deaths_q'] == 'high')]
    # Transpozycja macierzy
    selected_rows_transposed_g = selected_rows_g.T
    print("Wiersze po selekcji i transpozycji:")
    print(selected_rows_transposed_g)
    
    # h)
    print("\nH)\n")
    average_hosp_beds = covidtotals['hosp_beds'].mean()
    print("Średnia wartość kolumny 'hosp_beds':", average_hosp_beds)

    # i)
    print("\nI)\n")
    plt.figure(figsize=(10, 6))
    sns.regplot(x='total_cases', y='total_deaths', data=covidtotals)
    plt.xlabel('Liczba przypadków')
    plt.ylabel('Liczba zgonów')
    plt.title('Wykres regresji: Liczba przypadków vs. Liczba zgonów')
    plt.show()
    print("wykres 1")
    
    # j)
    print("\nJ)\n")
    selected_rows = covidtotals.loc[(covidtotals['total_cases'] < 300000) & (covidtotals['total_deaths'] > 20000)]
    selected_rows_transposed = selected_rows.T
    print("Wiersze po selekcji i transpozycji:")
    print(selected_rows_transposed)

    # k)
    print("\nK)\n")
    selected_rows_k = covidtotals.loc[(covidtotals['total_cases'] > 300000) & (covidtotals['total_deaths'] < 10000)]
    selected_rows_transposed_k = selected_rows_k.T
    print("Wiersze po selekcji i transpozycji:")
    print(selected_rows_transposed_k)

    # l)
    print("\nL)\n")
    plt.figure(figsize=(10, 6))
    sns.regplot(x='total_cases_pm', y='total_deaths_pm', data=covidtotals)
    plt.xlabel('Liczba przypadków na milion mieszkańców')
    plt.ylabel('Liczba zgonów na milion mieszkańców')
    plt.title('Wykres regresji: Liczba przypadków na milion mieszkańców vs. Liczba zgonów na milion mieszkańców')
    plt.show()
    print("wykres 2")
    
    
exercise3()
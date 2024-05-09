import pandas as pd
import numpy as np

nls97b = pd.read_csv("nls97b.csv")

nls97b.set_index('personid', inplace=True)

pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 15)
pd.set_option('display.width', 100)
pd.set_option('float_format', '{:,.0f}'.format)


def exercise1():
    print("Zadanie 1:\n")
    # a)
    mean_gpa = nls97b['gpaoverall'].mean()
    print("a) Średnia wartość oceny (GPA) wszystkich studentów:", mean_gpa)

    # b)
    stats_gpa = nls97b['gpaoverall'].describe()
    print("\nb) Statystyki opisowe dla rozkładu średniej oceny (GPA) studentów:")
    print(stats_gpa)

    # c) 
    quantiles_gpa = nls97b['gpaoverall'].quantile(np.arange(0.1, 1.1, 0.1))
    print("\nc) Kwantyle dla średniej oceny (GPA) studentów:")
    print(quantiles_gpa)

    # d)
    selected_students = nls97b[(nls97b['gpaoverall'] >= 3) & (nls97b['gpaoverall'] <= 3.5)].head(5)
    print("\nd) Pięciu studentów z oceną (GPA) między 3 a 3.5:")
    print(selected_students)

    # e)
    count_students_gpa = nls97b[(nls97b['gpaoverall'] >= 3) & (nls97b['gpaoverall'] <= 3.5)].shape[0]
    print("\ne) Liczba studentów z oceną (GPA) między 3 a 3.5:", count_students_gpa)

    # f)
    random_selected_students = nls97b[(nls97b['gpaoverall'] < 2) | (nls97b['gpaoverall'] > 4)].sample(5)
    print("\nf) Pięciu losowych studentów z oceną (GPA) poniżej 2 lub powyżej 4:")
    print(random_selected_students)

    # g)
    gpa_percentile = nls97b['gpaoverall'].quantile(0.99)
    selected_students_percentile = nls97b[nls97b['gpaoverall'] > gpa_percentile]
    count_students_percentile = selected_students_percentile.shape[0]
    min_gpa_percentile = selected_students_percentile['gpaoverall'].min()
    max_gpa_percentile = selected_students_percentile['gpaoverall'].max()
    print("\ng) Liczba studentów przekraczających 99 percentyl oceny (GPA):", count_students_percentile)
    print("   Minimalna wartość oceny (GPA) dla tych studentów:", min_gpa_percentile)
    print("   Maksymalna wartość oceny (GPA) dla tych studentów:", max_gpa_percentile)

    # h)
    gpa_above_4 = (nls97b['gpaoverall'] > 4).any()
    print("\nh) Czy którykolwiek z studentów ma ocenę (GPA) większą niż 4?:", gpa_above_4)

    # i)
    gpa_no_negative = (nls97b['gpaoverall'] >= 0).all()
    print("\ni) Czy wszystkie oceny średnie (GPA) studentów są większe lub równe 0?:", gpa_no_negative)

    # j)
    count_students_gpa_above_zero = (nls97b['gpaoverall'] > 0).sum()
    print("\nj) Liczba studentów z oceną (GPA) większą od zera:", count_students_gpa_above_zero)

    # k)
    count_students_gpa_zero = (nls97b['gpaoverall'] == 0).sum()
    print("\nk) Liczba studentów z oceną (GPA) równą zero:", count_students_gpa_zero)

    # l)
    count_students_no_gpa = nls97b['gpaoverall'].isna().sum()
    print("\nl) Liczba studentów bez przypisanej oceny (GPA):", count_students_no_gpa)

    # m)
    income_quantiles = nls97b['highestgradecompleted'].quantile([0.25, 0.5, 0.75])
    low_income_gpa = nls97b[nls97b['highestgradecompleted'] < income_quantiles[0.25]]['gpaoverall'].mean()
    high_income_gpa = nls97b[nls97b['highestgradecompleted'] > income_quantiles[0.75]]['gpaoverall'].mean()
    print("\nm) Średnia ocena studentów o niskim dochodzie:", low_income_gpa)
    print("Średnia ocena studentów o wysokim dochodzie:", high_income_gpa)

    # n)
    count_marital_status = nls97b['maritalstatus'].value_counts()
    print("\nn) Liczba studentów w każdej kategorii stanu cywilnego:")
    print(count_marital_status)
        
        
        
def exercise2():
    print("\n\nZadanie 2:\n")
    # a)
    gpa_multipield = nls97b['gpaoverall'] * 100
    print("a) Pierwsze pięć wartości po pomnożeniu przez 100:")
    print(gpa_multipield.head())

    # b)
    nls97b.loc[100061, 'gpaoverall'] = 3
    nls97b.loc[[100139, 100284, 100292], 'gpaoverall'] = 0
    print("b) Wartość 3 dla wiersza o indeksie 100061: ")
    print(nls97b.loc[100061, 'gpaoverall'])
    print("\nWiersze o indeksach 100139, 100284 i 100292 ustaw wartość na 0.")
    print(nls97b.loc[[100139, 100284, 100292], 'gpaoverall'])

    # c)
    nls97b['childnum'] = nls97b['childathome'] + nls97b['childnotathome']
    childnum_counts = nls97b['childnum'].value_counts().sort_index()
    print("\nc) Liczba wystąpień różnych wartości w kolumnie 'childnum':")
    print(childnum_counts)

    # d)
    nls97b.loc[100061:100292, 'gpaoverall'] = nls97b['gpaoverall'].mean()
    print("\nd) Wartosci gpa dla indeksów 100061 do 100292 po zmianie:")
    print(nls97b.loc[100061:100292, 'gpaoverall'])

    # e)
    nls97b.iloc[0, nls97b.columns.get_loc('gpaoverall')] = 2
    nls97b.iloc[1:4, nls97b.columns.get_loc('gpaoverall')] = 1
    print("\ne) Wartość 2 dla pierwszego wiersza i wartość 1 dla wierszy od drugiego do czwartego:")
    print(nls97b.iloc[0:4, nls97b.columns.get_loc('gpaoverall')])

    # f)
    max_gpa = nls97b['gpaoverall'].max()
    nls97b.loc[nls97b['gpaoverall'] > 4, 'gpaoverall'] = 4
    print("\n f) Najwiepsze wartości przed zmianami: ")
    print(max_gpa)
    print("\n Największe wartości po zmianach:")
    print(nls97b['gpaoverall'].nlargest())

    # g)
    print("\ng) Typ zwracany przez loc dla indeksu 100061:", type(nls97b.loc[100061, 'gpaoverall']))
    print("Typ zwracany przez loc dla indeksu 100061 z wykorzystaniem listy jako drugiego argumentu:", type(nls97b.loc[[100061], 'gpaoverall']))

exercise1()
exercise2()
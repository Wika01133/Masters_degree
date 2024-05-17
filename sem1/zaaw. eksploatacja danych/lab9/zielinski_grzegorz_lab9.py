import pandas as pd
import numpy as np

nls97c = pd.read_csv("nls97c.csv")

pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 15)
pd.set_option('display.width', 100)
pd.set_option('float_format', '{:,.0f}'.format)


def exercise1():
    print("\n\n----------ZADANIE 1----------")
    #a
    govprovidejobs_counts = nls97c['govprovidejobs'].value_counts()
    print("\na) Liczba wystąpień wartości w kolumnie 'govprovidejobs:",govprovidejobs_counts)

    #b
    nls97c['govprovidejobsdefprob'] = np.where(nls97c['govprovidejobs'].isnull(), np.nan, np.where(nls97c['govprovidejobs'].str.contains('not', na=False), 'No', 'Yes'))
    print("\nb) Nowa ramka:", nls97c['govprovidejobsdefprob'])
    
    #c
    govprovidejobs_pivot = pd.pivot_table(nls97c, values='personid', index='govprovidejobs', columns='govprovidejobsdefprob', aggfunc='count')
    print("\nc) Utworzenie tablicy przestawnej na podstawie kolumn 'govprovidejobs' i 'govprovidejobsdefprob'", govprovidejobs_pivot)

    #d
    maritalstatus_counts = nls97c['maritalstatus'].value_counts()
    print("\nd) Liczba wystąpień poszczególnych wartości w kolumnie 'maritalstatus':", maritalstatus_counts)

    #e
    maritalstatus_starts_with_space = nls97c['maritalstatus'].str.startswith(" ").any()
    print("\ne)Czy istnieje wartość w kolumnie 'maritalstatus', która zaczyna się od spacji:", maritalstatus_starts_with_space)

    #f
    maritalstatus_ends_with_space = nls97c['maritalstatus'].str.endswith(" ").any()
    print("\nf)")
    print("Czy istnieje wartość w kolumnie 'maritalstatus', która kończy się spacją:", maritalstatus_ends_with_space)

    #g
    nls97c['evermarried'] = np.where(nls97c['maritalstatus'].isnull(), np.nan, np.where(nls97c['maritalstatus'].str.strip() == 'Never-married', 'No', 'Yes'))
    print("\ng) Dodanie nowej kolumny 'evermarried':")
    print(nls97c['evermarried'])

    #h
    evermarried_pivot = pd.pivot_table(nls97c, values='personid', index='maritalstatus', columns='evermarried', aggfunc='count')
    print("\nh) Utworzenie tablicy przestawnej na podstawie kolumn 'maritalstatus' i 'evermarried'", evermarried_pivot)

    #i
    nls97c['receivedba'] = np.where(nls97c['highestdegree'].isnull(), np.nan,
                                    np.where(nls97c['highestdegree'].str[0].isin(['4', '5', '6', '7']), 'Yes', 'No'))
    print("\ni) Dodanie nowej kolumny 'receivedba'")
    print(nls97c['receivedba'])

    #j
    receivedba_pivot = pd.pivot_table(nls97c, values='personid', index='highestdegree', columns='receivedba', aggfunc='count')
    print("\nj)Utworzenie tablicy przestawnej na podstawie kolumn 'highestdegree' i 'receivedba'")
    print(receivedba_pivot)

    #k 
    weeklyhrstv_df = nls97c['weeklyhrstv'].head().reset_index(drop=True)
    num_list = [40, 2, 5, 10, 8]
    df = pd.DataFrame({'weeklyhrstv': weeklyhrstv_df, 'num': num_list})
    print("\nk) Utworzenie nowego obiektu DataFrame dla kolumny 'weeklyhrstv' i odpowiednio dopasowanych liczb:")
    print(df)

    #l
    def getnum(lst):
        if isinstance(lst, list):
            if lst[0] == 40:
                return 45
            elif lst[-1] == 2:
                return 1
            else:
                return lst[-1] - 5
        else:
            return np.nan
    print('l) Funkcja getnum')

    #m
    nls97c['weeklyhrstvnum'] = nls97c['weeklyhrstv'].str.extract(r'(\d+)').astype(float)
    nls97c['weeklyhrstvnum'] = nls97c['weeklyhrstvnum'].apply(getnum)
    print("\nm) Obliczenie liczby godzin spędzonych na oglądaniu telewizji:")
    print(nls97c['weeklyhrstvnum'])

    #n
    weeklyhrstv_pivot = pd.pivot_table(nls97c, values='personid', index='weeklyhrstv', columns='weeklyhrstvnum', aggfunc='count')
    print("\nn) Utworzenie tabeli przestawnej dla kolumn 'weeklyhrstv' i 'weeklyhrstvnum'")
    print(weeklyhrstv_pivot)

    #o
    comphrsold = ["None", "Less than 1 hour a week", "1to3hours a week", "4to6hours a week", "7to9hours a week", "10hours or more a week"]
    comphrsnew = ["A. Zero", "B. Mniej niż godzinę w tygodniu", "C.1-3 godziny w tygodniu", "D.4-6 godzin w tygodniu", "E. 7-9 godzin w tygodniu", "F. Więcej niż 10 godzin tygodniowo"]
    nls97c['weeklyhrscomputer_new'] = nls97c['weeklyhrscomputer'].replace(comphrsold, comphrsnew)
    print("\no) Zamiana kategorii 'weeklyhrscomputer'")
    print(nls97c[['weeklyhrscomputer', 'weeklyhrscomputer_new']])

    #p
    weeklyhrscomputer_counts = nls97c['weeklyhrscomputer'].value_counts().sort_index()
    print("\np) Liczba wystąpień w 'weeklyhrscomputer' posortowana")
    print(weeklyhrscomputer_counts)
    
def exercise2():
    print("\n\n----------ZADANIE 2----------")
    #a
    schoolrecordlist = ['satverbal', 'satmath', 'gpaoverall', 'gpaenglish', 'gpamath', 'gpascience', 'highestdegree', 'highestgradecompleted']
    demolist = ['maritalstatus', 'childathome', 'childnotathome', 'wageincome', 'weeklyhrscomputer', 'weeklyhrstv', 'nightlyhrssleep']
    print("\na) Utworzenie dwóch list", schoolrecordlist, demolist)
    
    #b
    schoolrecord = nls97c[schoolrecordlist]
    print("\nb) Stworzenie zmiennej schoolrecord:", schoolrecord)

    #c
    missing_values_col = schoolrecord.isnull().sum()
    print("\nc) Liczba brakujących wartości w kolumnach schoolrecord:")
    print(missing_values_col)

    #d
    misscnt = schoolrecord.isnull().sum(axis=1)
    print("\nd) Liczba brakujących wartości w wierszach schoolrecord:", misscnt)

    #e
    misscnt_counts = misscnt.value_counts().sort_index()
    print("\ne) Liczba brakujących wartości w wierszach schoolrecord:")
    print(misscnt_counts)

    #f
    rows_with_seven_or_more_missing_values = schoolrecord[misscnt >= 7].head(4).T
    print("\nf) Wiersze z co najmniej 7 brakującymi wartościami:")
    print(rows_with_seven_or_more_missing_values)
    
    #g
    schoolrecord = schoolrecord.dropna(thresh=2)
    print("\ng) Usunięcie wierszy z mniej niż 2 wartościami niepustymi", schoolrecord)

    #h
    missing_values_after_drop = schoolrecord.isnull().sum(axis=1).value_counts().sort_index()
    print("\nh) Liczba brakujących wartości w wierszach schoolrecord po usunięciu:")
    print(missing_values_after_drop)
    
    #i
    gpaoverall_mean_rounded_down = np.floor(schoolrecord['gpaoverall'].mean())
    print("\ni) Skonwertowana średnia wartość gpaoverall na liczbę całkowitą, zaokrąglając w dół")
    print(gpaoverall_mean_rounded_down)
    
    #j
    missing_values_gpaoverall = schoolrecord['gpaoverall'].isnull().sum()
    print("\nj) Liczba brakujących wartości w kolumnie 'gpaoverall' przed uzupełnieniem:")
    print(missing_values_gpaoverall)
    
    #k
    mean_gpaoverall = schoolrecord['gpaoverall'].mean().round()
    schoolrecord['gpaoverall'].fillna(mean_gpaoverall, inplace=True)
    print("\nk) Wypełnienie brakujących wartości w kolumnie 'gpaoverall'")
    print(schoolrecord['gpaoverall'])

    #l
    missing_values_gpaoverall_after_fill = schoolrecord['gpaoverall'].isnull().sum()
    print("\nl) Liczba brakujących wartości w kolumnie 'gpaoverall' po uzupełnieniu:", missing_values_gpaoverall_after_fill)
    

exercise1()
exercise2()
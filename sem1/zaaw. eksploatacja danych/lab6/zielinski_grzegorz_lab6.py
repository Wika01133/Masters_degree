import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

covidtotals = pd.read_csv("covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

pd.set_option('display.width', 100)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 15)
pd.set_option('display.float_format', '{:.0f}'.format)

print(covidtotals)

def exercise1():
    # a)
    print("\na)\n")
    scaler = StandardScaler()
    # b)
    print("\nb)\n")
    selected_columns = ['location', 'total_cases_pm', 'total_deaths_pm', 'pop_density', 'median_age', 'gdp_per_capita']
    print(selected_columns)
    
    # c)
    print("\nc)\n")
    covidanalysis = covidtotals[selected_columns].dropna()
    print(covidanalysis)

    # d)
    print("\nd)\n")
    covidanalysisstand = scaler.fit_transform(covidanalysis.iloc[:, 1:])
    print(covidanalysisstand)

    # e)
    print("\ne)\n")
    clf_name = 'Local Outlier Factor'
    print(clf_name)

    # f)
    print("\nf)\n")
    from sklearn.neighbors import LocalOutlierFactor
    clf = LocalOutlierFactor(contamination=0.1)
    print(clf)

    # g)
    print("\ng)\n")
    clf.fit(covidanalysisstand)
    print(clf)
    
    # h)
    print("\nh)\n")
    y_pred = clf.fit_predict(covidanalysisstand)
    print(y_pred)
    
    # i)
    print("\ni)\n")
    y_scores = clf.negative_outlier_factor_
    print(y_scores)
    
    # j)
    print("\nj)\n")
    pred = pd.DataFrame({'outlier': y_pred, 'scores': y_scores}, index=covidanalysis.index)
    
    np.random.seed(1)
    print(pred.sample(10))
    
    # k)
    print("\nk)\n")
    print(pred['outlier'].value_counts())

    # l)
    print("\nl)\n")
    grouped_pred = pred.groupby('outlier')['scores'].agg(['min', 'median', 'max'])
    print(grouped_pred)

    # m)
    print("\nm)\n")
    outliers_covid = pd.concat([covidanalysis, pred], axis=1)[pred['outlier'] == 1]
    outliers_covid = outliers_covid[['location', 'total_cases_pm', 'total_deaths_pm', 'scores']]
    outliers_covid_sorted = outliers_covid.sort_values(by='scores', ascending=False)
    print(outliers_covid_sorted)
    
    
def exercise2():
    print("\n\nZadanie 2:\n")
    # a) 
    print("\na)\n")
    analysisvars = ['location', 'total_cases_pm', 'total_deaths_pm', 'pop_density', 'median_age', 'gdp_per_capita']
    print(analysisvars)

    # b)
    print("\nb)\n")
    scaler = StandardScaler()

    # c)
    print("\nc)\n")
    missing_values = covidtotals.isnull().sum()
    print(missing_values)

    # d)
    print("\nd)\n")
    covidanalysis = covidtotals[analysisvars].dropna()
    print(covidanalysis)

    # e)
    print("\ne)\n")
    covidanalysisstand = scaler.fit_transform(covidanalysis.iloc[:, 1:])
    print(covidanalysisstand)

    # f)
    print("\nf)\n")
    clf = IsolationForest(n_estimators=100, max_samples='auto', contamination=0.1, max_features=1.0)
    print(clf)
    
    # g)
    print("\ng)\n")
    clf.fit(covidanalysisstand)
    print(clf)

    # h)
    print("\nh)\n")
    covidanalysis['anomaly'] = clf.predict(covidanalysisstand)
    print(covidanalysis['anomaly'])

    # i)
    print("\ni)\n")
    covidanalysis['scores'] = clf.decision_function(covidanalysisstand)
    print(covidanalysis['scores'])

    # j)
    print("\nj)\n")
    print(covidanalysis['anomaly'].value_counts())

    # k)
    print("\nk)\n")
    inliers = covidanalysis[covidanalysis['anomaly'] == 1]
    outliers = covidanalysis[covidanalysis['anomaly'] == -1]
    print("inliners:")
    print(inliers)
    print("outliers:")
    print(outliers)

    # l)
    print("\nl)\n")
    outliers_sorted = outliers[['location', 'total_cases_pm', 'total_deaths_pm', 'median_age', 'gdp_per_capita', 'scores']].sort_values(by='scores', ascending=False).head(10)
    print(outliers_sorted)

    # m)
    print("\nm)\n")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(inliers['gdp_per_capita'], inliers['median_age'], inliers['total_cases_pm'], c='blue', label='Normal')

    ax.scatter(outliers['gdp_per_capita'], outliers['median_age'], outliers['total_cases_pm'], c='red', label='Anomaly')

    ax.set_xlabel('GDP per Capita')
    ax.set_ylabel('Median Age')
    ax.set_zlabel('Total Cases per Million')
    ax.set_title('Detection of Anomalies using Isolation Forest')
    ax.legend()
    plt.show()
    
exercise1()
exercise2()
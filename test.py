import numpy as np
import pandas as pd
import regex as re
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.metrics import r2_score
import sklearn as skl

if __name__ == "__main__":
    df = pd.read_csv('raw_data.csv')

    for a in df:
        bad = False
        for b in df[a]:
            try:
                if b.isalpha():
                    bad = True
            except:
                pass
        if bad:
            vals = list(df[a].tolist())
            vals2 = []
            for v in vals:
                if v not in vals2:
                    vals2.append(v)
            thing = preprocessing.LabelEncoder()
            thing.fit(vals2)
            df[a] = thing.transform(vals)

    df.fillna(0, inplace=True)

    x, y = df.iloc[:, :-1], df.iloc[:, [-1]]

    regressor = LinearRegression()
    regressor.fit(x, y)
    stuff = regressor.predict(x)

    final_stuff = []
    for z in stuff:
        final_stuff.append(z[0])
    score1 = r2_score(y, final_stuff)
    print('LINEAR REGRESSION ACCURACY: ', score1)
    regressor = skl.linear_model.Lasso(.001)
    regressor.fit(x, y)

    score2=  r2_score(y, regressor.predict(x))
    print('LASSO ACCURACY: ', score2)

    from sklearn.tree import DecisionTreeRegressor
    # create regressor
    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)
    output = regressor.predict(x)
    print("DECISION TREE ACCURACY:", regressor.score(x, y))

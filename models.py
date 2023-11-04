from sklearn.linear_model import LinearRegression, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

class Linear_Regression:
    def __init__(self, data):
        regressor = LinearRegression()
        regressor.fit(data.x, data.y)
        print('linear init')

    def visualize(self):
        pass

class Lasso_Regression:
    def __init__(self, data):
        print('lasso init')

    def visualize(self):
        pass

class Decision_Tree:
    def __init__(self, data):
        print('decision tree init')

    def visualize(self):
        pass


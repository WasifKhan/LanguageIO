from numpy import array, polyfit
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from matplotlib import pyplot as plt

class Model:
    def __init__(self, model):
        self.name = model
        if model == 'Linear Regression':
            self.regressor = LinearRegression()
        elif model == 'Lasso Regression':
            self.regressor = Lasso(0.01)
        elif model == 'Decision Tree Regression':
            self.regressor = DecisionTreeRegressor()
        else:
            raise TypeError('Incorrect Model Specified') 


    def fit(self, x_train, y_train):
        self.regressor.fit(x_train, y_train)


    def predict(self, x_test, y_test):
        self.prediction = self.regressor.predict(x_test)
        score = r2_score(self.prediction, y_test)
        print(f'{self.name} accuracy: {score}')

    
    def display(self, y_test):
        plt.title(f'{self.name}')
        plt.xlabel('Actual')
        plt.ylabel('Predicted')

        plt.scatter(y_test, self.prediction, color='g')
        y_test = array(y_test).squeeze()
        pred = array(self.prediction).squeeze()
        a, b = polyfit(y_test, pred, 1)
        plt.plot(y_test, a*y_test+b)
        plt.show()
    

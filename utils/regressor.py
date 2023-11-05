from sklearn.linear_model import LinearRegression, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

class Model:
    def __init__(self, model):
        self.name = model
        if model == 'Linear Regression':
            self.regressor = LinearRegression()
        elif model == 'Lasso Regression':
            self.regressor = Lasso(0.001)
        elif model == 'Decision Tree Regression':
            self.regressor = DecisionTreeRegressor()
        else:
            raise TypeError('Incorrect Model Specified') 


    def fit(self, x_train, y_train):
        self.regressor.fit(x_train, y_train)


    def predict(self, x_test, y_test):
        prediction = self.regressor.predict(x_test)
        score = r2_score(prediction, y_test)
        print(f'{self.name} accuracy: {score}')


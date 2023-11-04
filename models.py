from sklearn.linear_model import LinearRegression, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

class Model:
    def __init__(self, model, data):
        regressor = None
        if model == 'Linear Regression':
            regressor = LinearRegression()
        elif model == 'Lasso Regression':
            regressor = Lasso(0.001)
        elif model == 'Decision Tree Regression':
            regressor = DecisionTreeRegressor()
        else:
            print('Incorrect Model Specified')
            return

        regressor.fit(data.x_train, data.y_train)
        prediction = regressor.predict(data.x_test)
        score = r2_score(prediction, data.y_test)
        print(f'{model} accuracy: {score}')


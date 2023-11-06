from utils.data_processor import DataProcessor
from utils.regressor import Model 

FILENAME = 'data/raw_data.csv'

if __name__ == "__main__":
    data = DataProcessor(FILENAME)
    models = ['Linear Regression', 'Lasso Regression', 'Decision Tree Regressor']
    
    for model in models:
        regressor = Model(model)
        regressor.fit(data.x_train, data.y_train)
        regressor.predict(data.x_test, data.y_test)
        regressor.display(data.y_test)


        

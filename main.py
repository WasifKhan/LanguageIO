from extract_data import Extract_Data
from models import Model 

if __name__ == "__main__":
    data = Extract_Data('raw_data.csv')
    linear_regression = Model('Linear Regression', data)
    lasso_regression = Model('Lasso Regression', data)
    decision_tree = Model('Decision Tree Regression', data)

        

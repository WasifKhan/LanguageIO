from extract_data import Extract_Data
from models import Linear_Regression
from models import Lasso_Regression
from models import Decision_Tree

if __name__ == "__main__":
    data = Extract_Data('raw_data.csv')
    models = {}
    models['linear_regression'] = Linear_Regression(data)
    models['lasso_regression'] = Lasso_Regression(data)
    models['decision_tree'] = Decision_Tree(data)
    for key in models:
        models[key].visualize()

        

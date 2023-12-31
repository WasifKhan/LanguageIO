# LanguageIO ML Exercise

## How To Run
* Clone this repository
* Required libraries: numpy, pandas, matplotlib, sklearn
* Run *main.py* using Python3.10 +

## Results
#### **Linear Regression Accuracy: 83%**
![Linear Regression](https://github.com/WasifKhan/LanguageIO/blob/master/images/linreg.png)
#### **Lasso Regression Accuracy: 79%**
![Lasso Regression](https://github.com/WasifKhan/LanguageIO/blob/master/images/lasso.png)
#### **Decision Tree Regressor Accuracy: 71%**
![Decision Tree Regressor](https://github.com/WasifKhan/LanguageIO/blob/master/images/decision.png)

## Data Exploration
* Meaningful dimensions are: Length, is_stopword and part of speech
* Source_client was included in model as there is *moderate* relationship with mistranslation probability
![Source v target](https://github.com/WasifKhan/LanguageIO/blob/master/images/source_client%20v%20target.png)
* *POS* and *Part Of Speech* are duplicates, only need 1 of these columns
* *num_words* does not belong in this dataset. Also all entries are 1 so doesn't effect result
* *fillna* should be replaced with *dropna* given low cardinality for columns
* To reduce variance, consider nouns and pronouns as idential part of speech
* No correlation between dates columns and mistranslation probability so we omit these, some examples:
![date1](https://github.com/WasifKhan/LanguageIO/blob/master/images/date1.png)
![date2](https://github.com/WasifKhan/LanguageIO/blob/master/images/date2.png)
![date4](https://github.com/WasifKhan/LanguageIO/blob/master/images/date4.png)
* Aggregating dates into 1 column still doesn't provide any meaningful relationship with mistranslation probability
![date4](https://github.com/WasifKhan/LanguageIO/blob/master/images/date%20added%20to%20system.png)

## Possible Reasons for Bad Prediction
* Data needs to be split into train/test data. High accuracy is a result of testing on same data model was trained with
* Low bias, high variance. The model is overfitting with unnecessary dimensions
* Not enough data points/too many columns. VC-dimension calculation shows that 5 dimensions require ~100 datapoints for *p-value < 0.05*

## Improvements In Provided Code
* Line 7: Import only what is needed, not entire library
* Line 13, 38: Variable names should be informative, perhaps call this 'numeric_data', 'prediction' respectively
* Line 41: Don't need to map prediction, r2_score function can handle raw input
* Line 42, 47, 54: Use f-strings for printing
* Line 43: Import Lasso directly
* Line 51: Imports should be at beginning of file 

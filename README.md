# LanguageIO ML Exercise

## How To Run
* Clone this repository
* Required libraries: numpy, pandas, matplotlib, sklearn
* Run *main.py* using Python3.10 +

## Visual Results
#### **Linear Regression Accuracy: 89%**
![Linear Regression](https://github.com/WasifKhan/LanguageIO/blob/master/images/linreg.png)
#### **Lasso Regression Accuracy: 87%**
![Lasso Regression](https://github.com/WasifKhan/LanguageIO/blob/master/images/lasso.png)
#### **Decision Tree Regressor Accuracy: 82%**
![Decision Tree Regressor](https://github.com/WasifKhan/LanguageIO/blob/master/images/decision.png)

## Data Exploration
* *POS* and *Part Of Speech* are duplicates, only need 1 of these columns 
* *num_words* does not belong in this dataset. Also all entries are 1 so doesn't affect result
* *fillna* should be replaced with *dropna* given low cardinality for columns
* To reduce bias, consider nouns and pronouns as idential part of speech
* No correlation between dates columns and mistranslation probability so we omit these, some correlations are provided below
![date1](https://github.com/WasifKhan/LanguageIO/blob/master/images/date1.png)
![date2](https://github.com/WasifKhan/LanguageIO/blob/master/images/date2.png)
![date3](https://github.com/WasifKhan/LanguageIO/blob/master/images/date3.png)
![date4](https://github.com/WasifKhan/LanguageIO/blob/master/images/date4.png)

## Possible Reasons for Bad Prediction
* Data needs to be split into train/test data. High accuracy is a result of testing on same data model was trained with
* Not enough data points/too many columns. Need to reduce the number of columns or increase the number of datapoints.

## Improvements In Provided Code
* Line 7: Import only what is needed, not entire library
* Line 13, 38: Variable names should be informative, perhaps call this 'numeric_data', 'prediction' respectively
* Line 41: Don't need to map prediction, r2_score function can handle raw input
* Line 42, 47, 54: Use f-strings for printing
* Line 43: Import Lasso directly
* Line 51: Imports should be at beginning of file 

## Next Steps
* Have 1 column "Date Entered" with numeric values that merge all the *date_added_to_system_is_X* columns
* Find correlation between all columns and target output to see which ones are most relevant

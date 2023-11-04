# Analysis


## Data
* POS and Part Of Speech are duplicates, only need 1 of these columns 
* num_words does not belong in this dataset. Also all entries are 1 so doesn't affect result
* Line 30: fillna should be replaced with dropna
* To reduce bias, consider nouns and pronouns as idential part of speech

## Model
* Data needs to be split into train/test data. High accuracy is a result of not splitting data

## Line Specific Comments
* Line 7: Import only what is needed, not entire library
* Line 13, 38: Variable names should be informative, perhaps call this 'numeric_data', 'prediction' respectively
* Line 41: Don't need to map prediction, r2_score function can handle raw input
* Line 42, 47, 54: Use f-strings for printing
* Line 43: Import Lasso directly
* Line 51: Imports should be at beginning of file 


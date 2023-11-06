from pandas import read_csv
from sklearn.model_selection import train_test_split


class DataProcessor:
    x_columns = ['length', 'source_client', 'is stopword', 'part of speech']
    y_column = ['mistranslation probability']
    def __init__(self, filename):
        data = read_csv(filename)
        # self._explore_data(data)
        self._prepare_data(data)
        self._encode_features()
        self._split_data()


    def _explore_data(self, data):
        from matplotlib import pyplot as plt
        from numpy import corrcoef
        target = data['mistranslation probability']
        for col in data:
            if col[0:4] == 'date':
                data[col].replace({'TRUE':1, 'FALSE':0})
                corr = corrcoef(data[col], target)
                plt.title(f'{col}')
                plt.xlabel('Column Value')
                plt.ylabel('Target')
                plt.scatter(data[col], target)
                plt.show()


    def _prepare_data(self, data):
        data = data.filter(DataProcessor.x_columns + DataProcessor.y_column)
        data = data.dropna()
        self.x_data = data.filter(DataProcessor.x_columns)
        self.y_data = data.filter(DataProcessor.y_column)
        self._encode_features()


    def _encode_features(self):
        is_stopword_map = {'TRUE': 1, 'yes': 1, 'FALSE': 0, 'no': 0}
        part_of_speech_map = {'noun': 1, 'pronoun': 1, 'verb': 2, 'adj': 3, \
                'adj.': 3, 'adjective': 3, 'adverb': 4, 'adv': 4, 'adv.': 4}

        self.x_data['is stopword'] = \
                self.x_data['is stopword'].replace(is_stopword_map)
        self.x_data['part of speech'] = \
                self.x_data['part of speech'].replace(part_of_speech_map)


    def _split_data(self):
        self.x_train, self.x_test, self.y_train, self.y_test = \
                train_test_split(self.x_data, self.y_data, test_size=0.4)
                

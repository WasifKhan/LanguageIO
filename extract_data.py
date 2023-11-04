from pandas import read_csv
from sklearn.model_selection import train_test_split

class Extract_Data:
    def __init__(self, endpoint):
        data = read_csv(endpoint)
        self._clean_data(data)


    def _map_data(self, x_data):
        is_stopword_map = {'TRUE': 1, 'yes': 1, 'FALSE': 0, 'no': 0}
        part_of_speech_map = {'noun': 1, 'pronoun': 1, 'verb': 2, 'adj': 3, \
                'adj.': 3, 'adjective': 3, 'adverb': 4, 'adv': 4, 'adv.': 4}

        x_data['is stopword'] = \
                x_data['is stopword'].replace(is_stopword_map)
        x_data['part of speech'] = \
                x_data['part of speech'].replace(part_of_speech_map)
        return x_data


    def _clean_data(self, data):
        x_columns = ['length', 'source_client', 'is stopword', 'part of speech']
        y_column = ['mistranslation probability']

        data = data.filter(x_columns + y_column)
        data = data.dropna()
        x_data = data.filter(x_columns)
        y_data = data.filter(y_column)

        x_data = self._map_data(x_data)

        
        self.x_train, self.x_test, self.y_train, self.y_test = \
                train_test_split(x_data, y_data, test_size=0.3)
                

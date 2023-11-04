from pandas import read_csv

class Extract_Data:
    def __init__(self, endpoint):
        columns = ['length', 'source_client', 'is stopword', 'part of speech', 'mistranslation probability']

        df = read_csv(endpoint)
        df = df.filter(columns)
        df.fillna(0, inplace=True)

        self.x, self.y = df.iloc[:, :-1], df.iloc[:, [-1]]
        print(self.x)
        print(self.y)

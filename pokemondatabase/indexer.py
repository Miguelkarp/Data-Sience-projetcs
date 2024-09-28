import pandas as pd


class DataFrames:
    def __init__(self):
        self.df = None
        self.df_types = None
        self.categories = None

    def datasets(self):
        database = 'pokedexflt.csv'
        types = 'idtypes.csv'
        self.df = pd.read_csv(database, index_col='Number')
        self.categories = [*self.df]
        self.categories.remove(self.categories[2])
        self.categories[1] = 'Type'
        self.df_types = pd.read_csv(types, index_col='ID')
        self.df_types.drop('Unnamed: 0', axis=1, inplace=True)

    def search(self, category):
        while category.lower() not in list(map(str.lower, self.categories)):
            print('Not a valid category, see the list above: ')
            print('Categories are: ', self.categories)
            category = input('Enter a Category: ')
        category = category[0].upper() + category[1:]
        element = input('Enter a %s: ' % category.lower())
        if category == 'Type':
            ids = self.df_types.index[
                    self.df_types['Type'] == element].tolist()
            external_df = self.df.loc[(self.df['Type 1'] == ids[0])]
            external_df_aux = self.df.loc[(self.df['Type 2'] == ids[0])]
            external_df = pd.concat([external_df, external_df_aux])
        elif category in self.categories[-6:]:
            element = float(element)
            external_df = self.df.loc[(self.df[category] >= element)]
        else:
            external_df = self.df.loc[(self.df[category] == element)]
        print(external_df.to_string())


category = input('Enter a Category: ')
data_frames = DataFrames()
data_frames.datasets()
data_frames.search(category)

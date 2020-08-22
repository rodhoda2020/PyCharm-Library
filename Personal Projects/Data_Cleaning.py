import pandas as pd
import numpy as np
import re

df = pd.read_csv(r'C:\Users\Rod Hoda\Documents\PyCharm\BL-Flickr-Images-Book.csv')
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(df.head())

to_drop = ['Edition Statement',
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']

df.drop(to_drop, inplace=True, axis=1)  # Another version of this on line 23
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(df.head())

# # This is another version of removing the elements on the given column.
# df.drop(columns=to_drop, inplace=True)

# removes the row that has the string "Identifier"
# It sets the identifier as the column to be used as the index, instead
# of creating a new index.
df.set_index('Identifier', inplace=True)


def get_citystate(item):
    if ' (' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    # print(df.head())

    # print(df.loc[206])

    # df.loc[1905:, "Date of Publication"].head(10)

    regex = r'^(\d{4})'

    extr = df['Date of Publication'].str.extract(regex, expand=False)
    # print(extr.head())

    df['Date of Publication'] = pd.to_numeric(extr)
    # print(df['Date of Publication'].dtype)

    # print(df['Date of Publication'].isnull().sum() / len(df))

# np.where(condition, then, else)

    # print(df['Place of Publication'].head(10))

    # print(df.loc[4157862])

    pub = df['Place of Publication']
    london = pub.str.contains('London')
    # london[:5]

    oxford = pub.str.contains('Oxford')

    # This prints the first elements of this list

    df['Place of Publication'] = np.where(london, 'London',
                                          np.where(oxford, 'Oxford',
                                                   pub.str.replace('-', ' ')))

    # print(df["Place of Publication"].head())

    # print(df.head())

    university_towns = []
    with open(r'C:\Users\Rod Hoda\Documents\PyCharm\university_towns.txt') as file:
        for line in file:
            if '[edit]' in line:

                state = line

            else:

                university_towns.append((state, line))

    # print(university_towns[:5])

    # This is how you would create a file variable with customized columns from a list.
    towns_df = pd.DataFrame(university_towns, columns=['State', 'RegionName'])

    # print(towns_df.head())
    towns_df = towns_df.applymap(get_citystate)
    print(towns_df.head())



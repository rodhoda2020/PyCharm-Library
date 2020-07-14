import pandas as pd

def Introducing_Pandas_Objects():

    # Let's introduce these three fundamental Pandas data structures:
    # the Series, DataFrame, and Index

    # The Pandas Series Object

    # A Pandas Series is a one-dimenionsional array of indexed data.
    # It can be created from a list of array as follows:
    data = pd.Series([0.25, 0.5, 0.75, 1.0])
    print(data)

    # The Series wraps both a sequence of values and a sequence of indices,
    # which we can access with the values and index attributes.

    # The values are simply a familiar NumPy array:
    print(data.values)

    # The index is an array-like object of type pd.Index, which we'll discuss
    # in more detail momentarily:
    print(data.index)

    # Like with a NumPy array, data can be accessed by the associated index
    # via the familiar Python square-bracket notation:
    print(data[1])

    print(data[1:3])

    # Series as generalized NumPy array

    # The series object appears to be interchangeable with a one-dimensional
    # NumPy array.
    #
    # The essential difference is the presence of the index:
    # while the NumPy array has an implicitly defined integer index used to
    # access the values, the Pandas Series has an explicitly defined index
    # associated with the values

    # This explicit index definition gives the Series object additional
    # capabilities. For example, the index need not be an integer, but can
    # consist of values of any desired type.

    # We can use strings as an index
    data = pd.Series([0.25, 0.5, 0.75, 1.0],
                     index = ['a', 'b', 'c', 'd'])
    print(data)

    print(data['b'])

    # Series as specialized dictionary

    # A dictionary is a structure that maps arbitrary keys to a set of arbitrary
    # values, and a Series is a structure that maps typed keys to a set of typed
    # values.

    # Here, we are constructing a Series object directly from a Python
    # dictionary:
    population_dict = {'California': 38332521,
                       'Texas': 26448193,
                       'New York': 19651127,
                       'Florida': 19552860,
                       'Illinois': 12882135}
    pop = pd.Series(population_dict)
    print(pop)

    # From here, typical dictionary-style item access can be performed:
    print(pop['California'])

    # Unlike a dictionary, though, the Series also supports array-style
    # operations such as slicing:
    print(pop['California':'Illinois'])
    # This will show only the ones written and everything in between

    # Constructing Series objects



if __name__ == "__main__":
    Introducing_Pandas_Objects()
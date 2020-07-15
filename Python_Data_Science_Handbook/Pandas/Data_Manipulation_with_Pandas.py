import pandas as pd
import numpy as np

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

    # We've already seen a few ways of constructing a Pandas Series from scratch;
    # all of them are some version of the following:
    # pd.Series(data, index=index)

    # where index is an optional argument, and data can be one of many entities

    # For example, it can be a list or NumPy array, in which the index defaults
    # to an integer sequence:
    print(pd.Series([2, 4, 6]))

    # Data can be scalar
    pd.Series(5, index=[100, 200, 300])

    # Data can be a dictionary, in which index defaults to the sorted dictionary
    # keys:
    print(pd.Series({2:'a', 1:'b', 3:'c'}))

    # The Pandas DataFrame Object

    # The next fundamental structure is the DataFrame. Like the Series object,
    # the DataFrame can be thought of either as a generalization of a NumPy
    # array, or as a specialization of a Python dictionary.

    # DataFrame as a generalized NumPy array

    # If a series is an analog of a one-dimensional array with flexible indices,
    # a DataFrame is an analog of a two-dimensional array with both flexible
    # row indices and flexible column names.

    # You can think of a DataFrame as a sequence of aligned Series objects.

    # To demonstrate this, let's first construct a new Series
    area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
                 'Florida': 170312, 'Illinois': 149995}

    area = pd.Series(area_dict)
    print(area)

    # Now that we have this and the population series from before, we can use
    # them to construct a single two-dimensional object
    states = pd.DataFrame({'population': pop,
                           'area': area})
    print(states)

    # Like the Series object, the DataFrame has an index attribute that gives
    # access to the index labels:
    print(states.index)

    # Additionally, the DataFrame has a columns attribute, which is an index
    # object holding the column labels:
    print(states.columns)

    # DataFrame as specialized dictionary

    # Similary, we can also think of a DataFrame as a specialization of a
    # dictionary. Where a dictionary maps a key to a value, a DataFrame maps
    # a column name to a Series of column data.

    # For example, asking for the 'area' attribute returns the Series object
    # containing the areas we saw earlier:
    print(states['area'])

    # Notice the potential point of confusion here: in a two-dimensional NumPy
    # array, data[0] will return the first row. For a DataFrame, data['col0']
    # will return the first column.

    # Constructing DataFrame objects

    # A DataFrame can be constructed in a variety of ways:

    # 1. From a single Series object
    pd.DataFrame(pop, columns=['population'])

    # 2. From a list of dicts
    data = [{'a': i, 'b': 2*i}
            for i in range(3)]
    print(pd.DataFrame(data))

    # Even if some keys are missing, Pandas will fill them in with NaN
    pd.DataFrame([{'a': 1, 'b':2}, {'b': 3, 'c': 4}])

    # 3. From a dictionary of Series objects
    pd.DataFrame({'population': pop,
                  'area': area})

    # 4. From a two-dimensional NumPy array.
    example = pd.DataFrame(np.random.rand(3, 2),
                           columns=['foo', 'bar'],
                           index=['a', 'b', 'c'])
    print(example)

    # 5. From a NumPy structured array
    A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])

    print(A.dtype)

    print(pd.DataFrame(A))

    # The Pandas Index Object

    # We have seen here that both the Series and DataFrame objects contain
    # an explicit index that lets you reference and modify data. This index
    # object is an interesting structure in itself, and it can be thought
    # of as immutable array or as an ordered set.

    # Those views have some interesting consequences in the operations available
    # on Index objects. Here is an example:
    ind = pd.Index([2, 3, 5, 7, 11])
    print(ind)

    # Index as immutable array

    # The Index object in many ways operates like an array. For example, we can
    # use Python indexing notation to retrieve values or slices:
    print(ind[1])

    print(ind[::2])

    # Index objects also have many of the attributes familiar from NumPy arrays:
    print(ind.size, ind.shape, ind.ndim, ind.dtype)

    # One difference between Index objects and NumPy arrays is that indices
    # are immutable - that is, they cannot be modified via the normal means:
    # ind[1] = 0    = error

    # Index as ordered set

    # Pandas objects are designed to facilitate operations such as joins across
    # datasets, which depend on many aspects of set arithmetic.

    indA = pd.Index([1, 3, 5, 7, 9])
    indB = pd.Index([2, 3, 5, 7, 11])

    # Intersection
    print(indA & indB)

    # Union
    print(indA | indB)

    # Symmetric difference
    print(indA ^ indB)

    # You can also write these operations via object methods
    indA.intersection(indB)

def Data_Indexing_and_Selection():
    print("Implement!")

if __name__ == "__main__":
    # Introducing_Pandas_Objects()
    Data_Indexing_and_Selection()
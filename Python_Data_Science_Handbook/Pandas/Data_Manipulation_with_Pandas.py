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

    # In the NumPy Unit, we looked in detail at methods and tools to access, set, and modify
    # values in NumPy arrays. These included indexing, slicing, masking, fancy indexing, and
    # combinations thereof. Here, we'll look at similar means of accessing and modifying
    # values in Pandas Series and DataFrame objects.

    # We'll start with the simple case of the one-dimensional Series object, and then move on
    # to the more complicated two-dimensional DataFrame object.

    # DATA SELECTION IN SERIES

    # A series object acts in many ways like a one-dimensional NumPy array,
    # and in many ways like a standard Python dictionary. With these overlapping
    # analogies in mind, we can understand data indexing and selection better

    # Series in dictionary

    data = pd.Series([0.25, 0.5, 0.75, 1.0],
                     index=['a', 'b', 'c', 'd'])
    print(data)

    print(data['b'])

    print('a' in data)
    print(data.keys())
    print(list(data.items()))

    # Series objects can even be modified with a dictionary-like syntax. Just
    # as you can extend a dictionary by assigning to a new key, you can extend
    # a Series by assigning to a new index value
    data['e'] = 1.25
    print(data)

    # Series as a one-dimensional array

    # A Series builds on this dictionary-like interface and provides array-style
    # item selection via the same basic mechanisms as NumPy arrays - that is,
    # slices, masking, and fancy indexing. Example of these are as follows:

    # Slicing by explicit index
    print(data['a':'c'])

    # Slicing by implicit integer index
    print(data[0:2])

    # Masking
    print(data[(data > 0.3) & (data < 0.8)])

    # Fancy indexing
    print(data[['a', 'e']])

    # Among these, slicing may be the most confusing. Notice that when you are
    # slicing with an explicit index (in line 265), the final index is included
    # in the slice, while when you're slicing with an implicit index (in line
    # 268) the final index is excluded from the slice

    # Indexers: loc, iloc, and ix

    # The loc attribute allows indexing and slicing that always reference the
    # explicit index:

    data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
    print(data.loc[1])

    print(data.loc[1:3])

    # The iloc attribute allows indexing and slicing that always references the
    # implicit Python-style index:
    print(data.iloc[1])

    print(data.iloc[1:3])

    # The third indexing attribute, ix, is a hybrid of the two, and for Series
    # objects is equivalent to standard []-based indexing. The purpose of the ix
    # indexer will become more apparent in the context of DataFrame objects.

    # One guiding principle of Python code is that 'explicit is better than
    # implicit.' The explicit nature of loc and iloc make them very useful in
    # maintaining clean and readable code; especially in the case of integer
    # indexes.

    # DATA SELECTION IN DATAFRAME

    # Recall that a DataFrame acts in many ways like a two-dimensional or
    # structured array, and in other ways like a dictionary of Series structures
    # sharing the same index

    # DataFrame as a dictionary

    # The first analogy we will consider is the DataFrame as a dictionary
    # of related Series objects

    area = pd.Series({'California': 423967, 'Texas': 695662,
                      'New York': 141297, 'Florida': 170312,
                      'Illinois': 149995})
    pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                     'New York': 19651127, 'Florida': 19552860,
                     'Illinois': 12882135})

    data = pd.DataFrame({'area': area, 'pop': pop})
    print(data)

    # The individual Series that make up the columns of the DataFrame can be
    # accessed via dictionary-style indexing of the column name:
    print(data['area'])

    # Equivalently, we can use attribute-style access with column names that
    # are strings:
    print(data.area)

    # If the column names are not strings, or if the column names conflict with
    # methods of the DataFrame, however, this attribute-style access is not
    # possible

    # The dictionary-style syntax can also be used to modify the object:
    data['density'] = data['pop'] / data['area']
    print(data)

    # DataFrame as two-dimensional array

    print(data.values)

    # With this picture in mind, we can do many familiar array-like observations
    # on the DataFrame itself. For example, we can transpose the full DataFrame
    # to swap rows and columns:

    print(data.T)

    # When it comes to indexing of DataFrame objects, however, it is clear that
    # the dictionary-style indexing of columns precludes our ability to simply
    # treat it as a NumPy array. In particular, passing a single index to an
    # array accesses a row:
    print(data.values[0])

    # and passing a single 'index' to a DataFrame accesses a column:
    print(data['area'])

    # Thus, for array-style indexing, we need another convention. Here Pandas
    # again uses the loc, iloc, ix indexers mentioned earlier. Using the iloc
    # indexer, we can index the underlying array as if it is a simple NumPy
    # array (using the implicit Python-style index), but the DataFrame is
    # maintained:
    print(data.iloc[:3, :2])

    print(data.loc[:'Illinois', :'pop'])

    # The ix indexer allows a hybrid of these two approaches:
    # Generally don't use it since the ix does not exist
    # print(data.ix[:3, :'pop'])

    print(data.loc[data.density > 100, ['pop', 'density']])

    # Any of these indexing conventions may also be used to set or modify
    # values
    data.iloc[0, 2] = 90

    print(data)

    # Additional indexing conventions

    # While indexing refers to columns, slicing refers to rows:
    print(data['Florida': 'Illinois'])

    # Such slices can also refer to rows by number rather than by index:
    print(data[1:3])

    # Similarly, direct masking operations are also interpreted row-wise rather
    # than column-wise:
    print(data[data.density > 100])

def Operating_on_Data_in_Pandas():
    print("Implement!")

if __name__ == "__main__":
    # Introducing_Pandas_Objects()
    # Data_Indexing_and_Selection()
    Operating_on_Data_in_Pandas()
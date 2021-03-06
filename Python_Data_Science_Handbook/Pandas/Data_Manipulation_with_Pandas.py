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

    # One of the essential pieces of NumPy is the ability to perform quick
    # element-wise operations. Pandas inherits much of this functionality from
    # NumPy, and the ufuncs that we introduced in NumPy's "Computation on NumPy
    # Arrays: Universal Functions" are key to this.

    # Pandas includes a couple useful twists, however: for unary operations
    # like negation and trig functions, these ufuncs will preserve index and
    # column labels in the output, and for binary operations such as addition
    # and multiplication, Pandas will automatically align indices when passing
    # the objects to the ufunc.

    # This means that keeping the context of data and combining data from
    # different sources become essentially foolproof ones with Pandas.

    # We will additionally see that there well-defined operations between
    # one-dimensional Series structures and two-dimensional DataFrame structures.

    # UFUNCS: INDEX PRESERVATION

    # Because Pandas is designed to work with NumPy, any NumPy ufunc will work
    # on Series and DataFrame objects. Let's demonstrate:

    rng = np.random.RandomState(42)
    print(rng)

    ser = pd.Series(rng.randint(0, 10, 4))
    print(ser)

    df = pd.DataFrame(rng.randint(0, 10, (3, 4)),
                      columns=['A', 'B', 'C', 'D'])
    print(df)


    # If we apply a NumPy ufunc on either of these objects, the result will be
    # another Pandas object with the indices preserved:
    print(np.exp(ser))

    # For a slightly more complext calculation:
    print(np.sin(df * np.pi / 4))

    # UFUNCS: INDEX ALIGNMENT

    # For binary operations on two Series or DataFrame objects, Pandas will align
    # indices in the process of performing the operation. This is very convenient
    # when you are working with incomplete data.

    # Index alignment in Series

    area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                      'California': 423967}, name='area')
    pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                            'New York': 19651127}, name='population')

    print(pop / area)

    # The resulting array contains the union of indices of the two input arrays,
    # which we could determine using standard Python set arithmetic on these
    # indices:
    print(area.index | pop.index)

    # Any missing values are filled in with NaN by default:

    A = pd.Series([2, 4, 6], index=[0, 1, 2])
    B = pd.Series([1, 3, 5], index=[1, 2, 3])

    print(A+B)

    # If using NaN values is not the desired behavior, we can modify the fill
    # value using appropriate object methods in place of the operators. For
    # example, calling A.add(B) is equivalent to calling A + B, but allows
    # optional explicit specification of the fill value for any elements in A
    # or B that might be missing:
    print(A.add(B, fill_value=0))

    # Index alignment in DataFrame

    # A similar type of alignment takes place for both columns and indices when
    # you are performing operations on DataFrames:
    A = pd.DataFrame(rng.randint(0, 20, (2, 2)),
                     columns=list('AB'))
    print(A)

    B = pd.DataFrame(rng.randint(0, 10, (3, 3)),
                     columns=list('BAC'))
    print(B)

    print(A+B)

    # Notice that indices are aligned correctly irrespective of their order in
    # the two objects, and indices in the result are sorted.

    # Fill_value for DataFrame (Note: Here we'll fill with the mean of all values
    # in A (which we compute by first stacking the rows of A)):
    fill = A.stack().mean()
    print(fill)

    print(A.add(B, fill_value=fill))

    # UFUNCS: OPERATIONS BETWEEN DATAFRAME AND SERIES

    # When you are performing operations between a DataFrame and a Series, and
    # index and column alignment is similarly maintained. Operations between a
    # DataFrame and a Series are similar to operations between a two-dimen. and
    # one-dimen. NumPy array.

    A = rng.randint(10, size=(3, 4))
    print(A)

    print(A[0])
    print(A-A[0])

    # In Pandas, the conventions similarly operates row-wise by default:
    df = pd.DataFrame(A, columns=list("QRST"))
    print(df)

    print(df - df.iloc[0])

    print(df.iloc[0])

    print('\n')
    # If you would like to operate column-wise, you can use the object methods
    # mentioned earlier, while specifying the axis keyword:
    print(df.subtract(df['R'], axis=0))

    # Note that these DataFrame/Series operations will automatically align
    # indices between the two elements:
    halfrow = df.iloc[0, ::2]
    print(halfrow)

    print(df - halfrow)

    # This preservation and alignment of indices and columns means that
    # operations on data in Pandas will always maintain the data context, which
    # prevents the types of silly errors that might come up when you are working
    # with heterogeneous and/or misaligned data in raw NumPy array.

def Handling_Missing_Data():

    # In this section, we wil discuss some general considerations for missing
    # data, discuss how Pandas chooses to represent it, and demonstrate some
    # built-in Pandas tools for handling missing data in Python. Here and
    # throughout the book, we'll refer to missing data in general as null,
    # NaN, or NA values

    # TRADE-OFFS IN MISSING DATA CONVENTIONS

    # Generally, there are two strategies to indicating the presence of missing
    # data in a table or DataFrame: using mask that globally indicates missing
    # values, or choosing a sentinel values that indicates a missing entry.

    # In the masking approach, the mask might be an entirely separate Boolean
    # array, or it may involve appropriation of one bit in the data representation
    # to locally indicate the null status of a value.

    # In the sentinel approach, the sentinel value could be some data-specific
    # convention, such as indicating a missing integer value with -9999 or some
    # rare bit pattern, or it could be a more global convention, such as
    # indicating a missing floating-point value with NaN (Not a Number).

    # MISSING DATA IN PANDAS

    # Pandas chose to use sentinels for missing data, and further chose to use
    # two already-existing Python null values: the special floating point NaN
    # value, and the Python none object.

    # None: Pythonic missing data

    # The first sentinel value used by Pandas is None, a Python singleton object
    # that is often used for missing data in Python code. Because None is a
    # Python object, it cannot be used in any arbitrary NumPy/Pandas array,
    # but only in arrays with data type 'object'.
    vals1 = np.array([1, None, 3, 4])
    print(vals1.dtype)

    # The use of Python objects in an array also means that if you perform
    # aggregations like sum() or min() across an array with a None value, you
    # generally will get an error.

    # NaN: Missing numerical data

    # The other missing data representation, NaN, is different: it is a special
    # floating-point value recognized by all systems that use the standard IEEE
    # floating-point representation:
    vals2 = np.array([1, np.nan, 3, 4])
    print(vals2.dtype)

    # You should be aware that NaN is a bit like a virus data-it infects any
    # other compiled it touches. Regardless of the operation, the result of
    # arithmetic with NaN will be another NaN:
    print(1 + np.nan)

    # Note that this means that aggregates over the values are well defined
    # (they don't result in an error) but not always useful:
    print(vals2.sum())

    # NumPy does provide some special aggregations that will ignore these missing
    # values:
    print(np.nansum(vals2))

    # Keep in mind that NaN is specifically a floating-point value; there is no
    # equivalent NaN value for integers, strings, or other types.

    # NaN and None in Pandas

    print(pd.Series([1, np.nan, 2, None]))

    # For types that don't have an available sentinel value, Pandas automatically
    # type-csts when NA values are present. If we set a value in an integer array
    # to np.nan, it will automatically be upcast to a floating point type
    x = pd.Series(range(2), dtype=int)
    print(x)

    x[0] = None
    print(x)

    # OPERATING ON NULL VALUES

    # There are several useful methods for detecting, removing, and replacing null
    # values in Pandas data structures. They are:
    # pd.isnull()     # Generate a Boolean mask indicating missing values
    # pd.notnull()    # Opposite of isnull()
    # pd.dropna()     # Return a filtered version of the data
    # pd.fillna()     # Return a copy of the data with missing values filled or imputed

    # Detecting null values
    # Pandas data structures have two useful methods for detecting null data: isnull()
    # notnull(). Either one will return a Boolean mask over the data. For example:
    data = pd.Series([1, np.nan, 'hello', None])
    print(data.isnull())

    # Boolean masks can be used directly as a Series or DataFrame index:
    print(data[data.notnull()])

    # Dropping null values

    # dropna() (which removes NA values) and fillna() (which fills in NA values).
    print(data.dropna())

    # For the DataFrame, there are more options.
    df = pd.DataFrame([[1, np.nan, 2],
                       [2, 3, 5],
                       [np.nan, 4, 6]])
    print(df)

    # We cannot drop single values from a DataFrame; we can only drop full rows
    # or full columns.

    # By default, dropna() will drop all rows in which any null values is present:
    print(df.dropna())

    # You can drop NA values along a different axis: axis=1 drops all columns
    # containing a null value:
    print(df.dropna(axis='columns'))

    # This drops some good data as well; you might rather be interested in dropping
    # rows or columns with all NA values, or a majority of NA values. This can be
    # specified through the 'how' or 'thresh' parameters

    # You can also specify how='all', which will only drop rows/columns that are
    # null values"
    df[3] = np.nan
    print(df)

    print(df.dropna(axis='columns', how='all'))

    # Thresh = threshold
    # The thresh parameter lets you specify a minimum number of non-null values for the
    # row/column to be kept:
    print(df.dropna(axis='rows', thresh=3))

    # Filling null values

    # You might wanna replace the NA values with  a single number like zero, or it might
    # be some sort of imputation or interpolation from the good values. You could do this
    # in-place using the isnull() method as a mask, but because it is such a common
    # operation Pandas providing the fillna() method, which returns a copy of the array
    # with the null values replaced.

    data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
    print(data)

    # We can fill NA entries with a single value, such as zero:
    print(data.fillna(0))

    # We can specify a forward-fill to propagate the previous value forward:
    print(data.fillna(method='ffill'))

    # Or a back-fill:
    print(data.fillna(method='bfill'))

    # For DataFrames, the options are similar, but we can also specify an axis along
    # which the fills take place:
    print(df)

    # Note: axis=1 is columns, axis=0 is rows (which is default)
    print(df.fillna(method='ffill', axis=1))

def Hierarchical_Indexing():
    # A common pattern in practice for handling three-dimensional and four-dimensional
    # data is to make use of hierarchical indexing (also known as multi-indexing) to
    # incorporate multiple index levels within a single index.

    # A MULTIPLY INDEXED SERIES

    # Let's start by considering how we  might represent two-dimensional data within a
    # one-dimensional Series.

    # The bad way

    index = [('California', 2000), ('California', 2010),
             ('New York', 2000), ('New York', 2010),
             ('Texas', 2000), ('Texas', 2010)]
    pop = [33871648, 37253956,
           18976457, 19378102,
           20851820, 25145561]
    population = pd.Series(pop, index=index)
    print(population)

    # With this indexing scheme, you can straightforwardly index or slice the series
    # based on this multiple index:
    print(population[('California', 2010):('Texas', 2000)])

    # But if you need to select all values from 2010, you'll need to do some messy
    # munging to make it happen:
    print(population[[i for i in population.index if i[1] == 2010]])
    # This is not clean or efficient

    # The better way: Pandas MultiIndex

    # Fortunately, Pandas provides a better way. Our tuple-based indexing is
    # essentially a rudimentary multi-index, and the Pandas MultiIndex type
    # gives us the type of operations we wish to have.
    index = pd.MultiIndex.from_tuples(index)
    print(index)

    # If we reindex our series with this MultiIndex, we see the hierarchical
    # representation of the data:
    pop = population.reindex(index)
    print(pop)

    # Now to access all data for which the second index is 2010, we can simply
    # use the Pandas slicing notation:
    print(pop[:, 2010])

    # MultiIndex as extra dimension

    # You might have noticed something else here: we could easily have stored the
    # the same data using a simple DataFrame with index and column labels.
    # The unstack() method will quickly convert a multiply-indexed Series into a
    # conventionally indexed DataFrame:
    pop_df = pop.unstack()
    print(pop_df)

    # The stack() method provides the opposite operation:
    print(pop_df.stack())

    # You might wonder why would we bother with hierarchical indexing. The reason is
    # simple: just as we were able to use multi-indexing to represent two-dimensional
    # data within a one-dimensional Series, we can also use it to represent data of
    # three or more dimensions in a Series or DataFrame.

    

if __name__ == "__main__":
    # Introducing_Pandas_Objects()
    # Data_Indexing_and_Selection()
    # Operating_on_Data_in_Pandas()
    # Handling_Missing_Data()
    Hierarchical_Indexing()
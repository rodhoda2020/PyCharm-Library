import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

def Fixed_Type_Array_in_Python():

    # This was the traditional way of writing arrays
    import array
    L = list(range(10))
    A = array.array('i', L)
    print(A)
    # 'i' is to indicate the contents are integers.

def Creating_Arrays_from_Python_Lists():

    # This is an integer array using numpy
    print(np.array([1, 4, 2, 5, 3]))

    # Numpy is constrained to arrays that all contain the same type.
    # If types do not match, NumPy will upcast if possible

    # Example, integer array changed to float array
    print(np.array([3.14, 4, 2, 3]))

    # If you wanted to explicitly set the data type
    print(np.array([1, 2, 3, 4], dtype='float32'))

    # This is something Python cannot do while NumPy can
    # It is that Numpy can create arrays that are multidimensional

    # Here is one way:
    print(np.array([range(i, i+3) for i in [2, 4, 6]]))
    # This is due to nested lists. The inner lists are treated as rows of the resulting
    # two-dimensional array.

def Creating_Arrays_from_Scratch():
    # It is more efficient to create arrays from scratch

    # This creates a length-10 integer array filled with zeros:
    np.zeros(10, dtype=int)

    # This creates a 3x5 floating-point array filled with ones
    np.ones((3, 5), dtype=float)

    # This creates a 3x5 array filled with 3.14
    np.full((3, 5), 3.14)

    # This creates an array filed with a linear sequence
    # Starting at 0, ending at 20, stepping by 2
    np.arange(0, 20, 2)

    # Creates an array of five values evenly spaced between 0 and 1
    np.linspace(0, 1, 5)

    # Creates a 3x3 array of uniformly distributed
    # random values between 0 and 1
    np.random.random((3, 3))

    # Creates a 3x3 array of normally distributed random values
    # with mean 0 and standard deviation 1
    np.random.normal(0, 1, (3, 3))

    # Creates a 3x3 array of random integers in the interval [0, 10)
    np.random.randint(0, 10, (3, 3))

    # Creates a 3x3 identity matrix
    np.eye(3)

    # Creates an uninitialized array of three integers
    # The values will be whatever happens to already exist at that
    # memory location
    np.empty(3)

def The_Basics_of_NumPy_Arrays():

    # There are the categories of basic array manipulation that will be shown in the following
    # functions.

    # Attributes of arrays: Determining the size, shape, memory consumption,
    # and data types of arrays

    # Indexing of arrays: Getting and setting the value of individual array elements.

    #Slicing of arrays: Getting and setting smaller subarrays within a larger array.

    # Reshaping of arrays: changing the shape of a given array

    # Joining and splitting of arrays: Combining multiple arrays into one, and splitting one
    # array into many

    print("Go to the next function for code")

def NumPy_Array_Atributes():

    # We are going to create three random arrays: one-dimensional, two-dimensional, and three
    # three-dimensional.
    # We'll use NumPy's random number generator, which we willl seed with a set value in
    # order to ensure that the same random arrays are generated each time this code is run:
    np.random.seed(0)

    x1 = np.random.randint(10, size=6)
    x2 = np.random.randint(10, size=(3, 4))
    x3 = np.random.randint(10, size=(3, 4, 5))

    # Each array has attributes ndim(the number of dimensions), shape(the size of each
    # dimension), and size(the total size of the array):
    print("x3 ndim: ", x3.ndim)
    print("x3 shape: ", x3.shape)
    print("x3 size: ", x3.size)

    print(x1.ndim)

    print("x3 ndim: ", x2.ndim)
    print("x3 shape: ", x2.shape)
    print("x3 size: ", x2.size)

    # This attribute is for the data type of the array
    print("dtype: ", x3.dtype)

    # Itemsize, which lists the size (in bytes) of each array element, and nbytes, which
    # lists the total size (in bytes) of the array:
    print("itemsize: ", x3.itemsize, "bytes")
    print("nbytes", x3.nbytes, "bytes")

def Array_Indexing_Accessing_Single_Elements():

    x1 = np.random.randint(0, 10, (3, 3))
    # print(x1)

    x2 = np.random.randint(0, 10, (3, 4))
    # print(x2)

    x3 = np.random.randint(0, 10, (1, 6))

    # In a one-dimensional array, you can access the i'th value by specifying the desired
    # index in square brackets

    # This is how you print the single first element in the array with NumPy
    print(x3[0, 0])

    print("x2 = ", x2)

    # This is for a whole row
    print(x2[0])

    # This is for a single element
    print(x2[2, 3])

    # You can also modify the values corresponding to the index notation
    x2[0, 0] = 123
    print(x2)

    # NumPy arrays have fixed types. This means you can not add a floating-point value
    # to an int array. It will change the value to the correct data type if possible
    x2[0, 0] = 3.14
    print(x2)

def Array_Slicing_Accessing_Subarrays():

    # One-dimensional subarrays
    x = np.arange(10)
    # print(x)

    # First five elements
    # print(x[:5])

    # Elements after index 5
    # print(x[5:])

    # Middle subarray
    # print(x[4:7])

    # Every other element
    # print(x[::2])

    # Every other element start at index 1
    # print(x[1::2])

    # All elements reversed
    # print(x[::-1])

    # Reversed every other from index 5
    # print(x[5::-2])

    # Multi-dimentional subarrays

    x2 = np.random.randint(0, 10, (3, 4))
    print(x2)

    # two rows, three columns
    print(x2[:2, :3])

    # All rows, every other column
    print(x2[:3, ::2])

    # Subarray dimensions can even be reversed together
    print(x2[::-1, ::-1])

    # One commonly needed routine is accessing single rows or columns of an array.
    # You do this by combining indexing and slicing

    # First column
    print(x2[:, 0])

    # First row
    print(x2[0, :])

    # Another way of getting the first row
    print(x2[0])

    # One important thing to know about array slices is that they return view rather
    # than copies of the array data. This is one area in which NumPy array slicing
    # from Python list slicing: in lists, slices will be copies

    # Let's extract 2x2 subarray from this
    x2_sub = x2[:2, :2]
    print(x2_sub)

    # Now if we modify this subarray, we'll see that the original array is changed as well.
    x2_sub[0,0] = 99
    print(x2_sub)

    print(x2)
    # This is useful because when we work with large datasets, we can access and process
    # pieces of these datasets without the need to copy the underlying data buffer.

    # Creating copies of arrays
    # We can copy the data within an array by using the copy() method

    x2_sub_copy = x2[:2, :2].copy()
    print(x2_sub_copy)

    x2_sub_copy[0, 1] = 441
    print(x2_sub_copy)

    print(x2)

def Reshaping_of_Arrays():

    # By using the reshape() method, you can put the numbers 1 through 9 in a 3x3 grid like this:
    grid = np.arange(1, 10).reshape((3, 3))
    print(grid)
    # Note: The size of the initial array must match the size of the reshaped array.

    # Another common reshaping pattern is the conversion of a one-dimensional array into
    # a two-dimensional row or column matrix.

    x = np.array([1, 2, 3])

    # Row vector via reshape
    print(x.reshape((1, 3)))
    print(x)

    # Row vector via newaxis
    print(x[np.newaxis, :])

    # Column vector via reshape
    print(x.reshape((3, 1)))

    #Column vector via newaxis
    print(x[:, np.newaxis])

def Array_Concatenation_and_Splitting():

    # Concatenation, or joining of two arrays in NumPy, is accomplished through
    # the routines np.concatenate, np.vstack, and np.hstack.

    # This is np.concatenate:
    x = np.array([1, 2, 3])
    y = np.array([3, 2, 1])

    print(np.concatenate([x, y]))

    z = [99, 99, 99]

    print(np.concatenate([x, y, z]))

    # np.concatenate used for two-dimensional arrays:
    grid = np.array([[1, 2, 3], [4, 5, 6]])

    print(np.concatenate([grid, grid]))

    # concatenate along the second axis (zero-indexed)
    print(np.concatenate([grid, grid], axis=1))

    # When working with arrays of mixed dimensions, it can be clearer to use the
    # np.vstack (vertical stack) and np.hstack(horizontal stack) functions:
    x = np.array([1, 2, 3])
    grid = np.array([[9, 8, 7], [6, 5, 4]])

    print(np.vstack([x, grid]))

    # Horizontally stack the arrays
    y = np.array([[99],
                 [99]])
    print(np.hstack([grid, y]))

    # Note: When using vstack, both arrays must have the same number of columns.
    #       For hstacks, they must have the same number of rows.

    # np.dstack will stack arrays along the third axis

    # Splitting of arrays
    # The opposite of concatenation is splitting, which is implemented by the functions
    # np.split, np.hsplit, np.vsplit.

    x = [1, 2, 3, 99, 99, 3, 2, 1]
    x1, x2, x3 = np.split(x, [3, 5])
    print(x1, x2, x3)

    grid = np.arange(16).reshape((4, 4))
    print(grid)

    # This is how the vsplit works. The 2 is the number of rows that will be placed per array
    upper, lower = np.vsplit(grid, [2])
    print(upper)
    print(lower)

    # This is how the hsplit works. The 2 is the number of columsn that will be placed per array
    left, right = np.hsplit(grid, [2])
    print(left)
    print(right)

    # np.dsplit will split arrays along the third axis.

def Computation_on_NumPy_Arrays_Universal_Functions():

    # The relative sluggishness of Python generally manifests itself in situations
    # where many small operations are being repeated - for instance, looping over
    # arrays to operations on each element

    # A straightforward approach might look like this
    np.random.seed(0)

    def compute_reciprocals(values):
        output = np.empty(len(values))
        for i in range(len(values)):
            output[i] = 1.0 / values[i]
        return output

    values = np.random.randint(1, 10, size=5)
    print(values)
    print(compute_reciprocals(values))

    # It turns out that the bottleneck here is not the operations themselves, but the
    # type-checking and function dispatches that CPython must do at each cycle of the
    # loop. Each time the reciprocal is computed, Python first examines the object’s
    # type and does a dynamic lookup of the correct function to use for that type.

    # If we were working in compiled code instead, this type specification would be
    # known before the code executes and the result could be computed much more efficiently

    # Numpy provides a convenient interface into just this kind of statically typed,
    # compiled routine. This is known as vectorized operation.

    # The NumPy version is much quicker at compiling the code
    print(1.0 / values)

    # Vectorized operations in NumPy are implemented via ufuncs, whose main purpose is
    # to quickly execute repeated operations on values in NumPy arrays

    # two arrays:
    print(np.arange(5) / np.arange(1, 6))

    # Multidimensional arrays:
    x = np.arange(9).reshape(3, 3)
    print(x**2)

    # Array Arithmetic

    x = np.arange(4)
    print("x =", x)
    print("x+5 =", x+5)
    print("x//2 =", x // 2)

    print(-(0.5*x + 1) ** 2)

    # Arithmetic Operators
    np.add(x, 2)

    # Table:
    np.add()              # Addition
    np.subtract()         # Subtraction
    np.negative()         # Unary Negation
    np.multiply()        # Multiplication
    np.divide()           # Division
    np.floor_divide()     # Floor division (e.g., 3 // 2 = 1)
    np.power()            # Exponentiation
    np.mod()              # Modulus/remainder

    # Absolute value:
    x = np.array([-2, -1, 0, 1, 2])
    print(abs(x))

    # The corresponding ufunc is np.absolute()

    # Trigonometric functions
    theta = np.linspace(0, np.pi, 3)

    print("theta =", theta)
    print("sin(theta) =", np.sin(theta))
    print("arcsin(theta) =", np.arcsin(theta))
    # Same goes for all other functions

    # Exponents and Logarithms
    x = [1, 2, 3]
    print("e^x =", np.exp(x))
    print("2^x =", np.exp2(x))
    print("3^x =", np.exp(3, x))

    print("\nln(x) =", np.log(x))
    print("log2(x) =", np.log2(x))

    print("exp(x) - 1 =", np.expm1(x))
    print("log(1+x) =", np.log1p(x))

    # You can find specialized ufuncs for complicated mathematical functions, go to
    # scipy.special, which like NumPy, has many more ufuncs that it  provides for any
    # obscure calculation

def Advanced_Ufunc_Features():

    # For large calculations, it is sometimes useful to be able to specify the array where the
    # result of the calculation will be stored
    x = np.arange(5)
    y = np.arange(5)
    np.multiply(x, 10, out=y)
    print(y)

    y = np.zeros(10)
    np.power(2, x, out=y[::2])
    print(y)

    # This practice is so that with large calculations, you save memory when it is stored
    # in an array.

    # Aggregates

    # Reduce aggregate
    x = np.arange(1, 6)
    print(x)
    print(np.add.reduce(x))

    print(np.multiply.reduce(x))

    # If we’d like to store all the intermediate results of the computation, we can instead use
    # accumulate:

    print(np.add.accumulate(x))

    # Outer products

    # Any ufuncs can compute the output of all pairs of two different inputs using the
    # the outer method

    x = np.arange(1, 6)
    print(np.multiply.outer(x, x))

def Aggregation_Min_Max_and_Everything_in_Between():

    # Often when you are faced with a large amount of data, a first step is to compute sum‐
    # mary statistics for the data in question

    # Summing the values in an array

    # Built-in Python sum function:
    L = np.random.random(100)
    print(L)
    print(sum(L))

    # NumPy version:
    print(np.sum(L))

    # The NumPy version executes the operation in compiled code, which is much more quicker

    # Minimum and Maximum

    # Built-in Python max/min functions:
    min(L), max(L)

    # NumPy's version:
    np.min(L), np.max(L)

    # A shorter syntax is to use methods of the array objec itself:
    L.min(), L.max(), L.sum()

    # Multidimensional aggregates
    M = np.random.random((3, 4))
    print(M)

    print(M.sum())
    print(M.max(axis=1))
    print(M.min(axis=0))

    # Aggregation functions

    # Additionally, most aggregates have a NaN-safe counterpart that computes
    # the result while ignoring missing values, which are marked by the special IEEE
    # floating-point NaN value.
    np.sum(),         np.nansum()           # Compute sum of elements
    np.prod(),        np.nanprod()          # Compute product of elements
    np.mean(),        np.nanmean()          # Computer mean of elements
    np.std(),         np.nanstd()           # Computer standard deviation
    np.var(),         np.nanvar()           # Compute variance
    np.min(),         np.nanmin()           # Compute min value
    np.max(),         np.nanmax()           # Compute max value
    np.argmin(),      np.nanargmin()        # Compute index of min value
    np.argmax(),      np.nanargmax()        # Compute index of max value
    np.median(),      np.nanmedian()        # Compute median of elements
    np.percentile,    np.nanpercentile()    # Compute rank-based statistics of elements
    np.any(),                               # Evalute whether any elements are true
    np.all(),                               # Evaluate whether all elements are true

def What_Is_the_Average_Height_of_US_Presidents():  # Exercise example

    df = pd.read_csv('president_heights.csv.txt')
    # print(df)

    # If the file is in another location:
    # df = pd.read_csv(r'C:\Users\rodho\OneDrive\Documents\Projects\venv\Python_Data_Science_Handbook/president_heights.csv.txt')
    # print(df)

    df.set_index("order", inplace=True)
    # print(df)

    heights = np.array(df['height(cm)'])
    print(heights)

    print(df)
    print("mean: ", heights.mean())
    print("Standard Deviation ", heights.std())
    print("Minimum height: ", heights.min())
    print("Maximum height: ", heights.max())
    x = heights.argmin() + 1

    print("The shortest President: \n", df.loc[x])

    # Visual representation of this data using Matplotlib

    plt.hist(heights) # This is how to write a histogram graph
    plt.title('Height Distribution of US Presidents')
    plt.xlabel('heights(cm)')
    plt.ylabel('number');
    plt.show()

def Computation_on_Arrays_Broadcasting():

    # Another means of vectorization operations is to use NumPy's broadcasting
    # functionality. Broadcasting is simply a set of rules of applying binary ufuncs
    # (addition, subtraction, multiplication, etc.) on arrays of different sizes

    # Binary operations are performed on an element-by-element basis:
    a = np.array([0, 1, 2])
    b = np.array([3, 4, 5])

    print(a+b)

    # Broadcasting allows these types of binary operations on arrays of different sizes

    # Adding a scalar (zero-dimensional array) to an array:
    print(a+5)

    # We can similarly extend this to arrays of higher dimensions:
    M = np.ones((3, 3))
    print(M)

    print(M + a)

    a = np.arange(3)
    b = np.arange(3)[:, np.newaxis] # Prints in vertical direction

    print(a)
    print(b)

    print(a+b)

    # Rules of Broadcasting

    # Broadcasting in NumPy follows a strict set of rules to determine the interaction between the two arrays.

    # Rule 1: If the two arrays differ in their number of dimensions, the shape of the one with the fewer
    #         dimensions is padded with ones on its leading (left) side.

    # Broadcasting example 1:
    M = np.ones((2, 4))
    a = np.arange(4)

    print(M)
    print(a)

    M.shape = (2, 4)
    a.shape = (4,)

    print(M+a)

    # Rule 2: If the shape of the two arrays does not match in any dimension, the array with shape equal to 1
    # in that dimension is stretched to match the other shape.

    # Broadcasting example 2:
    a = np.arange(3).reshape((3, 1))
    b = np.arange(3)

    print(a)

    a.shape = (3, 1)
    b.shape = (3,)


    print(a + b)

    # Rule 3: If in any dimension the sizes disagree and neither is equal to 1, an error is raised.

    # Broadcasting example 3:

    # Two arrays that are not compatible
    M = np.ones((3, 2))
    a = np.arange(3)

    M.shape = (3, 2)
    a.shape = (3,)

    # This would cause us to get an error.
    #  M + a

def Broadcasting_in_Practice():

    # Centering an array

    X = np.random.random((10, 3))
    print(X)

    Xmean = X.mean(0)
    print(Xmean)

    X_centered = X - Xmean

    print(X_centered.mean(0))

    print(X_centered)

    # Plotting a two-dimensional function

    # One place that broadcasting is very useful is in displaying images based on two-dimensional functions
    # If we want to define a function z=f(x,y), broadcasting can be used to compute the function across the grid:
    x = np.linspace(0, 5, 50)
    y = np.linspace(0, 5, 50)[:, np.newaxis]

    print(x), print(y)

    z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

    plt.imshow(z, origin="lower", extent=[0, 5, 0, 5], cmap='viridis')
    plt.colorbar()
    print(plt.show())

def Comparisons_Masks_and_Boolean_Logic(): # Example Included

    # Example: Counting Rainy Days

    # Imagine you have a series of data that represents the amount of precipitation
    # each day for a year in a given city. Here we'll load the daily rainfall
    # statistics for the city of Seattle.

    # We are extracting the column that includes the precipitation
    rainfall = pd.read_csv(r'Seattle2014.csv')["PRCP"].values
    inches = rainfall / 254
    print(inches.shape)
    plt.hist(inches, 40)

    plt.ylabel('inches')
    # print(plt.show())

    # Digging into the data

    # One approach to this would be to answer these questions by hand: loop through
    # the data, incrementing a counter each time we see values in some desired range.
    # This approach is inefficient. NumPy's ufuncs are a better substitute in place
    # of loops.

    # Comparison Operators as ufuncs

    x = np.array([1, 2, 3, 4, 5])
    print(x < 3)
    print(x > 3)
    print(x <= 3)
    print((2*x) == (x**2))

    # ==        np.equal
    # !=        np.not_equal
    # <         np.less
    # <=        np.less_equal
    # >         np.greater
    # >=        np.greater_equal

    rng = np.random.RandomState(0)
    print(rng)

    x = rng.randint(10, size=(3, 4))
    print(x)

    print(x < 6) # The result is a boolean array

    # Working with Boolean Arrays

    # Counting entries

    print(np.count_nonzero( x < 6))

    # How many values less than 6
    print(np.sum(x < 6))

    # How many values less than 6 in each row
    print(np.sum(x < 6, axis=1))

    # Are there any values greater than 8
    np.any(x > 8)

    # Are all values less than 10
    np.all(x < 10)

    # Are all values equal to 6
    np.all(x == 6)

    # Back to the example
    # How about if we wanted to know about days with rain less than four inches and greater than one inch
    print(np.sum((inches > 0.5) & (inches < 1)))

    # There are 29 days with rainfall between 0.5 and 1 inches.

    print(np.sum(~( (inches <= 0.5) | (inches >= 1))))

    print("Number days without rain: ", np.sum(inches == 0))
    print("Number of days with rain: ", np.sum(inches != 0))
    print("Days with more than 0.5 inches: ", np.sum(inches > 0.5))
    print("Rainy days with < 0.1 inches:  ", np.sum((inches > 0) & (inches < 0.1)))

    # Boolean Arrays as Masks

    # A more powerful pattern is to use Boolean arrays as masks, to select particular subsets of data themselves.

    # As before, we can obtain a Boolean array for, say, values that are less than 5:
    print(x < 5)

    # Now to select these values from the array, we can simply index on this Boolean array;

    # This is known as masking operation:
    print(x[x < 5])
    # What is returned is a one-dimensional array filled with all the values that meet this condition: in other words,
    # all the values in positions at which the mark array is True.

    # Back to the Seattle rain data:
    rainy = (inches > 0)

    summer = ((np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0))
    print(summer)

    print("Median precip on rainy days in 2014 (inches): ", np.median(inches[rainy]))

    print("Median precip on summer days in 2014 (inches): ", np.median(inches[summer]))

    print("Maximum precip on summer days in 2014 (inches): ", np.max(inches[summer]))

    print("Median precip on non-summer days in 2014 (inches): ", np.median(inches[rainy & ~summer]))

def Fancy_Indexing():
    print("Implement!")


if __name__ == "__main__":
    # Fixed_Type_Array_in_Python()
    # Creating_Arrays_from_Python_Lists()
    # Creating_Arrays_from_Scratch()
    # NumPy_Array_Atributes()
    # Array_Indexing_Accessing_Single_Elements()
    # Array_Slicing_Accessing_Subarrays()
    # Reshaping_of_Arrays()
    # Array_Slicing_Accessing_Subarrays()
    # Array_Concatenation_and_Splitting()
    # Computation_on_NumPy_Arrays_Universal_Functions()
    # Advanced_Ufunc_Features()
    # Aggregation_Min_Max_and_Everything_in_Between()
    # Aggregation_Min_Max_and_Everything_in_Between()
    # What_Is_the_Average_Height_of_US_Presidents()
    # Computation_on_Arrays_Broadcasting()
    # Broadcasting_in_Practice()
    # Comparisons_Masks_and_Boolean_Logic()
    Fancy_Indexing()
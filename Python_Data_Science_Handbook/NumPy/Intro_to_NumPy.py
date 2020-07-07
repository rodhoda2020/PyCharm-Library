import numpy as np
import pandas as pd
import matplotlib as plot
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
    print("This must be implemented!")

def Advanced_Ufunc_Features():
    print("This must be implemented!")

def Aggregation_Min_Max_and_Everything_in_Between():
    print("This must be implemented!")

def  What_Is_the_Average_Height_of_US_Presidents():  # Exercise example

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
    What_Is_the_Average_Height_of_US_Presidents()
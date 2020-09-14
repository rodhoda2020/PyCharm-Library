from coding_python import divide

# Note: In pycharm, in order to import from another python file, you must mark the
# directory that file is in as the source root.
# Unknown consequences to doing this, therefore un-mark the directory unless
# necessary otherwise
print(divide(10, 2))

# After running the program, since the code was imported from another file,
# the __name__ will change to the name of the file that was imported.
# '__main__' will only show up in the same file.

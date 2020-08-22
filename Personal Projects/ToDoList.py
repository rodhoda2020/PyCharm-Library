import pandas as pd

# WHat the excel sheet will look like
# Columns: Task, Due Date, Category, Level of Importance

# The user will only see the tasks through the program and not the excel sheet

# What the project will entail:

# 1. Adding a task (and all other aspects of it)
# 2. Printing all tasks
# 3. Print a specific task (Print tasks with the same due date, category, etc.)
# 4. Remove a task (We can print the tasks and ask the user which index they would like to remove)
#                  (We can move these tasks to another excel sheet that stores completed tasks)

# See if you can order the tasks by due date and then by level of importance
# See if you can program the script to use colors for the levels of importance, so that the blocks that are
# under the "Level of Importance" will use a color to signify their importance.

# A snippet for how the print specific task function will look like:
# def print_specific_task():
#   x = input("With which category would you like to print?") They should also be shown the list of categories they can choose from
#   if x == "category":
#       y = input("Which category would you like to print from?") This would show the different projects the user has used
#       if == "work":                                             to compartmentalize their tasks.
#           ...
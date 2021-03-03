import pandas as pd
import numpy as np

df = pd.read_csv("01-Jan-2018_to_24-Feb-2021.csv")

pd.set_option('display.max_columns', None)

to_drop = ['Order ID',
           'UNSPSC Code',
           'ASIN/ISBN',
           'Seller Credentials',
           'Purchase Order Number',
           'PO Line Number',
           'Tax Exemption Applied',
           'Tax Exemption Type',
           'Exemption Opt-Out',
           'Group Name',
           'Release Date',
           'Seller',
           'Carrier Name & Tracking Number']

df.drop(to_drop, inplace=True, axis=1)

print(df.head())

# A Calendar heat map that shows the number of purchases made in a single day based on the color of the block (day)


# What were the purchase price ranges?

# The number of purchases made by each person

# THe amount of money spent by each person

# How many purchases have been made between the two addresses

# How many days passed from the purchase date to shipment date

# What are the most common average days passed from purchase to shipment date

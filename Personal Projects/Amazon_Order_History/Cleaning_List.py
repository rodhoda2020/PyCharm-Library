import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


def clean_currency_values():
    df['Item Total'] = df['Item Total'].str.replace('$', '')
    df['Item Total'] = df['Item Total'].astype(float)

# A Calendar heat map that shows the number of purchases made in a single day based on the color of the block (day)


# What were the purchase price ranges?

# The number of purchases made by each person

def purchase_per_person():

    labels = df['Shipping Address Name'].unique()

    purchases = df['Shipping Address Name'].value_counts()

    plt.pie(purchases, labels=labels, autopct=lambda x: '{:.0f}'.format(x*purchases.sum()/100))
    plt.title('No. of Purchases Per Person')
    plt.axis('equal')
    return plt.show()


# The amount of money spent by each person
def expense_per_person():
    clean_currency_values()

    labels = df['Shipping Address Name'].unique()
    print(labels)
    labels1 = ['Danielle', 'Laleh', 'Rod', 'Sam']

    purchase_value = df.groupby(by=['Shipping Address Name'])['Item Total'].sum()
    print(purchase_value)

    plt.pie(purchase_value, labels=labels1, autopct= lambda x: '{:.2f}%  (${:.0f})'.format(x, x*purchase_value.sum()/100))
    plt.title('Sum of Purchases Per Person')
    plt.axis('equal')
    return plt.show()

# How many purchases have been made between the two addresses


def purchases_per_address():
    address = df['Shipping Address Street 1'].str[-4:].unique()
    print(address)

# How many days passed from the purchase date to shipment date

# What are the most common average days passed from purchase to shipment date


if __name__ == '__main__':
    # purchase_per_person()
    # expense_per_person()
    purchases_per_address()
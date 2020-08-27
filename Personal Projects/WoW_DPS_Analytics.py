import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
import matplotlib



def cleaning_data(file_path):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        df = pd.read_csv(file_path)

        raw_damage_amount = df['Amount']
        # print(raw_damage_amount)

        damage_amount_df = raw_damage_amount.str.split('\$|%', expand=True)
        damage_amount_df = damage_amount_df.rename(columns={0: 'Whole value',
                                                         1: 'Percent',
                                                         2: 'Abbreviated value'})
        # print(damage_amount_df)

        # Adding the new damage amount that has the whole value, percent and
        # abbreviated value separated into individual columns
        df['Damage (Whole value)'] = damage_amount_df['Whole value']
        df['Damage (Percent)'] = damage_amount_df['Percent']
        df['Damage (Abbreviated)'] = damage_amount_df['Abbreviated value']

        # Removes the whole 'Amount' column since the information is no
        # longer needed
        del df['Amount']

        # We also want to move the damage columns to be start at the second
        # position since they are easier to read next to the name
        column_names = ["Name",
                        "Damage (Whole value)",
                        "Damage (Percent)",
                        "Damage (Abbreviated)",
                        "Casts",
                        "Avg Cast",
                        "Hits",
                        "Avg Hit",
                        "Crit %",
                        "Uptime %",
                        "Miss %",
                        "DPS",
                        "Unnamed: 10"]
        df = df.reindex(columns=column_names)

        # This is the function for dropping duplicates. First
        # You give a subset of columns you want it to check, we only need 1.
        # You till it whether you want to keep the first one and remove other
        # duplicates.
        df.drop_duplicates(subset='Damage (Whole value)',
                           keep='first', inplace=True)

        # Special case (Try to modify later):
        # We need to remove the Whirlwind Off-hand row since it is an extension
        # of the main whirlwind


        # Since the rows that had duplicates were removed, the index
        # was too. We reset the index value to start from 0 again.
        df = df.reset_index()

        print(df)

        # For percent summation
        # Used to see if the total percent adds to 100 (or really close to it)
        damage_total_percent = df['Damage (Percent)']
        percent = pd.Series(damage_total_percent)
        print("The total percentage shown by the DataFrame: {}".format(sum(map(float, list(percent)))))

def pie_chart(file_path):
    df = pd.read_csv(file_path)



def main():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    cleaning_data(file_path)
    pie_chart(file_path)

if __name__ == '__main__':
    main()
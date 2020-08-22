import pandas as pd
import numpy as np

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    df = pd.read_csv(r'C:\Users\rodho\Documents\Warcraft Logs - Combat Analysis for Warcraft (1).csv')
    # print(df)

    raw_damage_amount = df['Amount']
    print(raw_damage_amount)
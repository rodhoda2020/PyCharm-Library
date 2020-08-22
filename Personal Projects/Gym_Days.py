import pandas as pd
import yaml
from pandas.io.json import json_normalize
import re

df = pd.read_csv(r'text_data.yml')

# print(pd.io.json.json_normalize(yaml.laod(fr'text_data.yml')))

with pd.option_context("display.max_rows", None, "display.max_columns", None):
    with open('text_data.yml', 'r') as f:
        df = pd.json_normalize(yaml.load(f, Loader=yaml.FullLoader), ['training', 'trainings'])
        # print(df)

        # If we were to use regex for the column "performed_at" then we can
        # go through this column of the DataFrame object and use a regular
        # expression to find the dates of each day.

        # We put each date into an array. We then need to filter out the duplicates
        # (search for how to remove duplicates from a NumPy array).

        # We then need to create another array that contains all the dates starting from
        # the same date is considered the earliest and ends with the same date that is
        # considered the latest. We then need to somehow compare the two arrays.
        # For every element that match with one another (have the same value), we can
        # create another boolean array that says true or false.
        # Once we do this, we need to show the all_dates array next to the bool array.

        # Something like this:

        # ...
        # 2020-06-22        True
        # 2020-06-23        False
        # 2020-06-24        False
        # 2020-06-25        True

        # This should all be done

        # print(df['performed_at'])

        performed_at = pd.DataFrame(df)

        dates_no_edit = performed_at['performed_at'].tolist()

        # print(dates_no_edit )
        dates = pd.Series(dates_no_edit)
        # print(dates)
        # print(performed_at['performed_at'])
        dates_edited = pd.to_datetime(dates).dt.date
        # print(dates_edited)

        date_list = []

        for i in dates_edited:
            if i not in date_list:
                date_list.append(i)

        d = pd.Series(date_list)
        print(d)
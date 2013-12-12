#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pandas import concat
from pandas import DataFrame
from pandas import Series


def transaction_from_dataframe(df):
    u"""
    input:
        df: pandas DataFrame
                Name   Sex  Week
            0   Apple   F   Mon
            1  Orange   F   Tue ...
            2   Apple   M   Fri
            3   Grape   M   Mon
            ...

    return:
        pandas DataFrame of transaction dataframe
            Name:Orange  Name:Grape  Name:Apple  Sex:M  Sex:F  Week:Fri  Week:Mon  Week:Tue
        0         0           0           1      0      1         0         1         0
        1         1           0           0      0      1         0         0         1     ...
        2         0           0           1      1      0         1         0         0
        3         0           1           0      1      0         0         1         0
        ...
    """
    transaction = []
    columns = []
    for idx in df:
        col_data = df[idx]
        col_values = set(col_data)
        for val in col_values:
            new_col_name = str(idx) + ":" + str(val)
            columns.append(new_col_name)
            col_ser = Series(1 if d == val else 0 for d in col_data)
            transaction.append(col_ser)

    transaction = concat(transaction, axis=1)
    transaction.columns = columns
    return transaction


def transaction_from_lists(trans_lists):
    u"""
    input:
        trans_lists: list of transaction data
            [['Apple', 'Grape'],
             ['Grape', 'Orange', 'Banana'],
             ['Orange', 'Grape'],
             ['Apple', 'Banana'],
             ...

    return:
        pandas DataFrame of transaction dataframe
               Orange  Grape  Apple  Banana
            0       0      1      1       0
            1       1      1      0       1 ...
            2       1      1      0       0
            3       0      0      1       1
            ...
    """
    transaction = []
    columns = []
    names = tuple(set(trans_data for trans_row in trans_lists for trans_data in trans_row))
    for name in names:
        columns.append(str(name))
        col_ser = Series([1 if name in trans_row else 0 for trans_row in trans_lists])
        transaction.append(col_ser)

    transaction = concat(transaction, axis=1)
    transaction.columns = columns
    return transaction

if __name__ == "__main__":
    df = DataFrame([["Apple", "F", "Mon"],
                    ["Orange", "F", "Tue"],
                    ["Apple", "M", "Fri"],
                    ["Grape", "M", "Mon"]])
    df.columns = ["Name", "Sex", "Week"]
    print "input:"
    print df
    print "output:"
    print transaction_from_dataframe(df)

    trans_lists = [["Apple", "Grape"],
                  ["Grape", "Orange", "Banana"],
                  ["Orange", "Grape"],
                  ["Apple", "Banana"]]
    print "input:"
    print trans_lists
    print "output:"
    print transaction_from_lists(trans_lists)

"""
Series: A one-dimensional array of values
DataFrame: A two-dimensional data structure used to store tabular data

Note: In pandas, Series-based data structures, there is a term called “axis,” which is used to
represent a sequence of values in a particular dimension. Series has only “axis 0” because it has
only one dimension.
"""
import pandas as pd


person_1 = pd.Series(['Adam', 'Male', '33', True])


if __name__ == '__main__':
    print(person_1)

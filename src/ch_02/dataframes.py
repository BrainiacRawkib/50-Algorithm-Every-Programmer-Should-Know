"""
Series: A one-dimensional array of values
DataFrame: A two-dimensional data structure used to store tabular data

Note: In pandas, Series-based data structures, there is a term called “axis,” which is used to
represent a sequence of values in a particular dimension. Series has only “axis 0” because it has
only one dimension.
"""
import pandas as pd


employees_df = pd.DataFrame([
    ['1', 'Adam', 32, True],
    ['2', 'Kareem', 22, False],
    ['3', 'Azeez', 38, True],
    ['4', 'Hassan', 34, False]
])


# In DataFrame, a single column or row is called an axis.

employees_df.columns = ['id', 'name', 'age', 'decision']


if __name__ == '__main__':
    print(employees_df)
    print('\n')
    print(employees_df[['name', 'age']])
    print('\n')
    print('**** Column Selection ****')
    print(employees_df.iloc[:, 3])
    print('\n')
    print('**** Row Selection ****')
    print(employees_df.iloc[1:3, :])
    print('\n')
    print('**** Selection with Age Condition ****')
    print(employees_df[employees_df.age > 30])
    print('\n')
    print('**** Selection with Age and Decision Condition ****')
    print(employees_df[(employees_df.age > 30) & (employees_df.decision == True)])

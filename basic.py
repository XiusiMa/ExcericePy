# thanks to Kevin Markham for his expertise and resources
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:41:32 2016

@author: mxs92
"""
'''
CLASS: Pandas for Exploratory Data Analysis
MovieLens 100k movie rating data:
    main page: http://grouplens.org/datasets/movielens/
    data dictionary: http://files.grouplens.org/datasets/movielens/ml-100k-README.txt
    files: u.user, u.user_original (no header row)
WHO alcohol consumption data:
    article: http://fivethirtyeight.com/datalab/dear-mona-followup-where-do-people-drink-the-most-beer-wine-and-spirits/    
    original data: https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption
    file: drinks.csv (with additional 'continent' column)
National UFO Reporting Center data:
    main page: http://www.nuforc.org/webreports.html
    file: ufo.csv
'''
'''
EXERCISE ONE
'''
import pandas as pd
# read drinks.csv into a DataFrame called 'drinks'

drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')              # assumes separator is comma

# print the head and the tail

drinks.head()
drinks.tail(10)

# examine the default index, data types, and shape

drinks.index
drinks.dtypes
drinks.shape
#drinks.values

# print the 'beer_servings' Series

drinks['beer_servings']

# calculate the mean 'beer_servings' for the entire dataset

drinks.beer_servings.mean()

# count the number of occurrences of each 'continent' value and see if it looks correct
drinks.continent.value_counts(ascending=True)
'''
Help on method value_counts in module pandas.core.base:

value_counts(self, normalize=False, sort=True, ascending=False, bins=None, dropna=True) method of pandas.core.series.Series instance
    Returns object containing counts of unique values.
    
    The resulting object will be in descending order so that the
    first element is the most frequently-occurring element.
    Excludes NA values by default.
    
    Parameters
    ----------
    normalize : boolean, default False
        If True then the object returned will contain the relative
        frequencies of the unique values.
    sort : boolean, default True
        Sort by values
    ascending : boolean, default False
        Sort in ascending order
    bins : integer, optional
        Rather than count values, group them into half-open bins,
        a convenience for pd.cut, only works with numeric data
    dropna : boolean, default True
        Don't include counts of NaN.
    
    Returns
    -------
    counts : Series
'''
users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|', index_col='user_id')

# BONUS: display only the number of rows of the 'users' DataFrame
#users.users_id.value_counts()
users.index.value_counts()

# BONUS: display the 3 most frequent occupations in 'users'

users.columns
mydata = pd.DataFrame( users.occupation.value_counts())
mydata.head(3)

# BONUS: create the 'users' DataFrame from the u.user_original file (which lacks a header row)
# Hint: read the pandas.read_table documentation



'''
EXERCISE TWO
'''

# filter 'drinks' to only include European countries


# filter 'drinks' to only include European countries with wine_servings > 300


# calculate the mean 'beer_servings' for all of Europe


# determine which 10 countries have the highest total_litres_of_pure_alcohol


# BONUS: sort 'users' by 'occupation' and then by 'age' (in a single command)
sort_value

# BONUS: filter 'users' to only include doctors and lawyers without using a |
# Hint: read the pandas.Series.isin documentation
users
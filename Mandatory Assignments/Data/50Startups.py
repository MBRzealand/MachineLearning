# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:00:48 2020

@author: EASJ
"""


import pandas as pd

#Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values



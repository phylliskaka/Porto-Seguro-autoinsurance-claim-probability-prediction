#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 23:03:12 2018

@author: phyllis
"""
#%%
import numpy as np
import pandas as pd 
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA 
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


#import dataset 
train_address = '/home/phyllis/Desktop/PCA/train.csv'
test_address = '/home/phyllis/Desktop/PCA/test.csv'

train_data = pd.read_csv(train_address, sep = ',')
test_data = pd.read_csv(test_address, sep = ',')

#preprocessing train data 
X_train = train_data.drop('target', 1)
Y_train = train_data['target']

#split the train data into train and test parts
X_train, X_train_test, Y_train, Y_train_test = train_test_split(X_train, Y_train, test_size = 0.3, random_state =0) 

#normalize the data on train data set 
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_train_test = sc.transform(X_train_test)


#Aplying PCA on train data set 
pca = PCA(n_components = 2) # you can change number of components here 
X_train = pca.fit_transform(X_train)
X_train_test = pca.transform(X_train_test)

#explained_variance = pca.explained_variance_ratio_
#print(explained_variance)

#train desiontree 
clf_gini = DecisionTreeClassifier(criterion = 'gini', max_depth = 6, random_state =0)
clf_gini.fit(X_train, Y_train)

#Train_test prediction
Y_prediction = clf_gini.predict(X_train_test)

#get the accuracy of train_test prediction 
accuracy = accuracy_score(Y_test, Y_prediction)

#%%
#test dataset 
X_test = test_data
X_test = sc.transform(X_test)
X_test = pca.transform(X_test)
Y_test_prediction = clf_gini.predict(X_test)

#output is Y_test_prediction 




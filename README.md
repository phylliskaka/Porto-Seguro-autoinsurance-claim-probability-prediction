# Porto-Seguro-autoinsurance-claim-probability-prediction
## Introduction 
Porto Seguro, one of Brazil’s largest auto and homeowner insurance companies, completely agrees. Inaccuracies in car insurance company’s claim predictions raise the cost of insurance for good drivers and reduce the price for bad ones. The goal of this project is build a model to predict the probability that a driver will initiate an auto insurance claim in the next year.

## Data Source
The data is taken from a Kaggle dataset: PCA analysis with Decision Tree     
URL: https://www.kaggle.com/priyasd/portoseguro      
The data consist of two csv file: test and train. train file include the target column which is the number that customer make claimm while the test file dont include the target column. The goal is to predict the target column for test file.

## Pseudo code 
#Preprocessing the _train_ data    
#Split the train data into _train_ and *train_test* parts   
#Applying normalization on _train_ data AND _train_test_ data  
#Aplying PCA on _train_ data AND *train_test* data  
#Training desiontree on _train_ data   
#Prediction of *train_test*   
#Get the accuracy of *train_test* prediction    
#Predic _test_ data  

## Issue 
1. After applying PCA on _train_ data, the contribution of all the principle components(totally 58 principle components) looks like following. 

![alt text](/home/phyllis/Pictures/Screenshot from 2018-10-31 21-08-12.png)




# Porto-Seguro-autoinsurance-claim-probability-prediction(PCA)
## Introduction 
Porto Seguro, one of Brazil’s largest auto and homeowner insurance companies, completely agrees with inaccuracies in car insurance company’s claim predictions raise the cost of insurance for good drivers and reduce the price for bad ones. The goal of this project is build a model to predict the probability that a driver will initiate an auto insurance claim in the next year.

## Data Source
The data is taken from a Kaggle dataset: [PCA analysis with Decision Tree](https://www.kaggle.com/priyasd/portoseguro)   

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
After applying PCA on _train_ data, the contribution of all the principal components(totally 58 principal components) looks like following:

![alt text](https://github.com/phylliskaka/Porto-Seguro-autoinsurance-claim-probability-prediction/blob/master/all%20principal%20component.png)

The first and second principal components only take 10% of total sum of eigenvalue. However, we are not sure it is noise or not. So we predict the data that reduce to 2 dimensions, 4 dimensions and 6 dimensions.The result turn out to be following:

| Number of reduced dimension |    Accuracy      |
|-----------------------------|:---------------: |
|        2 components         | 0.96368808942452 |
|        4 components         | 0.96366008825967 |
|        6 components         | 0.96364328756076 | 

Thus, we can assure that 2 components is the best for decision tree predition. 

 


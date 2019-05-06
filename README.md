# Porto-Seguro-autoinsurance-claim-probability-prediction(PCA)
## Introduction 
Porto Seguro, one of Brazil’s largest auto and homeowner insurance companies, completely agrees with that inaccuracies in car insurance company’s claim predictions raise the cost of insurance for good drivers and reduce the price for bad ones. The goal of this project is build a model to predict the probability that a driver will initiate an auto insurance claim in the next year.

## Data Source
This is a Kaggle project available at: [PCA analysis with Decision Tree](https://www.kaggle.com/priyasd/portoseguro)      

The dataset consists of two csv file: test.csv and train.csv. The data including 58 features which is the biggest challenge in this project. There are two reasons that we should avoid original dataset for prediction. 
First, in 58 features, there might be a lot of features that is irrelavent to predicting. And, predicing with a lot of irrelavent feature can lead to overfitting. Thus, in this project, we need to reduce the dataset dimension before feed to decision tree. Second, more features result to more computation using decision tree.   

## Result
1. After applying PCA on _train_ data, we can get the data that describe how many contribution each principal componenet will make in the prediction process. The percentage, that each principal components will contribute, are draw below:    

![alt text](https://github.com/phylliskaka/Porto-Seguro-autoinsurance-claim-probability-prediction/blob/master/all%20principal%20component.png) .   
  
In the graph, we can clearly see that the first and second principal components only contribute 10% in total. Thus, we are not sure how many components we should use for prediction. Hence, we need to search for optimum dimension which can result to best testing accuracy. To search for optimum dimension of data, we can do it two ways: coarse grid search and fine grid search .    
  
1. coarse grid search        
So I predicted the data that has dimensions of 2, 10, 18, 26, 32, 40, 48. The testing accuracy turn out to be following:      
![alt text](https://github.com/phylliskaka/Porto-Seguro-autoinsurance-claim-probability-prediction/blob/master/train_accuracy.png)    
    
From the graph, we can clearly see the tesing accuracy of experiment decreases with number of dimension increasing.          

2. fine grid search      
I predicted the data that has dimensions of 2, 4, 6 (max_depth = 6). The testing accuracy turn out to be following:    

| Number of reduced dimension |    Accuracy      |
|-----------------------------|:---------------: |
|        2 components         | 0.96368808942452 |
|        4 components         | 0.96366008825967 |
|        6 components         | 0.96364328756076 | 


The testing accuracy does not decrease very obviously. In this project, we decide to reduce the data to 2 dimensions and predicting test data using decision tree classifier. The best testing accuracy are 96.4%.   

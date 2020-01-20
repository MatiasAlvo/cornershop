    # Cornershop´s Data Science Test

For this data science test, I performed 4 different models: Linear Regression, deep neural network, random forest and XGBoost.  In this case, the model that worked the best was deep neural network and followed closely by linear regression.  This might mean that the relationship between the variables is near to linear or maybe we need more data to be able to gain advantage by using complex models.

I dumped predictions using this 4 models, but the predictions to be taken into account are the ones made with the deep neural network (DNN.csv) as it is the one that performed the best. 

Important scripts:

Features: reads the original data, process the data, adds new features and dumps new files for training, validation and test sets, and separate files for the data with null values for total_minutes

Regression_model, DNN_model, random_forest_model, xgboost_model: jupyter notebook python scripts, which create and train the respective models and make predictions for the desired data.  It is important to note that whenever we try to optimize on the hyperparameters, the process make time a lot of time to complete.  Moreover, training neural networks in the DNN_model file is also really slow.  The code is explained step by step to clarify the methodology used.

data: original data and dumps of the new data created in the Features script

Predictions: predictions made for the data with null values on total_minutes by the different models.

models_dump: dump of the different trained models

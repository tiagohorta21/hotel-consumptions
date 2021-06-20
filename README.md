# Hotel Consumptions

This assignment focuses in several aspects of a platform for the monitoring, prediction, and optimization of consumptions with a particular interest in the prediction of energy consumptions and anomaly detection.

In file hotel consumptions.csv you can find the data collected for a period of time in an hotel. Besides the timestamps of the observation, data includes wind velocity, external temperature, hotel occupation (number of guests), and the total consumption.

### This work will is divided in three parts:

**Data analysis and manipulation (max. 25%):** 

Use Pandas to make a study of your data. Present statistics, plot graphs, etc. Use Pandas to cleanup and do necessary operations into your data. Split the timestamp and use
it to, for instance, add a value with the day of the week, etc.

**Prediction model (max. 50%):** 

Use the Scikit-learn library to elaborate a study comparing several methods to preview the hotel consumptions. Make a justified decision for one of those methods - use (grid) cross-validation. Use Jupyter notebooks to do your study, and present your justifications using the markdown functionalities. Remember that you should only preview consumptions for days in the future when compared with the timestamp of the training data, i.e., you should “not use a split with shuffle method”. Furthermore, present your results (predictions) for at least 10 days, i.e., select “10” representative days, train with past data and compute the average results (e.g., mean square/absolute error, R2 or others).

**Azure ML Studio (max. 10%):** 

Design an experiment in the Azure ML Studio by training a model to predict the hotel’s consumption. Use that model to build a web service. Create an Excel file which connects to that web service and provides predictions given the above features.

**& some research... (max. 15%):** 

Implement a sliding window method which makes consumption predictions for near future periods. The model should use a regressor to form a collection of regressors with the following particularity:
  - A regressor is built every h-hours using data from the previous dhours (h and d are program parameter to be tuned).
  - The prediction should use k-regressors (k is a program parameter to be tuned) from the collection giving more importance to recent regressors. 

To implement this, use a method to select the regressors based on their timestamp. E.g., think of a roulette wheel with different sized slices or use a technique to “forget” older regressors.
Show (e.g., some statistics and plots) the accuracy of your prediction for the next hours.

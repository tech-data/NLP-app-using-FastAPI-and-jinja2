# Sentiment Analysis Model

This repository contains code for a sentiment analysis model that can classify texts as expressing one of five emotions: joy, anger, love, sadness, or fear. The model is built using a linear support vector classifier (LinearSVC) and the scikit-learn library. 

## Data

The model was trained and tested on two datasets: `data.csv` and `test.csv`. Both datasets contain texts and corresponding labels, with the labels representing the emotions expressed in the texts. 

The `data.csv` dataset has 18,000 rows and the `test.csv` dataset has 2,000 rows. The data was preprocessed by encoding the categorical labels as numerical values using the LabelEncoder from the scikit-learn library.

## Dependencies

The model was built using the following dependencies:

- pandas
- sklearn
- numpy
- pickle

## Usage

To use the sentiment analysis model, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies (pandas, sklearn, numpy, and pickle).
3. Run the `train.py` script to train the model on the `data.csv` dataset and save the model and LabelEncoder to files.
4. Run the `predict.py` script and input a text to get a prediction of the corresponding emotion expressed in the text.

Note that the model has an accuracy of 99.25% on the training set and 85.95% on the test set, so it should be used with caution and not relied on as the sole basis for sentiment analysis.




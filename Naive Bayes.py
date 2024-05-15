from google.colab import files
upload = files.upload()

import pandas as pd
df = pd.read_csv("diabetes_dataset.csv")

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import GaussianNB
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
print("Number of mislabeled points out of a total points :", ((y_test != y_pred).sum(), X_test.shape[0]))
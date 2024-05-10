from google.colab import files
upload = files.upload()

import pandas as pd
df = pd.read_csv("diabetes_dataset.csv")

import numpy as np

from sklearn.datasets import load_iris

data = load_iris()
#convert to a dataframe

df = pd.DataFrame(data.data, columns = data.feature_names)
df.head()
#create the species column

df['Species'] = data.target
df.head()
#replace this with the actual names

target = np.unique(data.target)

target_names = np.unique(data.target_names)

targets = dict(zip(target, target_names))

df['Species'] = df['Species'].replace(targets)
x = df.drop(columns="Species")

y = df["Species"]

feature_names = x.columns

labels = y.unique()
#split the dataset

from sklearn.model_selection import train_test_split

X_train, test_x, y_train, test_lab = train_test_split(x,y, test_size = 0.4,random_state = 42)
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='entropy',max_depth =3, random_state = 42)

clf.fit(X_train, y_train)
from sklearn import tree
import matplotlib.pyplot as plt

plt.figure(figsize=(30,10), facecolor ='k')

a = tree.plot_tree(clf,feature_names = feature_names, class_names = labels, rounded = True, filled = True,fontsize=14)

plt.show()
#2. As a Text-Based Diagram
from sklearn.tree import export_text

tree_rules = export_text(clf,feature_names = list(feature_names))

print(tree_rules)
# Predict Class From Test Values
test_pred_decision_tree = clf.predict(test_x)
from sklearn import metrics

import seaborn as sns

import matplotlib.pyplot as plt

confusion_matrix = metrics.confusion_matrix(test_lab,  test_pred_decision_tree)

matrix_df = pd.DataFrame(confusion_matrix)
ax = plt.axes()

sns.set(font_scale=1.3)

plt.figure(figsize=(10,7))

sns.heatmap(matrix_df, annot=True, fmt="g", ax=ax, cmap="magma")

ax.set_title('Confusion Matrix - Decision Tree')

ax.set_xlabel("Predicted label", fontsize =15)

ax.set_xticklabels(['']+labels)

ax.set_ylabel("True Label", fontsize=15)

ax.set_yticklabels(list(labels), rotation = 0)

plt.show()
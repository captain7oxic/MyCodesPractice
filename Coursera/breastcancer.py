#%%
import scipy as sp
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import numpy as np
cancer=load_breast_cancer()
print(" cancer.keys : \n{}".format(cancer.keys()))
print ("shape of breast cancer data: \n{}".format(cancer.data.shape))
#%%
print("Sample counts per class:\n{}".format(
{n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}))
#%%
print("feature description : \n{}".format(cancer.DESCR))
print("feature names of data points : \n{}".format(cancer.feature_names))

#%%
#predictions on the dataset using KNN
from sklearn.neighbors import KNeighborsClassifier
#splitting the data in training and splitting data
from sklearn.model_selection import train_test_split
# stratify was used here to make sure that training 
# and testing data
# have same proportions of target values.
# random state here was used as 66 for reproducibility of 
# initial shuffling of training datasets for each epoch

X_train, X_test, y_train, y_test = train_test_split(cancer.data,cancer.target, stratify=cancer.target, random_state=66)
training_accuracy=[]
test_accuracy=[]
#try all neighbours from 1 to 10
neighbor_mapping=range(1,11)
for neighbors in neighbor_mapping:
    #The model 🐱‍
    KNN=KNeighborsClassifier(n_neighbors=neighbors)
    KNN.fit(X_train,y_train)
    #storing scores in the test and accuracy lists
    training_accuracy.append(KNN.score(X_train,y_train))
    test_accuracy.append(KNN.score(X_test,y_test))

plt.plot(neighbor_mapping, training_accuracy, label="training accuracy")
plt.plot(neighbor_mapping, test_accuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
#%%


# %%

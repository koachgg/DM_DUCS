
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=100


gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)


print(f'Accuracy Score: {accuracy_score(y_test, y_pred) * 100} %')


knn = KNeighborsClassifier() # default k=5
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print(f'Accuracy Score: {accuracy_score(y_test, y_pred) * 100} %')


print(classification_report(y_test, y_pred))


dtree = DecisionTreeClassifier() # default criteria='gini'
dtree.fit(X_train, y_train)
y_pred = dtree.predict(X_test)


print(f'Accuracy Score: {accuracy_score(y_test, y_pred) * 100} %')


print(classification_report(y_test, y_pred))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100)


gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)


print(f'Accuracy Score: {accuracy_score(y_test, y_pred) * 100} %')


knn = KNeighborsClassifier() # default k=5
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print(f'Accuracy Score: {accuracy_score(y_test, y_pred) * 100} %')


print(classification_report(y_test, y_pred))


dtree = DecisionTreeClassifier() # default criteria='gini'
dtree.fit(X_train, y_train)
y_pred = dtree.predict(X_test)

y_pred = dtree.predict(X_test)

print(classification_report(y_test, y_pred))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)


gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)


print(f'Accuracy Score: {accuracy_score(y_test, y_pred) * 100} %')


knn = KNeighborsClassifier() # default k=5
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)


print(f'Accuracy Score: {accuracy_score(y_test, y_pred) * 100} %')

print(classification_report(y_test, y_pred))


dtree = DecisionTreeClassifier() # default criteria='gini'
dtree.fit(X_train, y_train)
y_pred = dtree.predict(X_test)


print(f'Accuracy Score: {accuracy_score(y_test, y_pred) * 100} %')


print(classification_report(y_test, y_pred))


from sklearn.model_selection import ShuffleSplit

 rs = ShuffleSplit(n_splits=10, test_size=0.25, random_state=100)
accuracy_gnb = []
accuracy_knn = []
accuracy_dtree = []


for train_index, test_index in rs.split(X):
 X_train = np.array([X[index] for index in train_index])
 X_test = np.array([X[index] for index in test_index])
 y_train = np.array([y[index] for index in train_index])
 y_test = np.array([y[index] for index in test_index])
 y_pred = GaussianNB().fit(X_train, y_train).predict(X_test)
 accuracy_gnb.append(accuracy_score(y_test, y_pred))
 y_pred = KNeighborsClassifier().fit(X_train, y_train).predict(X_test)
 accuracy_knn.append(accuracy_score(y_test, y_pred))
 y_pred = DecisionTreeClassifier().fit(X_train, y_train).predict(X_test)
 accuracy_dtree.append(accuracy_score(y_test, y_pred))
 
 
print(f'Mean accuracy of Gaussian Naive Bayes: {sum(accuracy_gnb) / len(accuracy_gnb) * 100} %')
print(f'Mean accuracy of K-Nearest Neighbors: {sum(accuracy_knn) / len(accuracy_knn) * 100} %')
print(f'Mean accuracy of Decision Tree Classifier: {sum(accuracy_dtree) / len(accuracy_dtree) * 100} %') 


dtree = DecisionTreeClassifier()
knn = KNeighborsClassifier()
gnb = GaussianNB()


accuracy_dtree = cross_val_score(dtree, X, y, cv=5)
accuracy_knn = cross_val_score(knn, X, y, cv=5)
accuracy_gnb = cross_val_score(gnb, X, y, cv=5)


print(f'Mean accuracy of Gaussian Naive Bayes: {sum(accuracy_gnb) / len(accuracy_gnb) * 100} %')
print(f'Mean accuracy of K-Nearest Neighbors: {sum(accuracy_knn) / len(accuracy_knn) * 100} %')
print(f'Mean accuracy of Decision Tree Classifier: {sum(accuracy_dtree) / len(accuracy_dtree) * 100} %')


from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=100)

 sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)


print(f'Accuracy Score: {accuracy_score(y_test, y_pred) * 100} %')


knn = KNeighborsClassifier() # default k=5
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)


print(f'Accuracy Score: {accuracy_score(y_test, y_pred) * 100} %')


print(classification_report(y_test, y_pred))


dtree = DecisionTreeClassifier() # default criteria='gini'
dtree.fit(X_train, y_train)
y_pred = dtree.predict(X_test)


print(f'Accuracy Score: {accuracy_score(y_test, y_pred) * 100} %')
print(classification_report(y_test, y_pred))


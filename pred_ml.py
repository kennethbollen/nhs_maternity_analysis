#!python3

from data_extract import *
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X_train, y_train)
print('Training score: {:.2f}'.format(knn.score(X_train, y_train)))
print('Test score: {:.2f}'.format(knn.score(X_test, y_test)))




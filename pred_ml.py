#!python3

from data_extract import *
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#a list of all the X variables
X_list = [smk, under ,obese, plus45, age35_to_39, age40_to_44, caesar, no_caesar, no_birth, no_live_birth]

#determine the correlation of each independent variable with the target variable
x_corr = []
for i in range(len(X_list)):
    x_corr.append(np.corrcoef(X_list[i], y)[0][1])
    
#plot the variables on a graph - create linear measure
fig = plt.figure()

slope_smk, int_smk = np.polyfit(smk, pre, 1)
x_smk = np.array([min(smk), max(smk)])
y_smk = slope_smk * x_smk + int_smk
plt.subplot(2, 5, 1)
plt.plot(smk, pre, marker='.', linestyle='none', color='r')
plt.xlabel('mothers smoking')
plt.ylabel('premature babies')
plt.title('%s correlation' % round(x_corr[0], 2))
plt.plot(x_smk, y_smk)

slope_under, int_under = np.polyfit(under, pre, 1)
x_under = np.array([min(under), max(under)])
y_under = slope_under * x_under + int_under
plt.subplot(2, 5, 2)
plt.plot(under, pre, marker='.', linestyle='none', color='r')
plt.xlabel('mothers underweight')
plt.ylabel('premature babies')
plt.title('%s correlation' % round(x_corr[1], 2))
plt.plot(x_under, y_under)

slope_obese, int_obese = np.polyfit(obese, pre,1)
x_obese = np.array([min(obese), max(obese)])
y_obese = slope_obese * x_obese + int_obese
plt.subplot(2, 5, 3)
plt.plot(obese, pre, marker='.', linestyle='none', color='r')
plt.xlabel('mothers obese')
plt.ylabel('premature babies')
plt.title('%s correlation' % round(x_corr[2], 2))
plt.plot(x_obese, y_obese)

slope_age39, int_age39 = np.polyfit(age35_to_39, pre,1)
x_age39 = np.array([min(age35_to_39), max(age35_to_39)])
y_age39 = slope_age39 * x_age39 + int_age39
plt.subplot(2, 5, 4)
plt.plot(age35_to_39, pre, marker='.', linestyle='none', color='r')
plt.xlabel('mothers aged 35 to 39')
plt.ylabel('premature babies')
plt.title('%s correlation' % round(x_corr[3], 2))
plt.plot(x_age39, y_age39)

slope_age44, int_age44 = np.polyfit(age40_to_44, pre,1)
x_age44 = np.array([min(age40_to_44), max(age40_to_44)])
y_age44 = slope_age44 * x_age44 + int_age44
plt.subplot(2, 5, 5)
plt.plot(age40_to_44, pre, marker='.', linestyle='none', color='r')
plt.xlabel('mothers aged 40 to 44')
plt.ylabel('premature babies')
plt.title('%s correlation' % round(x_corr[4], 2))
plt.plot(x_age44, y_age44)

slope_plus45, int_plus45 = np.polyfit(plus45, pre,1)
x_plus45 = np.array([min(plus45), max(plus45)])
y_plus45 = slope_plus45 * x_plus45 + int_plus45
plt.subplot(2, 5, 6)
plt.plot(plus45, pre, marker='.', linestyle='none', color='r')
plt.xlabel('mothers +45 years')
plt.ylabel('premature babies')
plt.title('%s correlation' % round(x_corr[5], 2))
plt.plot(x_plus45, y_plus45)

slope_caesar, int_caesar = np.polyfit(caesar, pre,1)
x_caesar = np.array([min(caesar), max(caesar)])
y_caesar = slope_caesar * x_caesar + int_caesar
plt.subplot(2, 5, 7)
plt.plot(caesar, pre, marker='.', linestyle='none', color='r')
plt.xlabel('mothers previous caesarian births')
plt.ylabel('premature babies')
plt.title('%s correlation' % round(x_corr[6], 2))
plt.plot(x_caesar, y_caesar)

slope_no_caesar, int_no_caesar = np.polyfit(no_caesar, pre,1)
x_no_caesar = np.array([min(no_caesar), max(no_caesar)])
y_no_caesar = slope_no_caesar * x_no_caesar + int_no_caesar
plt.subplot(2, 5, 8)
plt.plot(no_caesar, pre, marker='.', linestyle='none', color='r')
plt.xlabel('mothers no previous caesarian births')
plt.ylabel('premature babies')
plt.title('%s correlation' % round(x_corr[7], 2))
plt.plot(x_no_caesar, y_no_caesar)

slope_no_birth, int_no_birth = np.polyfit(no_birth, pre,1)
x_no_birth = np.array([min(no_birth), max(no_birth)])
y_no_birth = slope_no_birth * x_no_birth + int_no_birth
plt.subplot(2, 5, 9)
plt.plot(no_birth, pre, marker='.', linestyle='none', color='r')
plt.xlabel('mothers no previous births')
plt.ylabel('premature babies')
plt.title('%s correlation' % round(x_corr[8], 2))
plt.plot(x_no_birth, y_no_birth)

slope_no_live_birth, int_no_live_birth = np.polyfit(no_live_birth, pre,1)
x_no_live_birth = np.array([min(no_live_birth), max(no_live_birth)])
y_no_live_birth = slope_no_live_birth * x_no_live_birth + int_no_live_birth
plt.subplot(2, 5, 10)
plt.plot(no_live_birth, pre, marker='.', linestyle='none', color='r')
plt.xlabel('mothers no previous live births')
plt.ylabel('premature babies')
plt.title('%s correlation' % round(x_corr[9], 2))
plt.plot(x_no_live_birth, y_no_live_birth)

plt.show()

#split the data into train and test for dataset X and y
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#Linear Regreesion
param_grid_linear = {'n_jobs': [1, 2, 3, 4, 5]}
grid = GridSearchCV(LinearRegression(), param_grid_linear, cv=5)
grid.fit(X_train, y_train)
#print('best parameters (number of jobs): {}'.format(grid.best_params_))
#n_jobs = 1
print('linear regression training score: {:.2f}'.format(grid.score(X_train, y_train)))
#linear training score: 1
print('linear regression test score: {:.2f}'.format(grid.score(X_test, y_test)))
#linear test score: 0.02
linear_train_score = grid.score(X_train, y_train)
linear_test_score = grid.score(X_test, y_test)

#Lasso Regression, constrain the unimportant features
param_grid_lasso = {'alpha': [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]}
grid_lasso = GridSearchCV(Lasso(), param_grid_lasso, cv=5)
grid_lasso.fit(X_train, y_train)
#print('best parameters (alpha): {}'.format(grid_lasso.best_params_))
# alpha = 100
print('lasso training score: {:.2f}'.format(grid_lasso.score(X_train, y_train)))
# lasso score = 1
print('lasso test score: {:.2f}'.format(grid_lasso.score(X_test, y_test)))
# lasso score = 0.27
lasso_train_score = grid_lasso.score(X_train, y_train)
lasso_test_score = grid_lasso.score(X_test, y_test)

#K Nearest Neighbors Regression
param_grid_neighbors = {'n_neighbors': [1, 2, 3, 4, 5]}
grid_neighbors = GridSearchCV(KNeighborsRegressor(), param_grid_neighbors, cv=5)
grid_neighbors.fit(X_train, y_train)
#print('best parameters: {}'.format(grid_neighbors.best_params_))
print('KNN training score: {:.2f}'.format(grid_neighbors.score(X_train, y_train)))
#KNN Training score: 1
print('KNN test score: {:.2f}'.format(grid_neighbors.score(X_test, y_test)))
#KNN Test score: 0.41
knn_train_score = grid_neighbors.score(X_train, y_train)
knn_test_score = grid_neighbors.score(X_test, y_test)

#plot the scores
scores = pd.DataFrame({'train': [linear_train_score, lasso_train_score, knn_train_score], 'test': [linear_test_score, lasso_test_score, knn_test_score]}, index=['linear', 'lasso', 'knn'])
bar_xlabels = ['linear', 'lasso', 'knn']
N = len(bar_xlabels)
ind = np.arange(N)
width = 0.35
fig, ax = plt.subplots()
test_bar = ax.bar(ind, scores['test'], width, color='r')
train_bar = ax.bar(ind + width, scores['train'], width, color='y')
ax.set_xlabel('Models')
ax.set_ylabel('Scores')
ax.set_title('Models scores for train and test data')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(bar_xlabels)
ax.legend((test_bar, train_bar), ('test', 'train'))

#Manually choose features based on a abosulte correlation strength greater than 0.6
X_manual = []
for ob, over45, age39, age44, c, nb, nlb in zip(obese, plus45, age35_to_39, age40_to_44, caesar, no_birth, no_live_birth):
	X_manual.append([ob ,over45, age39, age44, c, nb, nlb])

#split the data into train and test for dataset X_manual and y
X_train, X_test, y_train, y_test = train_test_split(X_manual, y, random_state=0)

#Linear Regreesion
param_grid_linear = {'n_jobs': [1, 2, 3, 4, 5]}
grid = GridSearchCV(LinearRegression(), param_grid_linear, cv=5)
grid.fit(X_train, y_train)
#print('best parameters (number of jobs): {}'.format(grid.best_params_))
#n_jobs = 1
print('linear regression training score: {:.2f}'.format(grid.score(X_train, y_train)))
#linear training score: 1
print('linear regression test score: {:.2f}'.format(grid.score(X_test, y_test)))
#linear test score: 0.02
linear_train_score2 = grid.score(X_train, y_train)
linear_test_score2 = grid.score(X_test, y_test)

#Lasso Regression, constrain the unimportant features
param_grid_lasso = {'alpha': [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]}
grid_lasso = GridSearchCV(Lasso(), param_grid_lasso, cv=5)
grid_lasso.fit(X_train, y_train)
#print('best parameters (alpha): {}'.format(grid_lasso.best_params_))
# alpha = 100
print('lasso training score: {:.2f}'.format(grid_lasso.score(X_train, y_train)))
# lasso score = 1
print('lasso test score: {:.2f}'.format(grid_lasso.score(X_test, y_test)))
# lasso score = 0.27
lasso_train_score2 = grid_lasso.score(X_train, y_train)
lasso_test_score2 = grid_lasso.score(X_test, y_test)

#K Nearest Neighbors Regression
param_grid_neighbors = {'n_neighbors': [1, 2, 3, 4, 5]}
grid_neighbors = GridSearchCV(KNeighborsRegressor(), param_grid_neighbors, cv=5)
grid_neighbors.fit(X_train, y_train)
#print('best parameters: {}'.format(grid_neighbors.best_params_))
print('KNN training score: {:.2f}'.format(grid_neighbors.score(X_train, y_train)))
#KNN Training score: 1
print('KNN test score: {:.2f}'.format(grid_neighbors.score(X_test, y_test)))
#KNN Test score: 0.41
knn_train_score2 = grid_neighbors.score(X_train, y_train)
knn_test_score2 = grid_neighbors.score(X_test, y_test)

#plot 2nd scores
scores2 = pd.DataFrame({'train': [linear_train_score2, lasso_train_score2, knn_train_score2], 'test': [linear_test_score2, lasso_test_score2, knn_test_score2]}, index=['linear', 'lasso', 'knn'])
bar_xlabels2 = ['linear', 'lasso', 'knn']
N2 = len(bar_xlabels2)
ind2 = np.arange(N2)
width2 = 0.35
fig2, ax2 = plt.subplots()
test_bar2c= ax2.bar(ind2, scores2['test'], width2, color='r')
train_bar2 = ax2.bar(ind2 + width2, scores2['train'], width2, color='y')
ax.set_xlabel('Models')
ax.set_ylabel('Scores')
ax.set_title('Models scores for train and test data')
ax.set_xticks(ind2 + width2 / 2)
ax.set_xticklabels(bar_xlabels2)
ax.legend((test_bar2, train_bar2), ('test', 'train'))





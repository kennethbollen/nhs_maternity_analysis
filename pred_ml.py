#!python3

from data_extract import *
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

#a list of all the X variables
X_list = [smk, under ,obese, plus45, age35_to_39, age40_to_44, caesar, no_caesar, no_birth, no_live_birth]

#determine the correlation of each independent variable with the target variable
x_corr = []
for i in range(len(X_list)):
    x_corr.append(np.corrcoef(X_list[i], y)[0][1])
    
#plot the variables on a graph - create linear measure
fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10) = plt.subplots(2, 5)

slope_smk, int_smk = np.polyfit(smk, pre)
x_smk = np.array([min(smk), max(smk)])
y_smk = slope_smk * x_smk + int_smk
ax1.plot(smk, pre, marker='.', linestyle='none', color='r')
ax1.set_xlabel('mothers smoking')
ax1.set_ylabel('premature babies')
ax1.set_title('%s correlation' % round(x_corr[0], 2))
ax1.plot(x_smk, y_smk)

slope_under, int_under = np.polyfit(under, pre)
x_under = np.array([min(under), max(under)])
y_under = slope_under * x_under + int_under
ax2.plot(under, pre, marker='.', linestyle='none', color='r')
ax2.set_xlabel('mothers underweight')
ax2.set_ylabel('premature babies')
ax2.set_title('%s correlation' % round(x_corr[1], 2))
ax2.plot(x_under, y_under)

slope_obese, int_obese = np.polyfit(obese, pre)
x_obese = np.array([min(obese), max(obese)])
y_obese = slope_obese * x_obese + int_obese
ax3.plot(obese, pre, marker='.', linestyle='none', color='r')
ax3.set_xlabel('mothers obese')
ax3.set_ylabel('premature babies')
ax3.set_title('%s correlation' % round(x_corr[2], 2))
ax3.plot(x_obese, y_obese)

slope_age39, int_age39 = np.polyfit(age35_to_39, pre)
x_age39 = np.array([min(age35_to_39), max(age35_to_39)])
y_age39 = slope_age39 * x_age39 + int_age39
ax4.plot(age35_to_39, pre, marker='.', linestyle='none', color='r')
ax4.set_xlabel('mothers aged 35 to 39')
ax4.set_ylabel('premature babies')
ax4.set_title('%s correlation' % round(x_corr[3], 2))
ax4.plot(x_age39, y_age39)

slope_age44, int_age44 = np.polyfit(age40_to_44, pre)
x_age44 = np.array([min(age40_to_44), max(age40_to_44)])
y_age44 = slope_age44 * x_age44 + int_age44
ax5.plot(age40_to_44, pre, marker='.', linestyle='none', color='r')
ax5.set_xlabel('mothers aged 40 to 44')
ax5.set_ylabel('premature babies')
ax5.set_title('%s correlation' % round(x_corr[4], 2))
ax5.plot(x_age44, y_age44)

slope_plus45, int_plus45 = np.polyfit(plus45, pre)
x_plus45 = np.array([min(plus45), max(plus45)])
y_plus45 = slope_plus45 * x_plus45 + int_plus45
ax6.plot(plus45, pre, marker='.', linestyle='none', color='r')
ax6.set_xlabel('mothers +45 years')
ax6.set_ylabel('premature babies')
ax6.set_title('%s correlation' % round(x_corr[5], 2))
ax6.plot(x_plus45, y_plus45)

slope_caesar, int_caesar = np.polyfit(caesar, pre)
x_caesar = np.array([min(caesar), max(caesar)])
y_caesar = slope_caesar * x_caesar + int_caesar
ax7.plot(caesar, pre, marker='.', linestyle='none', color='r')
ax7.set_xlabel('mothers previous caesarian births')
ax7.set_ylabel('premature babies')
ax7.set_title('%s correlation' % round(x_corr[6], 2))
ax7.plot(x_caesar, y_caesar)

slope_no_caesar, int_no_caesar = np.polyfit(no_caesar, pre)
x_no_caesar = np.array([min(no_caesar), max(no_caesar)])
y_no_caesar = slope_no_caesar * x_no_caesar + int_no_caesar
ax8.plot(no_caesar, pre, marker='.', linestyle='none', color='r')
ax8.set_xlabel('mothers no previous caesarian births')
ax8.set_ylabel('premature babies')
ax8.set_title('%s correlation' % round(x_corr[7], 2))
ax8.plot(x_no_caesar, y_no_caesar)

slope_no_birth, int_no_birth = np.polyfit(no_birth, pre)
x_no_birth = np.array([min(no_birth), max(no_birth)])
y_no_birth = slope_no_birth * x_no_birth + int_no_birth
ax9.plot(no_birth, pre, marker='.', linestyle='none', color='r')
ax9.set_xlabel('mothers no previous births')
ax9.set_ylabel('premature babies')
ax9.set_title('%s correlation' % round(x_corr[8], 2))
ax9.plot(x_no_birth, y_no_birth)

slope_no_live_birth, int_no_live_birth = np.polyfit(no_live_birth, pre)
x_no_live_birth = np.array([min(no_live_birth), max(no_live_birth)])
y_no_live_birth = slope_no_live_birth * x_no_live_birth + int_no_live_birth
ax10.plot(no_live_birth, pre, marker='.', linestyle='none', color='r')
ax10.set_xlabel('mothers no previous live births')
ax10.set_ylabel('premature babies')
ax10.set_title('%s correlation' % round(x_corr[9], 2))
ax10.plot(x_no_live_birth, y_no_live_birth)

plt.show()

#supervised learning
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X_train, y_train)
print('Training score: {:.2f}'.format(knn.score(X_train, y_train)))
print('Test score: {:.2f}'.format(knn.score(X_test, y_test)))




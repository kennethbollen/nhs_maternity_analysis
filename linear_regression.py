import numpy as np
import matplotlib.pyplot as plt

from nhs_data7 import *
web_scrap_nhs(web_scrap)
create_lib_scrap(sites)
clean_data(df_dict)
premature_data(df_dict)

#setup the premature data
np_premature2 = np.array(np_premature)
pre = np.empty(len(np_premature2))
for i in np_premature2:
        np.append(pre, i)

#setup the smoking data
np_smoking2 = np.array(np_smoking)
smk = np.empty(len(np_smoking2))
for i in np_smoking2:
	np.append(smk, i)

#regression analysis
a, b = np.polyfit(smk, pre, 1)
#a 0.631736703899
#b -5032.53909527

#goodness of fit
print("min: ", np.min(smk), "max :", np.max(smk))
# min:  18797.0 max : 25441.0
x = np.array([18500, 25600])

#linear regression
y = a * x + b

#plotting the linear regression
_ = plt.plot(smk, pre, marker='.', linestyle='none', color='red')
plt.margins(0.02)
_ = plt.xlabel("Number of Mothers smoking during pregnancy")
_ = plt.ylabel("Number of Premature births (< 37 weeks)")
_ = plt.title("Does smoking lead to premature births?")
_ = plt.plot(x, y)
plt.show()

#create bootstrap replicates of the sample to test it out multiple times
#import the emprical cumlative distribution function
from emp_cum_dist_func2 import ecdf
#function to perform the pairs bootsrap for linear regression
from lin_reg_bs import draw_bs_pairs_linreg
#10000 bootstrap replicates of the mean
from bs_reps import *
bs_replicates = draw_bs_reps(pre, np.mean, 10000)
#standard error of the mean
sem = np.std(pre) / np.sqrt(len(np.sqrt(pre)))
print(sem)
#497.698905776
#standard deviation of bootstrap replicates
bs_std = np.std(bs_replicates)
print(bs_std)
#503.604220095

_ = plt.hist(pre, bins=50, normed=True)
_ = plt.xlabel("Number of premature births (< 37 weeks)")
_ = plt.ylabel("Probability Density Function (PDF)")
plt.show()
_ = plt.hist(bs_replicates, bins=50, normed=True)
_ = plt.xlabel("Number of premature births (< 37 weeks")
_ = plt.ylabel("Probability Density Function")
plt.show()
bs_replicates_smk = draw_bs_reps(smk, np.mean, 10000)
sem = np.std(smk) / np.sqrt(len(np.sqrt(smk)))
print(sem)
603.893265247
bs_std = np.std(smk)
print(bs_std)
2091.94763551
_ = plt.hist(bs_replicates_smk, bins=50, normed=True)
_ = plt.xlabel("Number of Mothers smoking during pregnancy")
_ = plt.ylabel("Probability Density Function")
plt.show()
#the mean is normally distributed
bs_replicates_pre_var = draw_bs_reps(pre, np.var, 10000)
_ = plt.hist(bs_replicates_pre_var, bins=50, normed=True)
_ = plt.xlabel("Number of premature births (< 37 weeks)")
_ = plt.ylabel("PDF")
plt.show()
#the variance of the premature data is slightly right skewed
bs_replicates_smk_var = draw_bs_reps(smk, np.var, size=10000)
_ = plt.hist(bs_replicates_smk_var, bins=50, normed=True)
_ = plt.xlabel("Number of Mothers smoking during pregnancy")
_ = plt.ylabel("PDF")
plt.show()
#the variance of the smoking data is slightly right skewed
conf_int_pre = np.percentile(bs_replicates, [2.5, 97.5])
conf_int_smk = np.percentile(bs_replicates_smk, [2.5, 97.5])
print(conf_int_pre)
[ 7970.89375     9947.66666667]
print(conf_int_smk)
[ 20941.79375  23292.55   ]
#The number of mothers smoking during a pregnancy in a 12 month period is between 20941 and 23292
#the number of premature births in a 12 month period is between 8000 and  10000
#pairs bootstrap
bs_slope_reps, bs_intercept_reps = draw_bs_pairs_linreg(smk, pre, size=1000)
#what is the 95th percentile confidence interval?
print(np.percentile(bs_slope_reps, [2.5, 97.5]))
[ 0.36194669  0.95071205]
_ = plt.hist(bs_slope_reps, bins=50, normed=True)
_ = plt.xlabel("slope")
_ = plt.ylabel("PDF")
plt.show()
#the slope is normally distributed
#plotting bootstrap regression
print(x)
[18500 25600]
print(np.max(bs_slope_reps))
1.26058460776
x = np.array([0,100])

for i in range(100):
	_ = plt.plot(x, bs_slope_reps[i]*x + bs_intercept_reps[i], linewidth=0.5, alpha=0.2, color='red')
	
_ = plt.plot(smk, pre, marker = '.', linestyle='none')
_ = plt.xlabel('smoking')
_ = plt.ylabel('premature')
plt.margins(0.02)
plt.show()


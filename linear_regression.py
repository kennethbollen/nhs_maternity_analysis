import numpy as np
import matplotlib.pyplot as plt
#import the emprical cumlative distribution function
from emp_cum_dist_func2 import ecdf
#function to perform the pairs bootsrap for linear regression
from lin_reg_bs import draw_bs_pairs_linreg
#bootstrap replicates
from bs_reps import *
#Pearson correlation
from p_corr import pearson_r

#Null: There is no relationship between smoking during pregnancy and premature births.
#Alterntive: There is a relationship between smoking during pregnancy and premature births.
#Significance level of 0.05 (95% confidence levels)

#determine slope and intercept
a, b = np.polyfit(smk, pre, 1)
#a 0.631736703899
#b -5032.53909527

#goodness of fit
print("min: ", np.min(smk), "max :", np.max(smk))
# min:  18797.0 max : 25441.0
x = np.array([18500, 25600])

#linear equation
y = a * x + b

#plotting the linear equation
_ = plt.plot(smk, pre, marker='.', linestyle='none', color='red')
plt.margins(0.02)
_ = plt.xlabel("Number of Mothers smoking during pregnancy")
_ = plt.ylabel("Number of Premature births (< 37 weeks)")
_ = plt.title("Does smoking lead to premature births?")
_ = plt.plot(x, y)
plt.show()
#plt_linreg.png

#create bootstrap replicates of the sample to test it out multiple times
#10000 bootstrap replicates of the mean
bs_replicates = draw_bs_reps(pre, np.mean, 10000)

#standard error of the mean
sem = np.std(pre) / np.sqrt(len(np.sqrt(pre)))
print(sem)
#506.969597513
#standard deviation of bootstrap replicates
bs_std = np.std(bs_replicates)
print(bs_std)
#508.696538502

#Probability density function of premature births
_ = plt.hist(bs_replicates, bins=50, normed=True)
_ = plt.xlabel("Number of premature births (< 37 weeks")
_ = plt.ylabel("Probability Density Function")
plt.show()
#pdf_pre.png

bs_replicates_smk = draw_bs_reps(smk, np.mean, 10000)
sem = np.std(smk) / np.sqrt(len(np.sqrt(smk)))
print(sem)
542.12294801
bs_std = np.std(smk)
print(bs_std)
1798.01840879
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

#Confidence intervals
conf_int_pre = np.percentile(bs_replicates, [2.5, 97.5])
conf_int_smk = np.percentile(bs_replicates_smk, [2.5, 97.5])
print(conf_int_pre)
#8651.81 and  10659.15
print(conf_int_smk)
#21849.45 and 23979.4

#pairs bootstrap
bs_slope_reps, bs_intercept_reps = draw_bs_pairs_linreg(smk, pre, size=1000)
#what is the 95th percentile confidence interval?
print(np.percentile(bs_slope_reps, [2.5, 97.5]))
#0.2380602 and 1.08508868
_ = plt.hist(bs_slope_reps, bins=50, normed=True)
_ = plt.xlabel("slope")
_ = plt.ylabel("PDF")
plt.show()
#pdf_slop.png
#the slope is right-skewed

#plotting bootstrap regression
print(x)
#18500 and 25600
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

pearson_r(smk, pre)
#0.68957787487139965
#The observed correlation between mothers who smoke during their pregnancy and premature births may just be by chance and that premature births are independent from smoking. Need to conduct a null hypothsis to determine
#To do the test, I will simulate the data assuming the null hypothesis is true
#Premutation test: Premute the smoking during pregnancy values but will leave the premature births values fixed to generate a new set of data
r_observed = pearson_r(smk, pre)
#initialize an array to store premutation replications
perm_replicates = np.empty(10000)
for i in range(10000):
	smk_permuted = np.random.permutation(smk)
	perm_replicates[i] = pearson_r(smk_permuted, pre)

p = np.sum(perm_replicates >= r_observed) / len(perm_replicates)
print('p-val = ', p)
#p-val = 0.0114
#significance level of 0.05 > p-value of 0.0114
#reject the null hypthosis

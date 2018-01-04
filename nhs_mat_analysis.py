
import statsmodels.api as sm
import matplotlib.pyplot as plt 
import numpy as np

#EDA on the relationship between smoking during pregnancy and premature births
slope, intercept = np.polyfit(smk, pre)
x = np.array([min(smk), max(smk)])
y = slope * x + intercept
_ = plt.plot(smk, pre, marker='.', linestyle='none', color='red')
plt.margins(0.02)
_ = plt.xlabel('Number of women smoking during pregnancy')
_ = plt.ylabel('Number of premature births')
_ = plt.title('Relationship between premature births and smoking during pregnancy')
_ = plt.plot(x, y)
plt.show()
#Scatterplot shows there is a postive linear relationship between smoking during pregnancy and premature births

#Statistical analysis on the relationship between smoking during pregnancy and premature births
#Null Hypothesis: Smoking during pregnancy has no effect on premature births
#Alterntive Hypothesis: Smoking during prgnancy has a effect on premature births

X = sm.add_constant(smk)
est = sm.OLS(pre, X).fit()
est.summary()
#R-Squared: Smoking during pregnancy only explains 43% of the vairance found i 
#Smoking coefficient: +1 smoking mother increase premature births by 0.6907
#Confidence interval: model predicts at a 97.5% confidence that the value of smoking is between 0.133 and 1.248
#At a 95% confidence level and p-value of 0.02 < alpha 0.05, which is statistically significant, we can reject the null hypothesis

#Would adding the variable BMI (underweight) better explain the reasons for premature births?
#Null Hypothesis: Smoking during pregnancy and being underweight has no effect on premature births
#Alterntive Hypothesis: Smoking during pregnancy and being underweight has an effect on premature births

x = []
for s, b in zip(smk, bmi):
  x.append([s,b])
  
X = sm.add_constant(x)
est = sm.OLS(pre, X).fit()
est.summary()
#Smoking coefficient: +1 smoking mother increase premature births by +0.8628
#BMI coefficient: +1 underweight mother increases premature births by +0.6802
#R-squared: Model explains 78% of the variance, 22% of the variance not captured by Smoking or BMI
#Confidence interval: model predicts at a 97.5% confidence that the value of smoking is between 0.478 and 1.247 and BMI is between -1.087 and -0.274
#Smoking p-value 0.001 < alpha 0.05, statistically significant, reject null
#BMI (underweight) p-value 0.004 < alpha 0.05, statistically significant, reject null



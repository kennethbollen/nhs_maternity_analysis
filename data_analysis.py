#independent variable is mothers who smoking and dependent variable is premature babies
#first step is to conduct EDA
import matplotlib.pyplot as plt
from p_corr import *

#scatter plot the two variables to see if there is a relationship
_ = plt.plot(np_smoking2, np_premature2, marker='.', linestyle='none', color='red')
plt.margins(0.02)
_ = plt.xlabel('Number of mothers that smoke before birth')
_ = plt.ylabel('Number of premature births < 37 weeks')
# np.polyfit() allows us to calculate the slope and the intercept
a, b = np.polyfit(np_smoking2, np_premature2, 1)
print('slope =', a, 'Premature births per mother / Smoking Mothers')
#PRINT: slope = 0.631736703899 Premature births per mother / Smoking Mothers
print('intercept =', b, 'Premature births per mother')
#PRINT: intercept = -5032.53909527 Premature births per mother
x = np.array([17000, 26000])
y = a * x + b
_ = plt.plot(x, y)
plt.show()

#Relationship between being underweight and premature births
>>> a, b = np.polyfit(bmi, pre, 1)
>>> print("min: ", np.min(bmi), "max: ", np.max(bmi))
min:  9623.0 max:  15105.0
x = np.array([9500, 15200])
y = a * x + b
_ = plt.plot(bmi, pre, marker='.', linestyle='none', color='red')
plt.margins(0.02)
_ = plt.xlabel("Number of Mothers Underweight(BMI) Giving Birth")
_ = plt.ylabel("Premature Births in the U.K (< 37 Weeks)")
_ = plt.title("Relationship between BMI and Premature Births in the U.K")
_ = plt.plot(x, y)
plt.show()

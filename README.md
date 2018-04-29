Causes of Premature births in the U.K
=======================================
Project that used the NHS maternity statistics to research the causes of premature births in the U.K for the past 18 months

Overview
----------
Languages: Python 3
Source: https://digital.nhs.uk/data-and-information/publications/statistical/maternity-services-monthly-statistics
Time period: April 2015 - January 2018
Time of analysis: January 2018 - April 2018
Packages used: pandas, numpy, requests, re, bs4, sklearn, matplotlib

Data Extract (data_extract.py)
-------------------------------
File provides code used to web scrap 2.5 years of data from NHS maternity website. Data collection was focused on premature birth rates, smoking habits of pregnant women, age profile of pregnant women and pregnancy history. All data was anonymized and aggregated at a national level

Data Analysis (data_analysis.py)
--------------------------------
File provides code used to calculate correlation between variables and EDA on their linear relationships. Additionally, code contains predictive modelling on the data set.

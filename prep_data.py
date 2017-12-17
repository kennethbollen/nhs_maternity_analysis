#! python3

import pandas as pd
import numpy as np
import re

np_premature = []
np_smoking = []
np_bmi = []
df_dict = {}

def create_lib(df_list):
    for i in range(len(df_list)):
        df_dict["df_%s" %str(i)] = df_list[i]
        print("creating file df_%s" %str(i))
        print()
    print("finished creating files \nCreated %s files" %str(len(df_list)))
    
def clean_data(df_dict):
    for k, v in df_dict.items():
        #remove values with an astrik and replace with a zero
        print("Cleaning data for %s..." %str(k))
        print()
        for i in df_dict[k]["Value"]:
            if i == "*":
                x = df_dict[k].index[df_dict[k]["Value"] == i].tolist()
                df_dict[k]["Value"][x[0]] = str(0)

    for k, v in df_dict.items():
        print("Removing thousand separators for %s..." %str(k))
        print()
        for i in df_dict[k]["Value"]:
            #remove the thousand separator
            if re.search(",",i) is not None:
                #find the index of the value with the thousand separator
                x = df_dict[k].index[df_dict[k]["Value"] == i].tolist()
                #remove the thousand separtor with
                y = re.sub(",","",i)
                #replace the thousand separtor value with a clean value
                df_dict[k]["Value"][x[0]] = y 

    for k, v in df_dict.items():
        #convert strings into floats
        print("Amending data types for %s..." %str(k))
        print()
        df_dict[k]["Value"] = df_dict[k]["Value"].astype("float")
    print("Completed cleaning for %s files..." %str(len(df_dict)))

def premature_data(df_dict):
    global np_premature
    counter = 0
    for k, v in df_dict.items():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "< 37 weeks", :].groupby("Measure")["Value"].sum()
        np_premature.append(i.values)
        print("Parsing premature dataset %s..." %str(counter))
    print()
    print("Completed Premature Data")

def smoking_data(df_dict):
    global np_smoking
    counter = 0
    for k, v in df_dict.dict():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "Smoker", :].groupby("Measure")["Value"].sum()
        np_smoking.append(i.values)
        print("Parsing smoking dataset %s..." %str(counter))
    print()
    print("Completed Smoking Data")

def bmi_data(df_dict):
    global np_bmi
    counter = 0
    for k, v in df_dict.items():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "Underweight", :].groupby("Measure")["Value"].sum()
        np_bmi.append(i.values)
        print("Parsing BMI dataset %s..." %str(counter))
    print()    
    print("Completed BMI Data")

#how many datasets contain data on premature births?
premature_data(df_dict)
np_premature2 = np.array(np_premature)
for i in range(len(df_dict)):
	print("df_%s: "  %str(i), np_premature2[i])
    
#answer: 12 datasets from df_0 to df_11
#trim the array to only the 11 data points
np_premature3 = np.array(np_premature2[:11])
pre = np.empty(len(np_premature3))
for i in np_premature3:
    np.append(pre, i)
            
#prepare the smoking data
smoking_data(df_dict)
np_smoking2 = np.array(np_smoking[:11])
smk = np.empty(len(np_smoking2))
for i in np_smoking2:
    np.append(smk, i)
               
#data preparation complete and now EDA

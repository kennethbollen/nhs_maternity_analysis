#python3!

import pandas as pd
import numpy as np

months = ["jul16","aug16","sep16","oct16","nov16","dec16","jan17","feb17","mar17", "apr17","may17","jun17"]
files = []
np_premature = []
np_smoking = []
np_bmi = []

#load data
def upload_csv(lis_months):
    global files    
    for month in months:
        df = pd.read_csv("/Users/2024450/Documents/Stats/msms-%s-exp-data.csv" % month)
        files.append(df)

def clean_data(df_list):
    for i in df_list:
        print("Cleaning data for %s..." %str(df_list))
        print()
        i.loc[i["Value"] == "*", :] = 0
        print("Amending data types...")
        print()
        i["Value"] = i["Value"].astype("float")
    print("Completed cleaning for %s files" %str(len(df_list)))

def premature_data(df_list):
    global np_premature
    for i in df_list:    
        pre = i.loc[i["Measure"] == "< 37 weeks", :].groupby("Measure")["Value"].sum()
        np_premature = np.append(np_premature, pre.values)

    print("Completed Premature Data")
    return(np_data)

def smoking_data(df_list):
    global np_smoking
    for i in df_list:    
        smk = i.loc[i["Measure"] == "Smoker", :].groupby("Measure")["Value"].sum()
        np_smoking = np.append(np_smoking, smk.values)

    print("Completed Smoking Data")
    return(np_smoking)

def bmi_data(np_data):
    global np_bmi
    for i in df_list:    
        bmi = i.loc[i["Measure"] == "Underweight", :].groupby("Measure")["Value"].sum()
        np_bmi = np.append(np_bmi, bmi.values)

    print("Completed BMI Data")
    return(np_bmi)

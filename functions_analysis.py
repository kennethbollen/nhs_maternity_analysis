#python3!

import pandas as pd
import numpy as np
import re

months = ["jul16","aug16","sep16","oct16","nov16","dec16","jan17","feb17","mar17", "apr17","may17","jun17"]
files = []
np_premature = []
np_smoking = []
np_bmi = []
df_dict = {}

#load data
def upload_csv(lis_months):
    global files    
    for month in months:
        print("Uploading %s..." % month)
        print()
        df = pd.read_csv("/Users/2024450/Documents/Stats/msms-%s-exp-data.csv" % month)
        files.append(df)

def create_lib(lis_files):
    for i in range(len(lis_files)):
        df_dict["df_%s" %str(i)] = files[i]
        print("creating file df_%s" %str(i))
        print()
    print("finished creating files \nCreated %s files" %str(len(lis_files)))
    
def clean_data(df_lib):
    for k, v in df_lib.items():
        print("Cleaning data for %s..." %str(df_lib[k]))
        print()
        df_lib[k].loc[df_lib[k]["Value"] == "*",:]
        print("Removing thousand separators...")
        print()
        for i in df_lib[k]["Value"]:
            re.sub(",","",i)
        print("Amending data types...%s" %str(df_lib))
        print()
        df_lib[k]["Value"] = df_lib[k]["Value"].astype("float")
    print("Completed cleaning for %s files" %str(len(df_lib[k])))

def premature_data(df_lib):
    global np_premature
    for k, v in df_lib.items():    
        pre = df_lib[k].loc[df_lib[k]["Measure"] == "< 37 weeks", :].groupby("Measure")["Value"].sum()
        np_premature = np.append(np_premature, pre.values)

    print("Completed Premature Data")
    return(np_data)

def smoking_data(df_lib):
    global np_smoking
    for k, v in df_lib.items():    
        smk = df_lib[k].loc[i["Measure"] == "Smoker", :].groupby("Measure")["Value"].sum()
        np_smoking = np.append(np_smoking, smk.values)

    print("Completed Smoking Data")
    return(np_smoking)

def bmi_data(df_lib):
    global np_bmi
    for k, v in df_lib.items():    
        bmi = df_lib[k].loc[i["Measure"] == "Underweight", :].groupby("Measure")["Value"].sum()
        np_bmi = np.append(np_bmi, bmi.values)

    print("Completed BMI Data")
    return(np_bmi)

#python3!

import pandas as pd
import numpy as np
import re

months = ["jul16","aug16","sep16","oct16","nov16","dec16","jan17","feb17","mar17", "apr17","may17","jun17"]
web_scrap = ["https://digital.nhs.uk/media/30069/Maternity-Services-Monthly-Statistics-England-July-2016-Experimental-statistics-CSV-data/Any/msms-jul16-exp-data","https://digital.nhs.uk/media/30335/Maternity-Services-Monthly-Statistics-England-August-2016-Experimental-statistics-CSV-Data/Any/msms-aug16-exp-data","https://digital.nhs.uk/media/30464/Maternity-Services-Monthly-Statistics-England-September-2016-Experimental-statistics-CSV-data/Any/msms-sep16-exp-data","https://digital.nhs.uk/media/30588/Maternity-Services-Monthly-Statistics-England-October-2016-Experimental-statistics-CSV-data/Any/msms-oct16-exp-data","https://digital.nhs.uk/media/30796/Maternity-Services-Monthly-Statistics-England-November-2016-Experimental-statistics-CSV-data/Any/msms-nov16-exp-data","https://digital.nhs.uk/media/30896/Maternity-Services-Monthly-Statistics-England-December-2016-Experimental-statistics-CSV-data/Any/msms-dec16-exp-data","https://digital.nhs.uk/media/31102/Maternity-Services-Monthly-Statistics-England-January-2017-Experimental-statistics-CSV-data/default/msms-jan17-exp-data","https://digital.nhs.uk/media/31446/Maternity-Services-Monthly-Statistics-England-February-2017-Experimental-statistics-CSV-data/default/msms-feb17-exp-data","https://digital.nhs.uk/media/31849/Maternity-Services-Monthly-Statistics-England-March-2017-Experimental-statistics-CSV-data/xls/msms-mar17-exp-data","https://digital.nhs.uk/media/32368/Maternity-Services-Monthly-Statistics-England-April-2017-Experimental-statistics-CSV-data/default/msms-apr17-exp-data","https://digital.nhs.uk/media/32951/Maternity-Services-Monthly-Statistics-England-May-2017-Experimental-statistics-CSV-data/default/msms-may17-exp-data","https://digital.nhs.uk/media/33526/Maternity-Services-Monthly-Statistics-England-June-2017-Experimental-statistics-CSV-data-/default/msms-jun17-exp-data"]
files = []
sites = []
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

def web_scrap_nhs(lis_months):
    global sites    
    for i in web_scrap:
        print("Uploading scrapping...")
        print()
        df = pd.read_csv(i)
        sites.append(df)

def create_lib(lis_files):
    for i in range(len(lis_files)):
        df_dict["df_%s" %str(i)] = files[i]
        print("creating file df_%s" %str(i))
        print()
    print("finished creating files \nCreated %s files" %str(len(lis_files)))
    
def clean_data(df_lib):
    for k, v in df_lib.items():
        #remove values with an astrik and replace with a zero
        print("Cleaning data...")
        print()
        for i in df_lib[k]["Value"]:
            if i == "*":
                x = df_lib[k].index[df_lib[k]["Value"] == i].tolist()
                df_lib[k]["Value"][x[0]] = str(0)

    for k, v in df_lib.items():
        print("Removing thousand separators...")
        print()
        for i in df_lib[k]["Value"]:
            #remove the thousand separator
            if re.search(",",i) is not None:
                #find the index of the value with the thousand separator
                x = df_lib[k].index[df_lib[k]["Value"] == i].tolist()
                #remove the thousand separtor with
                y = re.sub(",","",i)
                #replace the thousand separtor value with a clean value
                df_lib[k]["Value"][x[0]] = y 

    for k, v in df_lib.items():
        #convert strings into floats
        print("Amending data types...")
        print()
        df_lib[k]["Value"] = df_lib[k]["Value"].astype("float")
    print("Completed cleaning for %s files..." %str(len(df_lib[k])))

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

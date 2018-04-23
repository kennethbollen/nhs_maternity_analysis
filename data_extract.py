#!python3

import requests
import bs4
import re
import pandas as pd
import numpy as np

base_url = 'https://digital.nhs.uk'
maternity_hyplink = []
wp_num = []
csv_links = []
df_list = []
np_premature = []
np_smoking = []
np_bmi_under = []
np_bmi_obese = []
mother_age_35_to_39 = []
mother_age_40_to_44 = []
np_age_45plus = [] 
prev_caesarean = []
no_prev_birth = []
no_prev_live_birth = []
prev_birth = []
df_dict = {}

home_url = base_url + '/data-and-information/publications/statistical/maternity-services-monthly-statistics'
req = requests.get(home_url)
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text, 'lxml')

'''
#determine how many web page numbers to be looped through
for link in soup.find_all('a', href=True):
	if re.search('Last', link.text) is not None:
		last = link['href'].split("=")
		last[-1] = int(last[-1])
		wp_num = last[-1]
		print("There are %s pages to scrap" %last[-1])
		print()
'''

#collect urls
for link in soup.find_all('a', href=True):
	if re.search("Maternity Services Monthly Statistics, England.", link.text) is not None:
		maternity_hyplink.append(base_url + link['href'])
			
#collect the csv files
for hyplink in maternity_hyplink:
	req = requests.get(hyplink)
	req.raise_for_status()
	soup = bs4.BeautifulSoup(req.text, 'lxml')
	for link in soup.find_all('a', href=True):
		if re.search(".CSV data", link.text) is not None:
			csv_links.append(link['href'])
			
#convert csv files into dataframes
for csv in csv_links:
	print("Converting:\n %s" %csv)
	df = pd.read_csv(csv)
	df_list.append(df)
	
#next: clean data
def create_lib(df_list):
    for i in range(len(df_list)):
        #extract the df from list to dict
        #filter only the data from org level of nhs national to avoid duplications
        try:
                df_dict["df_%s" %str(i)] = df_list[i].loc[df_list[i]["Org_Level"] == "National",:]
                print("creating file df_%s" %str(i))
                print()
        except:
                print("df_%s has no org_level data" %str(i))
    print("finished creating files \nCreated %s files" %str(len(df_list)))

create_lib(df_list)
    
def clean_data(df_dict):
    for k, v in df_dict.items():
        #remove values with an astrik and replace with a zero
        for i in df_dict[k]["Value"]:
            if i == "*":
                x = df_dict[k].index[df_dict[k]["Value"] == i].tolist()
                df_dict[k]["Value"][x[0]] = str(0)
		
    for k, v in df_dict.items():
        #replace age 35-39 with 35 to 39
        for i in df_dict[k]["Measure"]:
            if i == "35-39":
                x = df_dict[k].index[df_dict[k]["Measure"] == i].tolist()
                df_dict[k]["Measure"][x[0]] = "35 to 39"
	
    for k, v in df_dict.items():
        #replace age 40-44 with 40 to 44
        for i in df_dict[k]["Measure"]:
            if i == "40-44":
                x = df_dict[k].index[df_dict[k]["Measure"] == i].tolist()
                df_dict[k]["Measure"][x[0]] = "40 to 44" 
		
    for k, v in df_dict.items():
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
        df_dict[k]["Value"] = df_dict[k]["Value"].astype("float")
    print("Completed cleaning for %s files..." %str(len(df_dict)))

clean_data(df_dict)

def premature_data(df_dict):
    counter = 0
    for k, v in df_dict.items():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "< 37 weeks", :].groupby("Measure")["Value"].sum()
        np_premature.append(i.values)

def smoking_data(df_dict):
    counter = 0
    for k, v in df_dict.items():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "Smoker", :].groupby("Measure")["Value"].sum()
        np_smoking.append(i.values)

def bmi_under(df_dict):
    counter = 0
    for k, v in df_dict.items():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "Underweight", :].groupby("Measure")["Value"].sum()
        np_bmi_under.append(i.values)

def bmi_obese(df_dict):
    counter = 0
    for k, v in df_dict.items():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "Obese", :].groupby("Measure")["Value"].sum()
        np_bmi_obese.append(i.values)

def mother_age_45plus(df_dict):
    counter = 0
    for k, v in df_dict.items():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "45 or Over", :].groupby("Measure")["Value"].sum()
        np_age_45plus.append(i.values)

def mother_age_35_to_39(df_dict):
    counter = 0
    for k, v in df_dict.items():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "35 to 39", :].groupby("Measure")["Value"].sum()
        mother_age_35_to_39.append(i.values)
	
def mother_age_40_to_44(df_dict):
    counter = 0
    for k, v in df_dict.items():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "40 to 44", :].groupby("Measure")["Value"].sum()
        mother_age_40_to_44.append(i.values)

def prev_caesarean(df_dict):
    counter = 0
    for k, v in df_dict.items():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "At least one Caesarean", :].groupby("Measure")["Value"].sum()
        prev_caesarean.append(i.values)
	
def prev_birth_no_caesarean(df_dict):
    counter = 0
    for k, v in df_dict.items():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "At least one Previous Birth, zero Caesareans", :].groupby("Measure")["Value"].sum()
        prev_birth.append(i.values)

def no_prev_birth(df_dict):
    counter = 0
    for k, v in df_dict.items():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "Zero Previous Births", :].groupby("Measure")["Value"].sum()
        no_prev_birth.append(i.values)
	
def no_prev_live_birth(df_dict):
    counter = 0
    for k, v in df_dict.items():
        counter += 1
        i = df_dict[k].loc[df_dict[k]["Measure"] == "No previous live births", :].groupby("Measure")["Value"].sum()
         no_prev_live_birth.append(i.values)
	
#how many datasets contain data on premature births?

premature_data(df_dict)
print(np_premature)
print()
num_data = np.count_nonzero(np_premature)
np_premature2 = np.array(np_premature[:num_data])
print(np_premature2)
print()
pre = np.empty(len(np_premature2))
for i in np_premature2:
	np.append(pre, i)
print(pre)
print()
	
#prepare the smoking data
smoking_data(df_dict)
print(np_smoking)
print()
np_smoking2 = np.array(np_smoking[:num_data])
print(np_smoking2)
print()
smk = np.empty(len(np_smoking2))
for i in np_smoking2:
    np.append(smk, i)
print(smk)
print()

bmi_data(df_dict)
print(np_bmi)
print()
np_bmi2 = np.array(np_bmi[:num_data])
print(np_bmi2)
print()
bmi = np.empty(len(np_bmi2))
for i in np_bmi2:
	np.append(bmi, i)
print(bmi)

#data preparation complete and now EDA'''

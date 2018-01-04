#! python3
"""web scrapping and data cleaning"""
import requests
import bs4
import re
import pandas as pd
import numpy as np

#web scrapping 
maternity_hyplink = []
wp_num = []
csv_links = []
df_list = []

#data cleaning
np_premature = []
np_smoking = []
np_bmi = []
df_dict = {}

#data source
url = 'https://digital.nhs.uk/article/4375/Public-health'
req = requests.get(url)
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text)

#determine how many web page numbers to be looped through
for link in soup.find_all('a', href=True):
	if re.search('Last', link.text) is not None:
		last = link['href'].split("=")
		last[-1] = int(last[-1])
		wp_num = last[-1]
		print("There are %s pages to scrap" %last[-1])
		print()
		
#loop through the web pages scrapping the data
for i in range(1, wp_num + 1):
	#find the hyperlinks for the web pages that contain the maternity data
	url = requests.get("https://digital.nhs.uk/article/4375/Public-health?p=%s" %i)
	url.raise_for_status()
	soup = bs4.BeautifulSoup(url.text)
	for link in soup.find_all('a', href=True):
		if re.search("Maternity Services Monthly Statistics, England.", link.text) is not None:
			maternity_hyplink.append(link['href'])
			print("Collecting Hyperlink: %s" %link.text)
			print()

#collect the csv files
for hyplink in maternity_hyplink:
	req = requests.get(hyplink)
	req.raise_for_status()
	soup = bs4.BeautifulSoup(req.text)
	for link in soup.find_all('a', href=True):
		if re.search(".CSV data", link.text) is not None:
			csv_links.append(link['href'])
			print("Collecting CSV: %s" %link.text)
			print()
			
#convert csv files into dataframes
for csv in csv_links:
	print("Converting: %s" %csv)
	df = pd.read_csv(csv)
	df_list.append(df)
	
#clean data

#creating a dictionary to hold dataframes
def create_lib(df_list):
    for i in range(len(df_list)):
        df_dict["df_%s" %str(i)] = df_list[i]
        print("creating file df_%s" %str(i))
        print()
    print("finished creating files \nCreated %s files" %str(len(df_list)))

create_lib(df_list)

#remove strings from 
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

clean_data(df_dict)

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
    for k, v in df_dict.items():
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

premature_data(df_dict)
print(np_premature)
print()
np_premature2 = np.array(np_premature[:12])
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
np_smoking2 = np.array(np_smoking[:12])
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
np_bmi2 = np.array(np_bmi[:12])
print(np_bmi2)
print()
bmi = np.empty(len(np_bmi2))
for i in np_bmi2:
	np.append(bmi, i)
print(bmi)

#data preparation complete and now EDA

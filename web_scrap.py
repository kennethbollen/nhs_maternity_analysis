#! python3
"""web scrapping maternity nhs data"""
import requests
import bs4
import re
import pandas as pd

maternity_hyplink = []
wp_num = []
csv_links = []
df_list = []

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
	
print("next: clean data")

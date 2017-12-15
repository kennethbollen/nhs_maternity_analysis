#! python3
"""web scrapping maternity nhs data"""
import requests
import bs4

maternity_hyplink = []
        
for i in range(1,4):
	#find the hyperlinks for the web pages that contain the maternity data
    url = requests.get("https://digital.nhs.uk/article/4375/Public-health?p=%s" %i)
	url.raise_for_status()
	soup = bs4.BeautifulSoup(url.text)
	for link in soup.find_all('a', href=True):
		if re.search("Maternity Services Monthly Statistics, England.", link.text) is not None:
			maternity_hylink.append(link['href'])

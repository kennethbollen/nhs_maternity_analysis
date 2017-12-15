#! python3
"""web scrapping maternity nhs data"""
import requests
import bs4

#access the website
url = requests.get('https://digital.nhs.uk/article/4375/Public-health')
url.raise_for_status()
soup = bs4.BeautifulSoup(url.text)

#find the hyperlinks for the web pages that contain the maternity data

maternity_hyplink = []

for link in soup.find_all('a', href=True):
    #regex to search html for hyperlinks with the link text for maternity web pages using a wildcard
    if re.search("Maternity Services Monthly Statistics, England.", link.text) is not None:
        #for each hyperlink, append to the list maternity_hylink and strip whitespace
        maternity_hylink.append(link['href'])

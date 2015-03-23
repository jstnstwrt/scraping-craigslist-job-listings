import requests
from bs4 import BeautifulSoup
import re


## setting the url for job search on craigslist
url = "http://newyork.craigslist.org/search/jjj"
base_url = 'http://newyork.craigslist.org'


r = requests.get(url)

## parsing the page source into usable data
soup = BeautifulSoup(r.content)


## collecting all the paragraph tags in the page source
g_data = soup.find_all("p",{"class": "row"})


## 
cl_listings = []

for item in g_data:
	
	listing_element = str(item.find_all('a',{"class":"hdrlnk"}))
	link_start = listing_element.find('href="') + len('href="')
	link_end = listing_element.find('"',link_start)
	link = listing_element[link_start:link_end]
	

	cl_listings.append(base_url+link)


print cl_listings

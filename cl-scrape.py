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
cl_data = soup.find_all("p",{"class": "row"})


## creating a list to store the data
cl_listings = []


# looping through the cl data
for item in cl_data:

	#identifying the link to the job listing
	title_start = listing_element.find('>')+1
	title_end = listing_element.find('<',title_start)
	title = listing_element[title_start:title_end]
	
	#identifying the link to the job listing
	listing_element = str(item.find_all('a',{"class":"hdrlnk"}))
	link_start = listing_element.find('href="') + len('href="')
	link_end = listing_element.find('"',link_start)
	link = listing_element[link_start:link_end]

	#getting the text content from the listing
	r2 = requests.get(base_url + link)
	soup2 = BeautifulSoup(r2.content)
	listing_content_element = str(soup2.find("section",{"id":"postingbody"}))
	listing_content_start = len('<section id="postingbody">')
	listing_content_end = listing_content_element.find('</section>',listing_content_start)
	listing_content = listing_content_element[listing_content_start:listing_content_end]
	



	cl_listings.append(base_url+link)


print cl_listings

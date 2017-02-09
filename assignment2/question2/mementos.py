import urllib2
from bs4 import BeautifulSoup
import requests


file = open('uris.txt', 'r')
urls =[]

for url in file:
    urls.append(url)

    try:
        resp = urllib2.urlopen('http://memgator.cs.odu.edu/timemap/link/'+url)
        html = resp.read()
        soup = BeautifulSoup(html, "html.parser")
		for mementos in soup.find_all('rel'):
			
			
			
	
		
    except:
        continue

file.close()


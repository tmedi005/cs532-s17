from bs4 import BeautifulSoup
import urllib2
import urlparse
import requests
import sys

#get url as argument 
if __name__ == "__main__":

	for arg in sys.argv[1:]:
		arg = param
		
	#param = "http://www.cs.odu.edu/~mln/teaching/"
	#param - param = "http://www.cs.odu.edu/~mln/pubs/all.html"

#url to test
	param = "http://www.cs.odu.edu/~mln/teaching/cs532-s17/test/pdfs.html"
		
        

	#open url 
	website = urllib2.urlopen(param)
	websiteHtml = website.read()
	
	#fetch all links(wasn't sure about html.parser but my compiler kept throwing me back
	#error warnings about it, so I threw it in
	soup = BeautifulSoup(websiteHtml, 'html.parser')

        #find all 'a' tags in the html to identify links
	for linkList in soup.find_all('a'):
                #get the links
		link = linkList.get('href')
		        
		#get header info	
		resp = urllib2.urlopen(link)
		data = resp.info();
		content = data.getheader('Content-Type')
			
                        			
			

                        #only prints pdf content types along with their size in bytes
		if content == "application/pdf" :
			size = data.getheader('content-length')
			print link, "\n", "Size =", size, "bytes\n"
                                




#just practice down here
"""
r = requests.get("http://www.cs.odu.edu/~mln/teaching/cs532-s16/test/pdfs.html")

resp = requests.head("http://www.cs.odu.edu/~mln/teaching/cs532-s16/test/pdfs.html")
#print resp.headers
print resp.headers['Content-Type']
print resp.headers['date']
if resp.headers['Content-Type'] == "application/pdf":
"""


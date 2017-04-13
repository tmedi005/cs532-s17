import sys
import os
import os.path
import feedparser
import urllib2
import time
import chardet
import argparse
from bs4 import BeautifulSoup

def dereferenceUri(uri):

    pagehandle = urllib2.urlopen(uri)
    pagedata = pagehandle.read()
    derefurl = pagehandle.geturl()
    pagehandle.close()

    return pagedata,derefurl

def getAtomFeedUri(html):

    soup = BeautifulSoup(html,'html') 

    atomLinks = soup.find_all('link',
        attrs = { 'rel' : 'alternate', 'type' : 'application/atom+xml' })

    atomURI = atomLinks[0].attrs['href']

    return atomURI

def meetsCriteria(feedText):

    parsedData = feedparser.parse(feedText)

    goodToGo = True

    sys.stderr.write("blog has " + str(len(parsedData.entries)) + " entries\n")

    if (len(parsedData.entries) < 25):
        goodToGo = False        

    return goodToGo

def getNextUri():

    uri = "http://www.blogger.com/next-blog?navBar=true&blogID=30361063" 

    pagehandle = urllib2.urlopen(uri)
    nexturi = pagehandle.geturl()
    pagehandle.close() 

    return nexturi


if __name__ == "__main__":

    feedlist = []
    feedlist.append("http://f-measure.blogspot.com/feeds/posts/default?max-results=200")
    feedlist.append("http://ws-dl.blogspot.com/feeds/posts/default?max-results=200")
 

    uriList = []
    while (len(feedlist) <= 100):
        out = open('../blogList.txt','w+')
        for link in feedlist:
            out.write(link)
            out.write('\n')
        out.close()

        try:
            uri = getNextUri()
            print("Getting unique uri")
            while len(list(filter(lambda x: x == uri,uriList))) != 0:
                uri = getNextUri()
            uriList.append(uri)
        except urllib2.HTTPError as e:
            sys.stderr.write("failed to acquire next uri, delaying 5 seconds\n")
            time.sleep(5)
        else:
            sys.stderr.write("\n" + "working on URI " + uri + "\n")
    
            try:
                html,derefuri = dereferenceUri(uri)
            except urllib2.HTTPError as e:
                sys.stderr.write("failed to dereference " + uri +
                    ", delaying 5 seconds\n")
                time.sleep(5)
            else:
                try:
                    feedURI = getAtomFeedUri(html)
                    sys.stderr.write("acquired feed URI " + feedURI + "\n")
                except IndexError as e:
                    sys.stderr.write(
                        "failed to acquire Atom feed from HTML, delaying 5 seconds\n \n")
                else:
                    try:
                        feedText,feedURI = dereferenceUri(feedURI)
                    except urllib2.HTTPError as e:
                        sys.stderr.write("failed to dereference " + feedURI +
                            ", delaying 5 seconds\n")
                        time.sleep(5)
                    else:
                        if meetsCriteria(feedText):
                            
                            sys.stderr.write("Saving blog feed " + feedURI + "?max-results=1000\n")
                            feedlist.append(feedURI + "?max-results=1000")
        
                        time.sleep(1)

    for feed in feedlist:
        print feed
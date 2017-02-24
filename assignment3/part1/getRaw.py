import urllib2
import sys
import re


def getHtml(uri):
	resp = urllib2.urlopen(uri)
	html = resp.read()
	return html

if __name__ == "__main__":

	with open('links.txt', 'r') as input:
		for index, line in enumerate(input):
			with open('uri_raw{}.txt'.format(index), 'w') as output:
				raw = getHtml(line)
				output.write(raw)
				output.close()
	
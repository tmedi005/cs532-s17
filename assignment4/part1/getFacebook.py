import xml.etree.ElementTree as ET 
from xml.dom import minidom
import sys

def getFriend(node):
	Friend = {}
	elements = node.getElementsByTagName('data')
	
	for element in elements:
		Friend[element.attributes['key'].value] = element.firstChild.data
	return Friend


def getAttributes(file):
	friendList = {}
	xml = minidom.parse(file)
	friends = xml.getElementsByTagName('node')

	for friend in friends:
		data = getFriend(friend)
		friendList[friend.getAttribute('id')] = data


	return friendList

def getMLN(list):
	mlnY = 0
	mlnX = 0
	for line in list:
		if line[1] == 'Michael Nelson':
			mlnY = line[0]
			mlnX = line[2]

	nelYS = 'nelsonX <- c(' + str(mlnX) + ')\n'
	nelXS = 'nelsonY <- c(' + str(mlnY) + ')\n'
	return  nelXS, nelYS


if __name__=='__main__':
	fileName = 'mln.graphml'



	data = getAttributes(fileName)
	makeGraph(data)
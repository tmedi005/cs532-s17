import statistics
import re

if __name__ == "__main__":
	with open('twitterFollowers.txt') as f:
		data = f.read()
	data = map(int, re.findall('\d+', data))

	print sorted(data)

	
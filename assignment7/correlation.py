from math import sqrt

def sim_pearson(prefs, p1, p2):
	si = {}
	for item in prefs[p1]:
	    if item in prefs[p2]: 
			si[item] = 1
	if len(si) == 0:
	    return 0
	n = len(si)
	sum1 = sum([prefs[p1][it] for it in si])
	sum2 = sum([prefs[p2][it] for it in si])
	sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
	sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
	pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
	num = pSum - sum1 * sum2 / n
	den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
	if den == 0:
	    return 0
	r = num / den
	return r

def topMatches(prefs,person,t=5,b=-5,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other) 
                  for other in prefs if other!=person]
  scores.sort()
  scores.reverse()
  return scores[0:t], scores[b:]


movies={}
for line in open('u.item'):
	(id,title)=line.split('|')[0:2]
	movies[id]=title

# Load data
prefs={}
for line in open('u.data'):
	(user,movieid,rating)=line.split('\t')[0:3]
	prefs.setdefault(user,{})
	prefs[user][movies[movieid]]=float(rating)

(mostMatching, leastMatching) = topMatches(prefs, '37')
print 'The top 5 substitutes:'
print str(mostMatching[0]) + '\n' + str(mostMatching[1]) + '\n' + str(mostMatching[2]) + '\n' + str(mostMatching[3]) + '\n' + str(mostMatching[4]) + '\n'

print 'The bottom 5 substitutes:'
print str(leastMatching[0]) + '\n' + str(leastMatching[1]) + '\n' + str(leastMatching[2]) + '\n' + str(leastMatching[3]) + '\n' + str(leastMatching[4]) + '\n'

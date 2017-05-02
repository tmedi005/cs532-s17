import math

def cosine(v1, v2):
  sumxx, sumyy, sumxy = 0 ,0 ,0 
  for i in range(len(v1)):
    x = v1[i]; y = v2[i]
    sumxx += float(x)*float(x)
    sumyy += float(y)*float(y)
    sumxy += float(x)*float(y)
  return 1-(sumxy/math.sqrt(sumxx*sumyy))

def getdistances(data,vec1):
  distancelist=[]
   
  for i in range(len(data)):
    vec2=data[i]
    try:
      distancelist.append((cosine(vec1,vec2),i))
    except:
      pass

  distancelist.sort()
  return distancelist

def knnestimate(data,vec1,k=5):
  
  dlist=getdistances(data,vec1)
  avg=0.0
  return dlist
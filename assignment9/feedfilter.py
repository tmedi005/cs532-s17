import feedparser
import re
import math
import docclass

savefile = open("data.txt", "a")

def read(feed,classifier):

  splitRegexp = re.compile( r"<[^>]+>" )

  num=0
  f=feedparser.parse(feed)

  string1 = '50 manual classifications\n\n'
  dividline = "_" * 100 + "\n"
  print string1
  savefile.write(string1)
  string2 = "{:<60}{:<12}{:<10}{:<8}{:<10}{}".format("Title", "Prediction", "Actual", 'cprob', 'fisherprob',"\n")
  print string2
  savefile.write(string2)
  savefile.write(dividline)

  for entry in f['entries'][0:50]:
    num=num +1
    title=entry['title'].encode('utf-8').replace("'","")
    print 'Title:     '+ title
    
    summary = splitRegexp.sub( "", entry[ "summary" ] )
    
    print summary #entry['summary'].encode('utf-8')

    fulltext='%s\n%s' % (entry['title'],entry['summary'])
    fulltext=fulltext.replace("'","")
    predicted=str(classifier.classify(fulltext))
    print 'Predicted category: ', predicted

    actual=raw_input('Actual category: ')
    classifier.train(fulltext, actual)

    feature=raw_input('Enter string classifier: ')

    cp=round(classifier.cprob(feature,actual),4)
    fcp=round(classifier.fisherprob(feature,actual),4)

    string3 = "{:<60}{:<12}{:<10}{}".format(title, predicted, actual, "\n")
    savefile.write(string3)
 
   
    classifier.manualClassdb(num, title, feature, predicted, actual, cp, fcp)
  savefile.write(dividline)
  num=50
  string4 = '\n\n50 automatic classifications\n\n'
  print string4
  savefile.write(string4)
  savefile.write(string2)
  savefile.write(dividline)
  for entry in f['entries'][50:100]:
    num=num+1
    title=entry['title'].encode('utf-8').replace("'","")
    print 'Title:     '+ title
    summary = splitRegexp.sub( "", entry[ "summary" ] )
    
    print summary #entry['summary'].encode('utf-8')

    fulltext='%s\n%s' % (entry['title'],entry['summary'])
    fulltext=fulltext.replace("'","")
    predicted=str(classifier.classify(fulltext))
    print 'Predicted: ', predicted

    actual=raw_input('Actual category: ')

    
    cp=round(classifier.cprob(feature,actual),4)
    fcp=round(classifier.fisherprob(feature,actual),4)

    string6 = "{:<60}{:<12}{:<10}{}".format(title, predicted, actual, "\n")
    savefile.write(string6)
    classifier.autoClassdb(num, title, feature, predicted, actual, cp, fcp)    
  savefile.write(dividline)

def entryfeatures(entry):
  splitter=re.compile('\\W*')
  f={}
  
  titlewords=[s.lower() for s in splitter.split(entry['title']) 
          if len(s)>2 and len(s)<20]
  for w in titlewords: f['Title:'+w]=1
  
  summarywords=[s.lower() for s in splitter.split(entry['summary']) 
          if len(s)>2 and len(s)<20]

  uc=0
  for i in range(len(summarywords)):
    w=summarywords[i]
    f[w]=1
    if w.isupper(): uc+=1
    
    if i<len(summarywords)-1:
      twowords=' '.join(summarywords[i:i+1])
      f[twowords]=1
    

  if float(uc)/len(summarywords)>0.3: f['UPPERCASE']=1
  
  return f


cl=docclass.fisherclassifier(docclass.getwords)
cl.setdb('database.db')
read('xmlfeed.xml',cl)
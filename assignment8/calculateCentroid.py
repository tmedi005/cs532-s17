import clusters


(blognames, words, data) = clusters.readfile('blogdata.txt')



#kclust=clusters.kcluster(data,k=5)
#kclust=clusters.kcluster(data,k=10)
kclust=clusters.kcluster(data,k=20)
print "\n\n"+str([blognames[r] for r in kclust[0]])
print "\n\n"+str([blognames[r] for r in kclust[1]])
print "\n\n"+str([blognames[r] for r in kclust[2]])
print "\n\n"+str([blognames[r] for r in kclust[3]])
print "\n\n"+str([blognames[r] for r in kclust[4]])

print "\n\n"+str([blognames[r] for r in kclust[5]])
print "\n\n"+str([blognames[r] for r in kclust[6]])
print "\n\n"+str([blognames[r] for r in kclust[7]])
print "\n\n"+str([blognames[r] for r in kclust[8]])
print "\n\n"+str([blognames[r] for r in kclust[9]])


print "\n\n"+str([blognames[r] for r in kclust[10]])
print "\n\n"+str([blognames[r] for r in kclust[11]])
print "\n\n"+str([blognames[r] for r in kclust[12]])
print "\n\n"+str([blognames[r] for r in kclust[13]])
print "\n\n"+str([blognames[r] for r in kclust[14]])
print "\n\n"+str([blognames[r] for r in kclust[15]])
print "\n\n"+str([blognames[r] for r in kclust[16]])
print "\n\n"+str([blognames[r] for r in kclust[17]])
print "\n\n"+str([blognames[r] for r in kclust[18]])
print "\n\n"+str([blognames[r] for r in kclust[19]])



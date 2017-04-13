import clusters

(blognames, words, data) = clusters.readfile('blogdata.txt')
cluster = clusters.hcluster(data)

clusters.printclust(cluster, labels=blognames)

clusters.drawdendrogram(cluster, blognames, jpeg='cluster.jpg')
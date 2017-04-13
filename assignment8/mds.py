import clusters

(blognames, words, data)=clusters.readfile('blogdata.txt')

sdata = clusters.scaledown(data)

clusters.draw2d(sdata, blognames, jpeg='MDS.jpg')
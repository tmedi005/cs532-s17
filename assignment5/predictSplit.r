library(igraph)
library(igraphdata)

data(karate)
k_network<-karate

edgeBetweenness <- edge.betweenness(k_network)
highestEB <- max(edgeBetweenness)
deleteEdge <- match(c(highestEB), edgeBetweenness)

plot.igraph(k_network, vertex.color="grey",vertex.shape="circle",
            edge.color="black",main="Zachary's Karate Club Network", 
            layout=layout.kamada.kawai)



library(igraph)
library(igraphdata)

data(karate)
k_network<-karate


while (clusters(k_network)$no < 2){
  
  edgeBetweenness <- edge.betweenness(k_network)
  sort <- order(-edgeBetweenness)
  highestEB <- sort[-1]
  deleteEdge <- get.edge(k_network, highestEB)
  k_network <- delete.edges(k_network,E(k_network,deleteEdge))
}


plot.igraph(k_network, vertex.color="purple",vertex.shape="circle",vertex.label.color="#ffffff",
            edge.color="black",main="Karate Club (2 group split)", 
            layout=layout.kamada.kawai)



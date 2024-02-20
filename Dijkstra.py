# Dijstra 
# Obtiene el camino mas corto entre un vertice dado y el resto de vertices de un grafo pontederado
# En un grafo ponderado las vertices tiene peso(valor)

#Problema
#Pedro debe llegar a tiempo a un punto G desde un punto P, asi que debe recorrer la ditancia minima,
#el detalle es que pedro se cansa a la mitad del camino, por lo tanto, se debe dar como resultado 
#un punto falso Z(o todas las posibles soluciones) tal que pedro se canse en el punto G.
# De lo contrario el resultado sera "*".

class Road:
    def __init__(self):
        self.graph=dict()
        self.min_road=dict()
        self.point_P=0
        self.point_G=0
        self.len_vertice=0
        self.len_road=0
    
    def insertVertice(self,vertice,dst,power):
        if vertice in self.graph.keys():
            self.graph[vertice][dst]=power
            return
        self.graph.update({vertice:{dst:power}})

    def inputGraph(self):
        text = input().split(" ")
        self.len_vertice=int(text[0])
        self.len_road=int(text[1])

        text = input().split(" ")
        self.point_P=int(text[0])
        self.len_G=int(text[1])

        for i in range(0,self.len_road):
            text = input().split(" ")
            self.insertVertice(text[0],text[1],int(text[2]))
            self.insertVertice(text[1],text[0],int(text[2]))


new = Road()
new.inputGraph()
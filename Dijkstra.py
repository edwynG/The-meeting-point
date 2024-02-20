# Dijstra 
# Obtiene el camino mas corto entre un vertice dado y el resto de vertices de un grafo pontederado
# En un grafo ponderado las vertices tiene peso(valor)

#Problema
#Pedro debe llegar a tiempo a un punto G desde un punto P, asi que debe recorrer la ditancia minima,
#el detalle es que pedro se cansa a la mitad del camino, por lo tanto, se debe dar como resultado 
#un punto falso Z(o todas las posibles soluciones) tal que pedro se canse en el punto G.
# De lo contrario el resultado sera "*".

# Estructura de datos
class Road:
    def __init__(self):
        #in private: _atribute
        self._graph=dict()
        self._point_P=0
        self._point_G=0
        self._len_vertice=0
        self._len_road=0

    def getGraph(self): return self._graph
    def getPoint_P(self): return self._point_P
    def getPoint_G(self): return self._point_G

    def _insertVertice(self,vertice,dst,power):
        if vertice in self._graph.keys():
            self._graph[vertice][dst]=power
            return
        self._graph.update({vertice:{dst:power}})

    def inputGraph(self):
        text = input().split(" ")
        self._len_vertice=int(text[0])
        self._len_road=int(text[1])

        text = input().split(" ")
        self._point_P=int(text[0])
        self._len_G=int(text[1])

        for i in range(0,self._len_road):
            text = input().split(" ")
            self._insertVertice(text[0],text[1],int(text[2]))
            self._insertVertice(text[1],text[0],int(text[2]))


    def Dijstra(self):
       return

 
# Main:
City = Road()
City.inputGraph()
print(City.getGraph())

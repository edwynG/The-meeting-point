# Dijstra 
# Obtiene el camino mas corto entre un vertice dado y el resto de vertices de un grafo pontederado
# En un grafo ponderado las vertices tiene peso(valor)

#Problema
#Pedro debe llegar a tiempo a un punto G desde un punto P, asi que debe recorrer la ditancia minima,
#el detalle es que pedro se cansa a la mitad del camino, por lo tanto, se debe dar como resultado 
#un punto falso Z(o todas las posibles soluciones) tal que pedro se canse en el punto G.
# De lo contrario el resultado sera "*".

# Estructura de datos
import sys
class Road:
    def __init__(self):
        #in private: _atribute
        self._graph=dict()
        self._point_P=0
        self._power_min=0
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
        self._point_P=text[0]
        self._point_G=text[1]

        for i in range(0,self._len_road):
            text = input().split(" ")
            self._insertVertice(text[0],text[1],int(text[2]))
            self._insertVertice(text[1],text[0],int(text[2]))


    def Dijstra(self,grafo,inicio,comming):
        items= list(grafo.keys())
        min_road=list()
        visited=list()
    
        for i in items:
            if i == str(inicio):
                min_road.append(0)
                visited.append(True)
            else:
                min_road.append(sys.maxsize)
                visited.append(False)

        here=str(inicio)
        ultimate=items.index(str(comming))

        while not visited[ultimate]:
            for key,value in (grafo.get(here)).items():
                if min_road[items.index(key)] > min_road[items.index(here)]+value:
                    min_road[items.index(key)]=min_road[items.index(here)]+value
            
            minimal=self.minimales(min_road,visited)
            here= items[min_road.index(minimal)]
            visited[items.index(here)]=True

        self._power_min=min_road[items.index(str(comming))]

    def minimales(self,arr,visited):
        minimal=sys.maxsize
        for i in range(0,len(visited)):
            if not visited[i]:
                if minimal >= arr[i]:
                    minimal=arr[i]

        return minimal
# Main:
City = Road()
City.inputGraph()
zone=City.getGraph()
init = City.getPoint_P()
comming= City.getPoint_G()
City.Dijstra(zone,init,comming)

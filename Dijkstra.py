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
        self._solution=list()
        self._point_P=0
        self._point_G=0
        self._crosses=list()
        self._len_vertice=0
    def getGraph(self): return self._graph
    def getPoint_P(self): return self._point_P
    def getPoint_G(self): return self._point_G
    def getSolution(self): return self._solution

    def printSolution(self): 
        if len(self._solution): 
            print(" ".join(self._solution))
            return
        print("*")

    def _insertVertice(self,vertice,dst,power):
        if vertice in self._graph.keys():
            if power != 0:
                self._graph[vertice][dst]=power
                return
            self._graph[vertice][dst]=sys.maxsize
            
            return
        self._graph.update({vertice:{dst:power}})

    def inputGraph(self):
        text = input().split(" ")
        self.len_vertice=int(text[0])
        len_road=int(text[1])

        text = input().split(" ")
        self._point_P=text[0]
        self._point_G=text[1]

        for i in range(0,len_road):
            text = input().split(" ")
            self._insertVertice(text[0],text[1],int(text[2]))
            self._insertVertice(text[1],text[0],int(text[2]))

        self._crosses=list(self._graph.keys())

    def Dijstra(self,grafo,init,comming):
        items= list(grafo.keys())
        min_road=list()
        visited=list()
        for i in items:
            if i == str(init):
                min_road.append(0)
                visited.append(True)
            else:
                min_road.append(sys.maxsize)
                visited.append(False)

        here=str(init)
        ultimate=items.index(str(comming))
        while not visited[ultimate]:
            for key,value in (grafo.get(here)).items():
                if min_road[items.index(key)] > min_road[items.index(here)]+value:
                    min_road[items.index(key)]=min_road[items.index(here)]+value
            
            
            minimal=self.minimales(min_road,visited)
            here= items[minimal]
            visited[items.index(here)]=True
            
        
        return min_road[items.index(str(comming))]

    def minimales(self,arr,visited):
        minimal=sys.maxsize
        indice=-1
        for i in range(0,len(visited)):
            if not visited[i]:
                if minimal >= arr[i]:
                    minimal=arr[i]
                    indice=i
        return indice
    
    def falsePoint(self,source,valor,dist,road=""):
        if valor == dist*2: 
            if source not in self._solution:
                self._solution.append(source)
        for key,value in (self._graph.get(source)).items():
            if road.find(key) == -1 and self._point_G != key and self._point_P != key : 
                self.falsePoint(key,valor+value,dist,road+key)

    def TheMeentingPoint(self,init):
        road_min =self.Dijstra(self._graph,init,self._point_G)
        self.falsePoint(self._point_G,road_min,road_min)
        arr= list()
        for key in self._solution:
            arr.append(key)
      
        for key in arr:
            minimo= self.Dijstra(self._graph,self._point_P,key)
            if (minimo/2) != road_min:
                self._solution.remove(key)
            
        self.printSolution()
    

City = Road()
City.inputGraph()
City.TheMeentingPoint(City.getPoint_P())



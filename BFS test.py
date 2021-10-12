from collections import defaultdict
class Tile:
    def __init__(self, column, row, isGoal):
        self.column = column
        self.row = row
        self.isGoal = isGoal
    def getXY(self):
        return self.column, self.row
    def getDistanceToGoal(self, goalNode):
        if(self.isGoal):
            return 0
        
class bfsGraph:
    # Constructor
    def __init__(self):
        # empty dictionary to store graph
        self.bfsGraph = {}
    # function to add an edge to graph
    def addTile(self,u,*edges): # You can create a tile here, or add new edges to it. The number of new edges can be 0 or more. (O typically means you are adding a tile with no connections)
        if(u not in self.bfsGraph):
            self.bfsGraph[u] = [u]
        for tile in edges:
            if [tile] not in self.bfsGraph[u]:
                self.bfsGraph[u] = self.bfsGraph[u] + [tile]


        #self.bfsGraph[u].append(v)
    # Function to BFS through our maze->graph and find the Tile marked as "Goal"
    def BFS(self, s): #S is the goal state. Goal is the tile
        # Mark all the vertices as not visited
        visited = {}
        for node in self.bfsGraph:
            visited[node] = False
        # Create a queue for BFS
        queue = []
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s.getXY())
            #print (s, end = " ")
            if (s.isGoal):
                print("Reached goal 2222!")
                print(s.getXY())
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.bfsGraph[s]:
                if( i.isGoal):
                    print("reached goal state!")
                    print (i.getXY())
                    break
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True        

""" ddict = {}
node1 = Tile(0,1, False)
node2 = Tile(1,1, False)
node3 = Tile(0,3, False)
node4 = Tile(0,4,True)
ddict[node1] = [node1]
ddict[node1] = ddict[node1] + [node2]
ddict[node2] = [node2]
ddict[node3] = [node3]
ddict[node4] = [node4]
ddict[node3] = ddict[node3] + [node4]
for nodes in ddict:
    for node in ddict[nodes]:
        if(node.isGoal):
            print("Goal reached: " , node.getXY())
            break
        else:
            print (node.getXY()) """


tile1 = Tile(0,1, False)
tile2 = Tile(1,1, False)
tile3 = Tile(0,3, False)
tile4 = Tile(0,4,True)
bfs1 = bfsGraph()
bfs1.addTile(tile1, tile2,tile3)
bfs1.addTile(tile2, tile3)
bfs1.addTile(tile3,tile4)
bfs1.addTile(tile4)
#print(bfs1.bfsGraph[tile2])
bfs1.BFS(tile1)

""" g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(0,3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
#g.BFS(2,1) """





class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    # Function to print a BFS of graph
    def BFS(self, s, goal):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        # Create a queue for BFS
        queue = []
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if(visited[i] == goal):
                    print("reached goal state!")
                    print (visited)
                    break
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
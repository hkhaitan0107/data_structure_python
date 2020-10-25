# Graph Eulerian path & circuit

class Node(object):
    def __init__(self, val):
        self.value = val
        self.edges = []
        self.visited = False
        self.incoming_edge = 0
        self.outgoing_edge = 0
        
class Edge(object):
    def __init__(self, val, from_node, to_node):
        self.value = val
        self.from_node = from_node
        self.to_node = to_node
        
class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = []
        
    def insert_node(self, node_val):
        new_node = Node(node_val)
        self.nodes.append(new_node)
        return new_node
        
    def insert_edge(self, edge_val, node_from_val, node_to_val):
        from_node_finder = None
        to_node_finder = None
        for n in self.nodes:
            if from_node_finder and to_node_finder:
                break
            else:
                if node_from_val == n.value:
                    from_node_finder = n
                elif node_to_val == n.value:
                    to_node_finder = n
                
        if from_node_finder == None:
            from_node_finder = self.insert_node(node_from_val)
        if to_node_finder == None:
            to_node_finder = self.insert_node(node_to_val)
            
        new_edge = Edge(edge_val, from_node_finder, to_node_finder)
        from_node_finder.edges.append(new_edge)
        from_node_finder.outgoing_edge += 1
        to_node_finder.edges.append(new_edge)
        to_node_finder.incoming_edge += 1
        self.edges.append(new_edge)
        
    def find_node(self, find_node_val):
        for n in self.nodes:
            if n.value == find_node_val:
                return n
          
        return None
    
    def _clear_visited(self):
        for _node in self.nodes:
            _node.visited = False
            
    def bfs_graph_traversal(self, starting_node_val):
        starting_node = self.find_node(starting_node_val)
        
        if starting_node == None:
            print("Invalid Input")
            return
        visit_queue = [starting_node]
        self._clear_visited()
        while len(visit_queue) > 0:
            current_node = visit_queue.pop()
            if current_node.visited == False:
                current_node.visited = True
                print(current_node.value)
            
            for e in current_node.edges:
                if e.from_node.value == current_node.value and e.to_node.visited == False:
                    visit_queue.insert(0, e.to_node)
                    #print("Inserting Node: {}".format(e.to_node.value))
                    
    def eulerian_circuit(self):
        for n in self.nodes:
            if n.incoming_edge != n.outgoing_edge:
                return False
        return True
        
    def eulerian_path(self):
        pos_1 = 0
        neg_1 = 0
        for n in self.nodes:
            if pos_1 > 1 or neg_1 > 1:
                return False
            if n.incoming_edge != n.outgoing_edge:
                if abs(n.incoming_edge - n.outgoing_edge) > 1:
                    return False
                elif n.incoming_edge - n.outgoing_edge == 1:
                    pos_1 += 1
                else:
                    neg_1 += 1
        return True
    
graph = Graph()                    
graph.insert_edge(51, 0, 1)     # MV <-> SF
graph.insert_edge(51, 1, 0)     # SF <-> MV
graph.insert_edge(9950, 0, 3)   # MV <-> Shanghai
graph.insert_edge(9950, 3, 0)   # Shanghai <-> MV
graph.insert_edge(10375, 0, 5)  # MV <-> Sao Paolo
graph.insert_edge(10375, 5, 0)  # Sao Paolo <-> MV
graph.insert_edge(9900, 1, 3)   # SF <-> Shanghai
graph.insert_edge(9900, 3, 1)   # Shanghai <-> SF
graph.insert_edge(9130, 1, 4)   # SF <-> Berlin
graph.insert_edge(9130, 4, 1)   # Berlin <-> SF
graph.insert_edge(9217, 2, 3)   # London <-> Shanghai
graph.insert_edge(9217, 3, 2)   # Shanghai <-> London
graph.insert_edge(932, 2, 4)    # London <-> Berlin
graph.insert_edge(932, 4, 2)    # Berlin <-> London
graph.insert_edge(9471, 2, 5)   # London <-> Sao Paolo
graph.insert_edge(9471, 5, 2) 

print(graph.eulerian_path())
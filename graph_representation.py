# Graph
class node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        
class edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
        
    def insert_node(self, node_value):
        new_node = node(node_value)
        self.nodes.append(new_node)
        
    def insert_edge(self, value, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for _node in self.nodes:
            if node_from_val == _node.value:
                print("node found = {}".format(_node.value))
                from_found = _node
            if node_to_val == _node.value:
                print("node found = {}".format(_node.value))
                to_found = _node
                
        if from_found == None:
                from_found = node(node_from_val)
                self.nodes.append(from_found)
                print("Added new node = {}".format(node_from_val))
        if to_found == None:
                to_found = node(node_to_val)
                self.nodes.append(to_found)
                print("Added new node = {}".format(node_to_val))
                
        new_edge = edge(value, from_found, to_found)
        print("Added edge from {} to {}".format(node_from_val, node_to_val))
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)
            
    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        edge_list = []
        for edge in self.edges:
            new_edge = (edge.value, edge.node_from.value, edge.node_to.value)
            edge_list.append(new_edge)
        return edge_list
       
    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        max_index = self.get_max_index()
        adjacency_list = [None] * (max_index + 1)
        for _edge in self.edges:
            if adjacency_list[_edge.node_from.value] == None:
                adjacency_list[_edge.node_from.value] = [(_edge.node_to.value, _edge.value)]
            else:
                adjacency_list[_edge.node_from.value].append((_edge.node_to.value, _edge.value))
        
        return adjacency_list 
        
    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        max_index = self.get_max_index()
        adjacency_list = [[0 for i in range(max_index + 1)] for j in range(max_index + 1)]
        for _edge in self.edges:
            adjacency_list[_edge.node_from.value][_edge.node_to.value] = _edge.value
        return adjacency_list
    
    def get_max_index(self):
        max_index = -1
        if len(self.nodes) > 0:
            for _node in self.nodes:
                if _node.value > max_index:
                    max_index = _node.value
        return max_index
    
graph1 = graph()
graph1.insert_edge(100, 1, 2)
graph1.insert_edge(101, 1, 3)
graph1.insert_edge(102, 1, 4)
graph1.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
#print(graph1.get_edge_list())
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
#print(graph1.get_adjacency_list())
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print(graph1.get_adjacency_matrix())
                
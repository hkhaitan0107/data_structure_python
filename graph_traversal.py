class Queue(object):
    def __init__(self, val):
        self.que = [val]
        
    def enqueue(self, val):
        if len(self.que) > 0:
            self.que.insert(0, val)
        else:
            self.que = [val]
            
    def dequeue(self):
        if len(self.que) > 0:
            return self.que.pop()
        else:
            return None
    
    def peek(self):
        if len(self.que) > 0:
            return self.que[-1]
        else:
            return None

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False
        
class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes = None, edges = None):
        self.nodes = nodes or []
        self.edges = edges or []
        self._node_map = {}
        self.node_names = []
    
    def set_node_names(self, node_names):
        self.node_names = list(node_names)
        
    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        node_dict = {node_from_val:None, node_to_val: None}
        for _node in self.nodes:
            if _node.value in node_dict:
                node_dict[_node.value] = _node
                if all(node_dict.values()):
                    break
                
        for node_val in node_dict:
            node_dict[node_val] = node_dict[node_val] or self.insert_node(node_val)
            
        new_edge = Edge(new_edge_val, node_dict[node_from_val], node_dict[node_to_val])
        node_dict[node_from_val].edges.append(new_edge)
        node_dict[node_to_val].edges.append(new_edge)
        self.edges.append(new_edge)
        
    def get_edge_list(self):
        return [(e.value, e.node_from, e.node_to) for e in self.edges]
    
    def get_edge_list_names(self):
        return [(e.value, 
                self.node_names[e.node_from.value], 
                self.node_names[e.node_to.value]) 
                for e in self.edges]
        
    def adjacency_list(self):
        max_val = self.get_max_limit()
        adjacency_list = [[None] * (max_val + 1)]
        for e in self.edges:
            if adjacency_list[e.node_from.value] == None:
                adjacency_list[e.node_from.value] = [e.node_to.value]
            else:
                adjacency_list[e.node_from.value].append(e.node_to.value)
                
        return adjacency_list
    
    def get_adjacency_list_names(self):
        max_val = self.get_max_limit()
        adjacency_list_names = [[] for _ in range(max_val)]
        for e in self.edges:
            if adjacency_list_names[e.node_from.value] == None:
                adjacency_list_names[e.node_from.value] = [self.node_names[e.node_to.value]]
            else:
                adjacency_list_names[e.node_from.value].append(self.node_names[e.node_to.value])
                
        return adjacency_list_names
        
    def get_adjacency_matrix(self):
        max_val = self.get_max_limit()
        adjacency_matrix = [[0] * (max_val + 1) for _ in range(max_val)]
        for e in self.edges:
            adjacency_matrix[e.node_from.value][e.node_to.value] = e.value
        return adjacency_matrix
        
    def find_node(self, node_number):
        "Return the node with value node_number or None"
        return self._node_map.get(node_number)
    
    def get_max_limit(self):
        max_val = -1
        if len(self.node_names) > 0:
            return len(self.node_names)
        if len(self.nodes) > 0:
            for _node in self.nodes:
                if _node.value > max_val:
                    max_val = _node.value
        return max_val
        
    def _clear_visited(self):
        for _node in self.nodes:
            _node.visited = False

    def dfs_helper(self, start_node):
        """TODO: Write the helper function for a recursive implementation
        of Depth First Search iterating through a node's edges. The
        output should be a list of numbers corresponding to the
        values of the traversed nodes.
        ARGUMENTS: start_node is the starting Node
        MODIFIES: the value of the visited property of nodes in self.nodes 
        RETURN: a list of the traversed node values (integers).
        """
        if start_node.visited == True:
            return []
        ret_list = [start_node.value]
        start_node.visited = True

        for e in start_node.edges:
            if e.node_from.value == start_node.value:
                k = self.dfs_helper(e.node_to)
                if k != []:
                    ret_list += k
        return ret_list

    def dfs(self, start_node_num):
        """Outputs a list of numbers corresponding to the traversed nodes
        in a Depth First Search.
        ARGUMENTS: start_node_num is the starting node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        self._clear_visited()
        start_node = self.find_node(start_node_num)
        return self.dfs_helper(start_node)

    def dfs_names(self, start_node_num):
        """Return the results of dfs with numbers converted to names."""
        return [self.node_names[num] for num in self.dfs(start_node_num)]

    def bfs(self, start_node_num):
        """TODO: Create an iterative implementation of Breadth First Search
        iterating through a node's edges. The output should be a list of
        numbers corresponding to the traversed nodes.
        ARGUMENTS: start_node_num is the node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        node = self.find_node(start_node_num)
        self._clear_visited()
        ret_list = []
        track_queue = Queue(node)
        while track_queue.peek().visited == False:
            current_node = track_queue.dequeue()
            if ret_list == []:
                ret_list = [current_node.value]
            else:
                ret_list.append(current_node.value)
            
            current_node.visited = True
            for e in current_node.edges:
                if e.node_from.value == current_node.value and e.node_to.visited == False:
                    track_queue.enqueue(e.node_to)
        
        return ret_list

    def bfs_names(self, start_node_num):
        """Return the results of bfs with numbers converted to names."""
        return [self.node_names[num] for num in self.bfs(start_node_num)]
        
graph = Graph()

# You do not need to change anything below this line.
# You only need to implement Graph.dfs_helper and Graph.bfs

graph.set_node_names(('Mountain View',   # 0
                      'San Francisco',   # 1
                      'London',          # 2
                      'Shanghai',        # 3
                      'Berlin',          # 4
                      'Sao Paolo',       # 5
                      'Bangalore'))      # 6 

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
graph.insert_edge(9471, 5, 2)   # Sao Paolo <-> London
# (6) 'Bangalore' is intentionally disconnected (no edges)
# for this problem and should produce None in the
# Adjacency List, etc.

import pprint
pp = pprint.PrettyPrinter(indent=2)

print("Edge List")
pp.pprint(graph.get_edge_list_names())

print("\nAdjacency List")
pp.pprint(graph.get_adjacency_list_names())

print("\nAdjacency Matrix")
pp.pprint(graph.get_adjacency_matrix())

# nn = graph.find_node(1)
# for i in nn.edges:
#     if i.node_from.value == 1:
#         print(i.node_to.value)

print("\nDepth First Search")
pp.pprint(graph.dfs_names(2))

# Should print:
# Depth First Search
# ['London', 'Shanghai', 'Mountain View', 'San Francisco', 'Berlin', 'Sao Paolo']

print("\nBreadth First Search")
pp.pprint(graph.bfs_names(2))
# test error reporting
# pp.pprint(['Sao Paolo', 'Mountain View', 'San Francisco', 'London', 'Shanghai', 'Berlin'])

# Should print:
# Breadth First Search
# ['London', 'Shanghai', 'Berlin', 'Sao Paolo', 'Mountain View', 'San Francisco']
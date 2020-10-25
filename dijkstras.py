# Graph Eulerian path & circuit
class HeapNode(object):
    def __init__(self, distance, node):
        self.node = node
        self.distance = distance
        
class MinHeap(object):
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
        
    def upward_adjustment(self):
        i = self.current_size
        parent = i // 2
        while i // 2 > 0:
            if self.heap_list[parent].distance > self.heap_list[i].distance:
                self.heap_list[parent], self.heap_list[i] = self.heap_list[parent], self.heap_list[i]
            else:
                break
    
    def heap_insertion(self, value):
        # Append the value to the last of the list
        self.heap_list.append(value)
        self.current_size += 1
        # Upwards re-adjust to maintain heap
        self.upward_adjustment()
    
    def get_min_child(self, parent_index):
        if (2*parent_index) + 1 > self.current_size:
            return 2*parent_index
        else:
            if self.heap_list[2*parent_index].distance < self.heap_list[(2*parent_index)+1].distance:
                return 2*parent_index
            else:
                return (2*parent_index) + 1
        
        
    def downwards_readjustment(self, parent_index):
        while 2 * parent_index <= self.current_size: 
            # Get min child index
            min_child = self.get_min_child(parent_index)
            
            #Replace parent with the min child
            if self.heap_list[parent_index].distance > self.heap_list[min_child].distance:
                self.heap_list[parent_index], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[parent_index]
            else:
                break
            parent_index = min_child
            
    def heap_deletion(self):
        # Remove the top most element from the heap
        
        min_el = self.heap_list[1]
        self.current_size -= 1
        
        # Shift last element to the top 
        self.heap_list[1] = self.heap_list.pop()
        
        # Downwards re-adjustment
        self.downwards_readjustment(1)
        
        return min_el
        
        
class Node(object):
    def __init__(self, val):
        self.value = val
        self.edges = []
        self.relaxation = False
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
    
    def find_node(self, node_val):
        for n in self.nodes:
            if n.value == node_val:
                return n
        return None
    
    def get_node_table(self, start_node):
        visit_map = {start_node: None}
        dist_map = {start_node.value: 0}
        for n in self.nodes:
            if n.value != start_node.value:
                visit_map[n] = None
                dist_map[n.value] = float('inf')
                
        return visit_map, dist_map
        
    def shortest_spanning_path(self, start_node_val):
        start_node = self.find_node(start_node_val)
        visit_map, distance_map = self.get_node_table(start_node)
        
        current = start_node
        while not all(visit_map.values()):
            min_heap =  MinHeap()
            visit_map[current] = "Visited"
            for e in current.edges:
                if e.from_node.value == current.value and visit_map[e.to_node] == None:
                    dist_val = e.to_node.value + distance_map[e.from_node.value]
                    
                    if dist_val < distance_map[e.to_node.value]:
                        distance_map[e.to_node.value] = dist_val
                        e.to_node.relaxation = True
                    else:
                        dist_val = distance_map[e.to_node.value]
                        
                    heap_el = HeapNode(dist_val, e.to_node)
                    min_heap.heap_insertion(heap_el)
                    
            current = min_heap.heap_deletion().node
        return distance_map
                
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

print(graph.shortest_spanning_path(0))
# print(graph.eulerian_path())
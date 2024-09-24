from queue import deque
from queue import Queue

graph = {
    '1': ['2', '9', '10'],
    '2': ['3', '4'],
    '3': [],
    '4': ['5', '6', '7'],
    '5': ['8'],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
    '10': [],
}


print("-- Breadth First Search --")
def BFS(graph, start):  ### First In First Out
    visited = []  # List to keep track of visited nodes.
    queue = deque([start])  # Initialize a queue

    while queue:
        node = queue.popleft() 
        visited.append(node)
        childs = graph[node]

        for child in childs:
            if child not in visited and child not in queue:
                queue.append(child)
    return visited

print(BFS(graph, '1'))


print("-- Depth First Search without Recursion --") 
def DFS(graph, start):  ### Last In First Out  
    stack = []
    visited = []
    stack.append(start)
    while stack:
        node = stack.pop()
        visited.append(node)
        childs = graph[node]
       
        for child in reversed(childs):
            if child not in visited:
                stack.append(child)
    return visited 


print(DFS(graph, '1'))

visited = []
print("-- Depth First Search with Recursion --") 
def DFS_Recursion(graph, start):
    visited.append(start)
    childs = graph[start]
    for child in childs:
        DFS_Recursion(graph, child)
            
    return visited
print(DFS_Recursion(graph, '1'))


# Uniform cost, Priority Queue - variant of queue, lowest first
from queue import PriorityQueue

graph = {
        "1": {"2": 3, "3": 4, "5": 2},
        "2": {"1": 3, "4": 1, "5": 2},
        "3": {"1": 4, "5": 2, "6": 3},
        "4": {"2": 1, "8": 4},
        "5": {"2": 2, "3": 2, "7": 5},
        "6": {"3": 3, "9": 5},
        "7": {"5": 5, "8": 2, "10": 2},
        "8": {"4": 4, "7": 2, "10": 4},
        "9": {"6": 5, "10": 3},
        "10": {"7": 2, "8": 4, "9": 3}
    }

def uniform_cost_search_pq(graph, start, goal):
    # Priority Queue where the priority is the cost
    pq = PriorityQueue()
    pq.put((0, start, []))  # (cost, current_node, path)
    visited = set()
    while not pq.empty():
        cost, node, path = pq.get()
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == goal:
                return path
            for child, child_cost in graph[node].items():
                if child not in visited:
                    pq.put((child_cost + cost, child, path))


# Example usage with the graph defined earlier




####  Deepening Depth-First Search (IDDFS)

def deepening_dfs_iterative(graph, start, goal):
    depth = 0


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Find a path from A to G using IDDFS (Iterative)
start_node = 'A'
goal_node = 'G'
path = deepening_dfs_iterative(graph, start_node, goal_node)
print(f"Nodes visited from {start_node} to {goal_node} using IDDFS: {path}")
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # on node, conduct BFS, add each neighbour on queue
        # saving a snapshot neighbor after each neighbour is added
        # create a node
        # if no neighbour/ neighbor seen, graph complete?

        ## 

        # queue: {}
        # seen: {1, 2}

        # empty case
        if node == None: return None

        newG = {}
        queue = collections.deque([node])
        newG[node] = Node(1)
        
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in newG:
                    newG[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                newG[curr].neighbors.append(newG[neighbor])

        return newG[node]



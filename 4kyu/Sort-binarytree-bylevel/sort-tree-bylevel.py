# implemented with breadth-first traversal
from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
        
def tree_by_levels(node):
    
    dqueque = deque()
    res = []
    
    if not node:
        return res
    else:
        dqueque.append(node)

    def append_children(node):
            if node.left :
                dqueque.append(node.left)
            if node.right :
                dqueque.append(node.right)
              
    while dqueque:
        append_children(dqueque[0])
        res.append(dqueque[0].value)
        dqueque.popleft()
    return res

print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))
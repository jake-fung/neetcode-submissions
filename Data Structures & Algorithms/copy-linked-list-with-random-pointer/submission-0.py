"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1st pass: create each deep copy node, no next or random yet, hash map old to new
        oldToNew = {None: None}

        curr = head
        while curr:
            node = Node(curr.val)
            oldToNew[curr] = node
            curr = curr.next
        # 2nd pass: using hashmap, we can point next or random from old to new and map it to the new node
        curr = head
        while curr:
            node = oldToNew[curr]
            node.next = oldToNew[curr.next]
            node.random = oldToNew[curr.random]
            curr = curr.next
        return oldToNew[head]
            
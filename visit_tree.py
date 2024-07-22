from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# m -> l -> r
def preorder(root: Optional[TreeNode]) -> List[TreeNode]:
    if not root:
        return []
    
    stk, order = [root], []
    while stk:
        node = stk.pop()
        order.append(node)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)

    return order

# l -> m -> r
def inorder(root: Optional[TreeNode]) -> List[TreeNode]:
    stk, order = [], []
    cur = root
    while cur or stk:
        while cur:
            stk.append(cur)
            cur = cur.left
        cur = stk.pop()
        order.append(cur)
        cur = cur.right
    
    return order

# l -> r -> m
def postorder(root: Optional[TreeNode]) -> List[TreeNode]:
    if not root:
        return []

    stk, order = [root], []
    while stk:
        cur = stk.pop()
        order.append(cur)
        if cur.left:
            stk.append(cur.left)
        if cur.right:
            stk.append(cur.right)
        
    return order[::-1]

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3

    def printer(order):
        print([n.val for n in order])

    printer(preorder(node1))
    printer(inorder(node1))
    printer(postorder(node1))
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_binary_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) for val in values]
    root = nodes[0]
    queue = deque([root])
    idx = 1
    while queue and idx < len(nodes):
        node = queue.popleft()
        # print(node.val)
        if idx < len(nodes):
            node.left = nodes[idx]
            queue.append(node.left)
            idx += 1
        if idx < len(nodes):
            node.right = nodes[idx]
            queue.append(node.right)
            idx += 1
    return root

def print_inorder(node):
    if not node:
        return
    print_inorder(node.left)
    print(node.val, end=' ')
    print_inorder(node.right)

def preorderTraversal(node):
    res = []
    def preorder(root):
        if not root:
            return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)
    preorder(node)
    return res

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        print("maxDepth(None) -> 0")
        return 0
    print(f"maxDepth(TreeNode({root.val})) called")
    if root.left:
        print(f"  Calling left child: TreeNode({root.left.val})")
    else:
        print(f"  Calling left child: None")
    left_depth = maxDepth(root.left)        
    if root.right:
        print(f"  Calling right child: TreeNode({root.right.val})")
    else:
        print(f"  Calling right child: None")
    right_depth = maxDepth(root.right)
    result = 1 + max(left_depth, right_depth)
    print(f"maxDepth(TreeNode({root.val})) returns {result} (left: {left_depth}, right: {right_depth})")
    return result

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    res = 0
    def dfs(node):
        nonlocal res

        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        res = max(res, left + right)
        
        return 1 + max(left, right)
    dfs(root)
    return res
            

# Example usage:
root = build_binary_tree([1,2,3,None,None,4])
# print("In-order traversal of the tree:")
# print_inorder(root)
# print("Pre-order traversal of the tree:")
# print(" ".join(map(str, preorderTraversal(root))))
print(maxDepth(root))

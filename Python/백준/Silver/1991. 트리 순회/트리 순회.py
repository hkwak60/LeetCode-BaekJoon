class Node():
    def __init__(self, value,):
        self.data = value
        self.left = None
        self.right = None

def insert(node, parent, leftchild,rightchild):
    if node is None:
        return
    if node.data==parent.data:
        if leftchild!='.':
            node.left = Node(leftchild)
        if rightchild!='.':
            node.right = Node(rightchild)
    insert(node.left, parent, leftchild, rightchild)
    insert(node.right, parent, leftchild, rightchild)


# Pre-order DFS: Root, Left, Right 전위순회
def pre_order_dfs(node):
    if node is None:
        return
    print(node.data, end='')
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)

# In-order DFS: Left, Root, Right 중위순회
def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.data, end='')
    in_order_dfs(node.right)

# Post-order DFS: Left, Right, Root 후위순회
def post_order_dfs(node):
    if node is None:
        return
    post_order_dfs(node.left)
    post_order_dfs(node.right)
    print(node.data, end='')

import sys

N = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip().split()
root = Node(line[0])
insert(root,Node(line[0]),line[1],line[2])

for i in range(N-1):
    line = sys.stdin.readline().strip().split()
    insert(root, Node(line[0]), line[1],line[2])

pre_order_dfs(root)
print()
in_order_dfs(root)
print()
post_order_dfs(root)
print()
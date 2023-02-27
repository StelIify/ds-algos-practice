class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

    def __repr__(self):
        return str(self.value)


def search(search_value, node):
    if node is None or node.value == search_value:
        return node

    elif node.value < search_value:
        return search(search_value, node.right_child)

    else:
        return search(search_value, node.left_child)


node1 = TreeNode(25)
node2 = TreeNode(75)

node1_1 = TreeNode(10)
node1_2 = TreeNode(33)

node2_1 = TreeNode(56)
node2_2 = TreeNode(89)

root = TreeNode(50, node1, node2)
node1.left_child = node1_1
node1.right_child = node1_2

node2.left_child = node2_1
node2.right_child = node2_2

print(search(56, root))

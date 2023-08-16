from data_structures.queue import Queue


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

    def __repr__(self):
        return str(self.value)


def dfs_search(search_value, node):
    if node is None or node.value == search_value:
        return node

    elif node.value < search_value:
        return dfs_search(search_value, node.right_child)

    else:
        return dfs_search(search_value, node.left_child)


def insert(value, node):
    if node.value < value:
        if node.right_child is None:
            node.right_child = TreeNode(value)
        else:
            insert(value, node.right_child)

    elif node.value >= value:
        if node.left_child is None:
            node.left_child = TreeNode(value)
        else:
            insert(value, node.left_child)


def traverse(node, depth=0):
    if node is None:
        return depth
    traverse(node.left_child, depth + 1)
    print(node)
    traverse(node.right_child, depth + 1)


def max_depth(node):
    if node is None:
        return 0
    max_left = max_depth(node.left_child)
    max_right = max_depth(node.right_child)
    return 1 + max(max_left, max_right)


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

insert(45, root)
insert(41, root)
insert(31, root)


# traverse(root)
# print(max_depth(root))


def bfs(head: TreeNode, number) -> bool:
    q = Queue(head)

    while len(q):
        current = q.dequeue()
        print(current)
        if current.value == number:
            return True
        if current.left_child:
            q.enqueue(current.left_child)
        if current.right_child:
            q.enqueue(current.right_child)
    return False


# print(bfs(root, 41))

c_node_2 = TreeNode(10)
c_node_3 = TreeNode(30)

root1 = TreeNode(20, c_node_2, c_node_3)
root2 = TreeNode(20, c_node_3, c_node_2)


def compare_binary_trees(head_one, head_two) -> bool:
    if not head_one and not head_two:
        return True
    if not head_one or not head_two:
        return False
    if head_one.value != head_two.value:
        return False

    return compare_binary_trees(head_one.left_child, head_two.left_child) and \
        compare_binary_trees(head_one.right_child, head_two.right_child)


print(compare_binary_trees(root1, root2))

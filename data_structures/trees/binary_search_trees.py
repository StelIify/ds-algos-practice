from data_structures.queue import Queue
from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

    def __repr__(self):
        return str(self.value)


def dfs(node: TreeNode, search_value):
    if node is None:
        return False
    if node.value == search_value:
        return True
    elif search_value > node.value:
        return dfs(node.right_child, search_value)
    else:
        return dfs(node.left_child, search_value)


def bfs(head: TreeNode, number) -> bool:
    q = Queue(head)

    while len(q):
        current = q.dequeue()
        if current.value == number:
            return True
        if current.left_child:
            q.enqueue(current.left_child)
        if current.right_child:
            q.enqueue(current.right_child)
    return False


def insert(value, node):
    if value > node.value:
        if not node.right_child:
            node.right_child = TreeNode(value)
            return
        else:
            insert(value, node.right_child)

    elif value <= node.value:
        if not node.left_child:
            node.left_child = TreeNode(value)
            return
        else:
            insert(value, node.left_child)


def delete(node, delete_value):
    if not node:
        return None
    if delete_value > node.value:
        node.right_child = delete(node.right_child, delete_value)
        return node
    elif delete_value < node.value:
        node.left_child = delete(node.left_child, delete_value)
        return node
    else:
        if not node.left_child:
            return node.right_child
        elif not node.right_child:
            return node.left_child
        else:
            # it has two children
            node.right_child = successor(node.right_child, node)
            return node


def successor(node, node_to_delete):
    if node.left_child:
        node.left_child = successor(node.left_child, node_to_delete)
        return node
    else:
        node_to_delete.value = node.value
        return node.right_child


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
    max_node = max(max_left, max_right)
    return 1 + max_node


def find_minimum_value(node):
    if not node.left_child:
        return node
    return find_minimum_value(node.left_child)


def find_kth_max_value(root, k):
    res = []

    def traverse_in_order(node):
        if not node:
            return
        traverse_in_order(node.right_child)
        if len(res) == k:
            return
        res.append(node.value)
        traverse_in_order(node.left_child)

    traverse_in_order(root)
    return res[-1]


def find_ancestors(root: TreeNode, value: int):
    res = []

    def pre_order_traverse(node: TreeNode, value):
        if not node:
            return False
        if node.value == value:
            return True
        if value < node.value:
            left = pre_order_traverse(node.left_child, value)
            if left:
                res.append(node.value)
                return True
        elif value > node.value:
            right = pre_order_traverse(node.right_child, value)
            if right:
                res.append(node.value)
                return True
        return False

    pre_order_traverse(root, value)
    return res


def find_nodes_at_k_distance_from_root(root, k):
    queue = deque()
    queue.append(root)
    c = 0

    while queue:
        current = queue.popleft()
        queue.append(current.left_child)
        queue.append(current.right_child)
        if c == k:
            return list(queue)
        c += 1


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
node1_1.left_child = TreeNode(6)
node2_1.right_child = TreeNode(60)

insert(6, root)
insert(4, root)

# print(find_minimum_value(root))  # 4
# print(find_kth_max_value(root, 3))
# print(find_ancestors(root, 60))
# print(max_depth(root))
print(find_nodes_at_k_distance_from_root(root, 2))


# delete(root, 50)
# insert(31, root)

# print(dfs(root, 56))
# print(bfs(root, 56))


def compare_binary_trees(head_one, head_two) -> bool:
    if not head_one and not head_two:
        return True
    if not head_one or not head_two:
        return False
    if head_one.value != head_two.value:
        return False

    return compare_binary_trees(head_one.left_child, head_two.left_child) and \
        compare_binary_trees(head_one.right_child, head_two.right_child)


c_node_2 = TreeNode(10)
c_node_3 = TreeNode(30)

root1 = TreeNode(20, c_node_2, c_node_3)
root2 = TreeNode(20, c_node_3, c_node_2)
# print(compare_binary_trees(root1, root2))

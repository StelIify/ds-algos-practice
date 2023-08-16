from data_structures.trees.binary_search_trees import TreeNode, insert
from data_structures.queue import Queue


def invert_tree_bfs(root: TreeNode):
    if not root:
        return root

    q = Queue(root)

    while len(q):
        current = q.dequeue()
        current.left_child, current.right_child = current.right_child, current.left_child
        if current.left_child:
            q.enqueue(current.left_child)
        if current.right_child:
            q.enqueue(current.right_child)
    return root


def invert_tree_dfs(root: TreeNode):
    if not root:
        return root

    temp = root.left_child
    root.left_child = root.right_child
    root.right_child = temp

    invert_tree_bfs(root.left_child)
    invert_tree_bfs(root.right_child)
    return root


node_1 = TreeNode(2)
node_2 = TreeNode(7)
root = TreeNode(4, node_1, node_2)
insert(1, root)
insert(3, root)
insert(6, root)
insert(9, root)

print(invert_tree_dfs(root))

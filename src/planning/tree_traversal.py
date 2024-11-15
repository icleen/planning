

def bfs(tree, search_value, test_results=False):
    node_queue = [tree.root]
    visited = []
    node_idx = 0
    value_found = False
    while node_idx < len(node_queue):
        # add the children of the current node to the stack
        cur_node = node_queue[node_idx]
        visited.append(cur_node.value)
        if cur_node.value == search_value:
            value_found = True
            break
        if cur_node.left_child is not None:
            node_queue.append(cur_node.left_child)
        if cur_node.right_child is not None:
            node_queue.append(cur_node.right_child)
        node_idx += 1

    if not test_results:
        return value_found
    return value_found, len(visited), visited


def dfs(tree, search_value, test_results=False):
    node_stack = [tree.root]
    visited = []
    value_found = False
    while len(node_stack) > 0:
        # add the children of the current node to the stack
        cur_node = node_stack[-1]
        visited.append(cur_node.value)
        if cur_node.value == search_value:
            value_found = True
            break
        node_stack = node_stack[:-1]
        if cur_node.right_child is not None:
            node_stack.append(cur_node.right_child)
        if cur_node.left_child is not None:
            node_stack.append(cur_node.left_child)

    if not test_results:
        return value_found
    return value_found, len(visited), visited


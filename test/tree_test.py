import numpy as np

from planning.trees import BinaryTree
from planning.tree_traversal import bfs, dfs


def create_test_trees():
    """
    Returns:
    - list: BinaryTree objects each with a filled tree for which operations can be performed
    """
    base_tree = BinaryTree()
    base_values = [50, 25, 75, 10, 37, 93, 88, 2, 65, 44, 23, 56]
    for base_value in base_values:
        base_tree.insert(base_value)
    print(base_tree.print())

    base_keys = {
        'search_value': 56, 
        'binary_search_num': 4,
        'binary_search': [50, 75, 65, 56],
        'bfs_visted_num': 11, 
        'bfs_visted': [50, 25, 75, 10, 37, 65, 93, 2, 23, 44, 56], 
        'dfs_visted_num': 10,
        'dfs_visted': [50, 25, 10, 2, 23, 37, 44, 75, 65, 56],
    }

    return [base_tree], [base_keys]


def test_breadth_first_search(test_trees, tree_keys):
    for ti, tree in enumerate(test_trees):
        test_key = tree_keys[ti]
        value_found, num_visited, path_values = bfs(tree, test_key['search_value'], test_results=True)
        assert num_visited == test_key['bfs_visted_num']
        assert path_values == test_key['bfs_visted']
        print('passed bfs test', ti + 1)
    return True


def test_depth_first_search(test_trees, tree_keys):
    for ti, tree in enumerate(test_trees):
        test_key = tree_keys[ti]
        value_found, num_visited, path_values = dfs(tree, test_key['search_value'], test_results=True)
        assert num_visited == test_key['dfs_visted_num'], 'num visisted wrong'
        assert path_values == test_key['dfs_visted'], 'visisted values wrong'
        print('passed dfs test', ti + 1)
    return True


def main():

    test_trees, tree_keys = create_test_trees()

    try:
        test_breadth_first_search(test_trees, tree_keys)
    except Exception as e:
        print('breadth first search error:', e)

    try:
        test_depth_first_search(test_trees, tree_keys)
    except Exception as e:
        print('depth first search error:', e)


if __name__ == '__main__':
    main()


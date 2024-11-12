

class Node:

    def __init__(self, value, parent, max_children=None):
        self._value = value
        self._parent = parent
        self._children = []
        self._max_children = max_children

    @property
    def value(self):
        return self._value
    
    @property
    def parent(self):
        return self._parent
    
    @property
    def children(self):
        return self._children
    
    @property
    def max_children(self):
        return self._max_children
    
    def add_child(self, child):
        self._children.append(child)


class BinaryNode(Node):

    def __init__(self, value, parent):
        super().__init__(value, parent, max_children=2)

        self._left_child = None
        self._right_child = None

    @property
    def left_child(self):
        return self._left_child

    @left_child.setter
    def left_child(self, left_child):
        self._left_child = left_child

    @property
    def right_child(self):
        return self._right_child

    @right_child.setter
    def right_child(self, right_child):
        self._right_child = right_child


class BinaryTree:

    def __init__(self, max_children=2):
        self._root_node = None
        self._max_children = max_children

    def insert(self, value):
        if self._root_node is None:
            self._root_node = BinaryNode(value, None)
        else:
            cur_node = self._root_node
            while cur_node is not None:
                if value <= cur_node.value:
                    if cur_node.left_child is None:
                        cur_node.left_child = BinaryNode(value, cur_node)
                        cur_node = None
                    else:
                        cur_node = cur_node.left_child
                else:
                    if cur_node.right_child is None:
                        cur_node.right_child = BinaryNode(value, cur_node)
                        cur_node = None
                    else:
                        cur_node = cur_node.right_child

    def print(self):
        if self._root_node is None:
            return 'empty tree'
        node_stack = [self._root_node]
        levels = [node_stack]
        node_idx = 0
        level_idx = 0
        while True:
            while level_idx < len(levels):
                while node_idx < len(levels[level_idx]):
                    # add the children of the current node to the next level of the stack
                    cur_node = node_stack[0]
                    node_stack = node_stack[1:]
                    if cur_node.left_child is not None:
                        node_stack.append(cur_node.left_child)
                        levels[level_idx].append(cur_node.left_child)


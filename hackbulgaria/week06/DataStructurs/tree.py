from copy import deepcopy

class Node():
    def __init__(self, data):
        self.data = data
        self.children = [] # all the child nodes
        self.parent = None
        self.node_level = 0

class Tree:
    def __init__(self, root):
        self.root = Node(root)
        self.depth = 0

    def add_child(self, parent, child):
        child = Node(child)
        if self.find(child.data):
            return False
        wanted_node = self.find_node(parent, self.root)
        if not wanted_node:
            return False
        wanted_node.children.append(child)
        child.parent = wanted_node
        child.node_level = child.parent.node_level + 1
        if child.node_level > self.depth:
            self.depth = child.node_level
        return True
    
    def find_node(self, data, node):
        cur = node
        if cur.data == data:
            return cur
        else:
            for child in cur.children:
                result = self.find_node(data, child)
                if result:
                    return result
                continue # optional

    def find(self, x):
        if self.find_node(x, self.root):
            return True
        return False     

    def height(self):
        return self.depth

    def count_nodes(self, node=None):
        if not node:
            cur = self.root
        else:
            cur = node
        if cur.children == []:
            return 2 # +1 for the last and + 1 for the root 
        else:
            for child in cur.children:
                if self.count_nodes(child):
                    return 1 + self.count_nodes(child)

    def tree_levels(self):
        if not self.root:
            return False
        cur = deepcopy(self.root.children)
        result = [[self.root.data]] #{k:[] for k in range(self.depth)}
        while True:
            new_nodes = []
            temp_result = []
            if len(cur) == 0:
                break
            for child in cur:
                temp_result.append(child.data)
                if len(child.children) > 0:
                    for grandchild in child.children:
                        new_nodes.append(grandchild)
            cur = new_nodes
            result.append(temp_result)
        return result


                
#result[child.node_level].append(child.data)

    """
        Returns a list of lists with the nodes foe each level1
        tree.tree_levels = [[5], [4, 3], [2]]
    """

foo = Tree(5)
foo.add_child(5, 1)
foo.add_child(5, 2)
foo.add_child(5, 3)
foo.add_child(1, 8)








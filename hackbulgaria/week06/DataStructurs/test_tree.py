import unittest
from tree import Tree

class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree(5)
        self.root = self.tree.root

    def test_add_child(self):
        self.tree.add_child(5, 4)
        self.assertEqual(len(self.root.children), 1)
        self.assertEqual(self.root.children[0].data, 4)
        self.tree.add_child(4, 2)
        self.assertEqual(self.root.children[0].children[0].data, 2)
        self.assertFalse(self.tree.add_child(2, 2))
        self.tree.add_child(5, 3)
        self.assertEqual(self.root.children[1].data, 3)

    def test_find(self):        
        self.tree.add_child(5, 4)
        self.tree.add_child(5, 3)
        self.tree.add_child(4, 2)
        self.assertTrue(self.tree.find(5))
        self.assertTrue(self.tree.find(2))
        self.assertFalse(self.tree.find(1))

    def test_height(self):
        self.tree.add_child(5, 4)
        self.tree.add_child(5, 3)
        self.tree.add_child(4, 2)
        self.assertEqual(self.tree.height(), 2)
        self.tree.add_child(2, 1)
        self.assertEqual(self.tree.height(), 3)

    def test_count_nodes(self):
        self.tree.add_child(5, 4)
        self.tree.add_child(5, 3)
        self.assertEqual(self.tree.count_nodes(), 3)
        self.tree.add_child(4, 2)
        self.assertEqual(self.tree.count_nodes(), 4)

    def test_tree_levels(self):        
        self.tree.add_child(5, 4)
        self.tree.add_child(5, 3)
        self.tree.add_child(4, 2)
        self.assertEqual(self.tree.tree_levels(), [[5], [4, 3], [2]])
        self.tree.add_child(3, 1)
        self.tree.add_child(1, 9)
        self.assertEqual(self.tree.tree_levels(), [[5], [4, 3], [2, 1], [9]])




if __name__ == '__main__':
    unittest.main()

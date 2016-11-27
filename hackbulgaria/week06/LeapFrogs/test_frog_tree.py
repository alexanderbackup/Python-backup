import unittest
from frog_tree import LeapFrogs

class TestLeapFrogs(unittest.TestCase):
    
    def setUp(self):
        self.frog_tree = LeapFrogs(3)

    def test_add_move(self):
        self.frog_tree.add_move()
        self.assertEqual(self.frog_tree.root.data, '>>>_<<<')
        self.frog_tree.add_move(self.frog_tree.root)
        self.assertEqual(len(self.frog_tree.root.next), 4)

    def test_find_answer(self):
        self.frog_tree = LeapFrogs(3)
        self.frog_tree.add_move(self.frog_tree.root)
        self.assertTrue(self.frog_tree.find_answer(self.frog_tree.root, self.frog_tree.frogs_end)) # '>>>_<<<' => '<<<_>>>' Example


    def test_valid_positions(self):
        self.frog_tree.add_move() # DO NOT FORGET !
        self.assertEqual(self.frog_tree.valid_positions(self.frog_tree.root), {'>>><_<<', '>>><<_<', '>_>><<<', '>>_><<<'})

    

if __name__ == '__main__':
    unittest.main()

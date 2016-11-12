import unittest
from game_of_life import GameOfLife
from unittest import mock

class TestGameOfLife(unittest.TestCase):
    def setUp(self):
        self.game = GameOfLife({(0, 1), (1, 1), (2, 1)}, 3)

    def test_set_live_cells(self):
        self.assertEqual(self.game.grid,
                         [[False, True, False], 
                          [False, True, False],
                          [False, True, False]])

    def test_new_matrix(self):
        self.assertEqual(self.game.new_matrix(),
                         [[False, False, False], 
                          [False, False, False],
                          [False, False, False]])

    def test_get_coordinates(self):
        self.assertEqual(self.game.get_coordinates(), 
                         {(0, 1), (1, 2), (0, 0), (2, 1), (2, 0), (2, 2), (1, 0), (1, 1), (0, 2)})

    def test_calculate_next_generation(self):
        self.assertEqual(self.game.calculate_next_generation(),
                         [[False, False, False], 
                          [True, True, True],
                          [False, False, False]])
    
    def test_calculate_liveness(self):
        self.assertTrue(self.game.calculate_liveness(1, 1), True)
        self.assertFalse(self.game.calculate_liveness(0, 0), False)

    def test_validate_coordinates(self):
        self.assertTrue(self.game.validate_coordinates(1, 1), True)
        self.assertFalse(self.game.validate_coordinates(-1, 1), False)

#    def test_random_population(self):
#        self.assertEqual(self.game.random_population(), 1)


if __name__ == '__main__':
    unittest.main()



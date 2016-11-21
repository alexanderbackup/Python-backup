import unittest
from ll_boiler_plate import LinkedList


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_adding_element(self):
        self.ll.add_element(4)
        self.assertEqual(self.ll.size(), 1)

    def test_set_element(self):
        self.ll.add_element(1)
        self.ll.add_element(2)
        self.ll.add_element(3)
        self.assertEqual(self.ll.index(1).data, 2)
        self.ll.set_element(1, 'smth')
        self.assertEqual(self.ll.index(1).data, 'smth')

    def test_remove_element(self):
        self.ll.add_element(4)
        size = self.ll.size()
        self.ll.remove(0)
        size2 = self.ll.size()
        self.assertFalse(size == size2)

    def test_remove_element2(self):
        self.ll.add_element(1)
        self.ll.add_element(2)
        self.ll.add_element(3)
        self.ll.add_element(4)
        self.ll.remove(2)
        self.assertEqual(self.ll.index(2).data, 4)

    def test_pprint(self):
        self.ll.add_element(1)
        self.ll.add_element(2)
        self.ll.add_element(3)
        self.ll.add_element(4)
        self.assertEqual(self.ll.pprint(), '[1, 2, 3, 4]')

    def test_check_if_string(self):
        self.assertEqual(self.ll.check_if_string('smth'), '"smth"')
        def test_str():
            pass
        self.assertEqual(self.ll.check_if_string(test_str), 'test_str')



    def test_add_at_index(self): # , index, data
        self.ll.add_element(1)
        self.ll.add_element('here')
        self.assertEqual(self.ll.index(1).data, 'here')
        self.ll.add_at_index(1, 'there')
        self.assertEqual(self.ll.index(1).data, 'there')

    def test_add_first(self):
        self.ll.add_element(1)
        self.assertEqual(self.ll.index(0).data, 1)
        self.assertTrue(self.ll.list_size == 1)
        self.ll.add_first('new_first')
        self.assertEqual(self.ll.index(0).data, 'new_first')
        self.assertTrue(self.ll.list_size == 2)

    def test_add_list(self):
        self.ll.add_element(1)
        self.ll.add_element(2)
        self.ll.add_element(3)
        self.ll.add_element(4)
        self.assertEqual(self.ll.add_list(['a', 'b', 'c']),
                                       ['a', 'b', 'c', 1, 2, 3, 4])

    def test_add_linked_list(self):
        self.ll.add_element(1)
        self.ll.add_element(2)
        self.ll.add_element(3)
        self.ll2 = LinkedList()
        self.ll2.add_element('a')
        self.ll2.add_element('b')
        self.ll2.add_element('c')
        self.ll.add_linked_list(self.ll2.head)
        self.assertEqual(self.ll.pprint(), '[1, 2, 3, "a", "b", "c"]')





if __name__ == '__main__':
    unittest.main()

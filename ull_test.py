# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:28:24 2022

@author: liurh
"""
import unittest
from hypothesis import given, settings
import hypothesis.strategies as st
from unrolled_linked_list import UnrolledLinkedList


class TestMutableULList(unittest.TestCase):
    # first we use unit test!

    def test_add_and_remove(self):
        print('\nTesting add and remove...')
        ull = UnrolledLinkedList()
        ull.add(1)
        self.assertEqual(ull.to_list(), [1])
        ull.add(2)
        self.assertEqual(ull.to_list(), [1, 2])
        ull.remove(1)
        self.assertEqual(ull.to_list(), [2])
        ull.remove(2)
        self.assertEqual(ull.to_list(), [])

    def test_traversal(self):
        print('Testing traversal...')
        ull = UnrolledLinkedList(4)
        self.assertEqual(ull.traversal(), None)

    def test_to_list(self):
        print('Testing to_list...')
        ull = UnrolledLinkedList(4)
        ull.add(1)
        ull.add(2)
        ull.add(3)
        self.assertEqual(type(ull.to_list()), list)

    def test_from_list(self):
        print('Testing from_list...')
        dlist = [1, 2, 3, 4]
        ull = UnrolledLinkedList(4)
        self.assertEqual(ull.from_list(dlist), None)

    def test_size(self):
        print('Testing size...')
        ull = UnrolledLinkedList(4)
        ull.add(1)
        ull.add(2)
        ull.add(3)
        ull.add(4)
        self.assertEqual(ull.size(), 4)

    def test_set_element(self):
        print('Testing set_element...')
        ull = UnrolledLinkedList(4)
        lit = [1, 2, 3, 4]
        ull.from_list(lit)
        self.assertEqual(ull.set_element(1, 999).to_list(), [1, 999, 3, 4])

    def test_ull_filter(self):
        print('Testing ull_filter...')
        ull = UnrolledLinkedList(4)
        ull.from_list([1, 2, 3, 4])
        ull.ull_filter()
        self.assertEqual(ull.to_list(), [2, 4])

    def test_ull_map(self):
        print('Testing ull_map...')
        ull = UnrolledLinkedList(4)
        ull.from_list([1, 2, 3, 4])
        ull.ull_map(lambda x: x**2)
        self.assertEqual(ull.to_list(), [1, 4, 9, 16])

    def test_ull_reduce(self):
        print('Testing ull_reduce...')
        ull = UnrolledLinkedList(4)
        ull.from_list([1, 2, 3, 4])
        self.assertEqual(ull.ull_reduce(lambda x, y: x+y), 10)

    def test_iterate(self):
        print('Testing iterate...')
        ull = UnrolledLinkedList()
        ull.from_list([1, 2, 3, 4])
        iter1 = iter(ull)
        iter2 = iter(ull)
        arr = ull.to_list()
        for cyi in range(4):
            self.assertEqual(next(iter1), arr[cyi])
        for cyi in range(4):
            self.assertEqual(next(iter2), arr[cyi])

    def test_reverse(self):
        print('Testing reverse...')
        ull = UnrolledLinkedList(4)
        ull.from_list([1, 2, 3, 4])
        b = ull.reverse()
        self.assertEqual(b.to_list(), [4, 3, 2, 1])

    def test_is_member(self):
        print('Testing is_member...')
        ull = UnrolledLinkedList(4)
        ull.from_list([1, 2, 3, 4])
        b = ull.is_member(3)
        self.assertEqual(b, True)
        b = ull.is_member(5)
        self.assertEqual(b, False)

    def test_empty(self):
        print('Testing empty...')
        ull = UnrolledLinkedList()
        ull.from_list([1, 2, 3, 4])
        b = ull.empty()
        self.assertEqual(b, None)

# ---------------------------------------------
    # then we use PBT test!
    @settings(max_examples=10)
    @given(st.lists(st.integers()))
    def test_concat_PBT(self, a):
        ull = UnrolledLinkedList()
        ullcp = UnrolledLinkedList()
        ull.from_list([1, 2, 3])
        ullcp.from_list(a)
        result = ull.to_list()+ullcp.to_list()
        ull_list = ull.concat(ullcp).to_list()
        self.assertEqual(ull_list, result)

    @settings(max_examples=10)
    @given(st.lists(st.integers()))
    def test_monoid_properties_PBT(self, a):
        ull1 = UnrolledLinkedList()
        ull2 = UnrolledLinkedList()
        ull3 = UnrolledLinkedList()
        ull1.from_list(a)
        ull2.from_list(a)
        ull3.from_list(a)
        # test identity element
        ie1 = ull1.concat(ull2, empty=ull1).to_list()
        ie2 = ull2.concat(ull1, empty=ull1).to_list()
        self.assertEqual(ie1, ie2)
        # test associativity
        obj1 = ull1.concat(ull2).concat(ull3).to_list()
        obj2 = ull2.concat(ull3).concat(ull1).to_list()
        self.assertEqual(obj1, obj2)


if __name__ == '__main__':
    unittest.main()

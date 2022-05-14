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
        ull = UnrolledLinkedList(4)
        self.assertEqual(ull.traversal(), None)

    def test_to_list(self):
        ull = UnrolledLinkedList(4)
        ull.add(1)
        ull.add(2)
        ull.add(3)
        self.assertEqual(type(ull.to_list()), list)

    def test_from_list(self):
        dlist = [1, 2, 3, 4]
        ull = UnrolledLinkedList(4)
        self.assertEqual(ull.from_list(dlist), None)

    def test_size(self):
        ull = UnrolledLinkedList(4)
        ull.add(1)
        ull.add(2)
        ull.add(3)
        ull.add(4)
        self.assertEqual(ull.size(), 4)

    def test_set_element(self):
        ull = UnrolledLinkedList(4)
        lit = [1, 2, 3, 4]
        ull.from_list(lit)
        self.assertEqual(ull.set_element(1, 999).to_list(), [1, 999, 3, 4])

    def test_ull_filter(self):
        ull = UnrolledLinkedList(4)
        ull.from_list([1, 2, 3, 4])
        ull.ull_filter()
        self.assertEqual(ull.to_list(), [2, 4])

    def test_ull_map(self):
        ull = UnrolledLinkedList(4)
        ull.from_list([1, 2, 3, 4])
        ull.ull_map(lambda x: x**2)
        self.assertEqual(ull.to_list(), [1, 4, 9, 16])

    def test_ull_reduce(self):
        ull = UnrolledLinkedList(4)
        ull.from_list([1, 2, 3, 4])
        self.assertEqual(ull.ull_reduce(lambda x, y: x+y), 10)

    def test_iterate(self):
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
        ull = UnrolledLinkedList(4)
        ull.from_list([1, 2, 3, 4])
        b = ull.reverse()
        self.assertEqual(b.to_list(), [4, 3, 2, 1])

    def test_is_member(self):
        ull = UnrolledLinkedList(4)
        ull.from_list([1, 2, 3, 4])
        b = ull.is_member(3)
        self.assertEqual(b, True)
        b = ull.is_member(5)
        self.assertEqual(b, False)

    def test_empty(self):
        ull = UnrolledLinkedList()
        ull.from_list([1, 2, 3, 4])
        b = ull.empty()
        self.assertEqual(b, None)

    # new: test which demonstrates how capacity can increase.
    def test_capacity(self):
        ull = UnrolledLinkedList()
        self.assertEqual(ull.capacity, 4)
        # dynamically extended
        ull.capacity = 6
        self.assertEqual(ull.capacity, 6)

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
    def test_monoid_identity_PBT(self, a):
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

    # new: Test associativity, in sequence of concatenations.
    @settings(max_examples=10)
    @given(st.lists(st.integers()))
    def test_monoid_associativity_PBT(self, a):
        ull_a = UnrolledLinkedList()
        ull_b = UnrolledLinkedList()
        ull_c = UnrolledLinkedList()
        ull_a.from_list(a[:3])
        ull_b.from_list(a[3:7])
        ull_c.from_list(a[7:])
        # (a.b).c
        ie1 = ull_a.concat(ull_b).concat(ull_c).to_list()
        # a.(b.c)
        ie2 = ull_a.concat(ull_b.concat(ull_c)).to_list()
        # (a.b).c = a.(b.c)
        self.assertEqual(ie1, ie2)


if __name__ == '__main__':
    unittest.main()

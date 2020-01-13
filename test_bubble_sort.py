import unittest
from bubble_sort import *

class testbublesort(unittest.TestCase):

    #tests of the function name-bubbleSort(arr)

    def test_bubblesort1(self):
        arr1=[4,2,1,7]
        expected=[1,2,4,7]
        bubbleSort(arr1)

        self.assertEqual(expected,arr1)

    def test_bubblesort2(self):
        arr1 = ['w', 'a', 'v', 'o']
        expected = ['a', 'o', 'v', 'w']
        bubbleSort(arr1)

        self.assertEqual(expected, arr1)

    def test_bubblesort3(self):
        arr1 = []
        expected = "No array insert"
        result=bubbleSort(arr1)

        self.assertEqual(expected, result)

    #  If no elements are lost from the array

    def test_bubblesort4(self):
        arr1 = [4, 2, 1, 7]
        expected = len([1, 2, 4, 7])
        bubbleSort(arr1)

        self.assertEqual(expected,len(arr1))




# GROUP -> HDU123 - Liu Riheng & Chen Weite - lab 1 - variant 1

# Student number:

Liu Riheng 212320037
Chen Weite 212320039

## Laboratory work description

Lab1 includes the definition of unrolled linked list data structure and the implementation of data structure related mutable algorithms.
We implemented at least 18 methods. Then we test the data structure and its algorithms using unit tests and PBT tests.
After GitHub active, we passed all tests.


## Project structure

- `UnrolledLinkedList.py` -- implementation of `UnrolledLinkedList` and `Node` class with more than 18 methods.
   
- `ull_test.py` -- unit and PBT tests for `UnrolledLinkedList`.

- .github/workflows/check.yml -- for GitHub active.

## Contribution

- Liu Riheng
   1.Define data structures and implement basic methods such as adding, deleting, traversal, etc.
   2.Implement `ull_test.py` which include unit and PBT tests.
   3.Complete readme and GitHub active.
- Chen Weite
   1.Implement other methods of UnrolledLinkedList.
   2.Check code style and unify code formatting.
   3.Collect the resources required by lab1, including the use of software, the description of data structure.

## Changelog

- 13.04.2022 - 0
Initial
1.Implement `UnrolledLinkedList.py` and `ull_test.py`
2.GitHub active successfully
3.Update README

- 25.04.2022 - 0
1. Bad naming. Read about how to name modules and tests for them.
2. Update GitHub action configuration from the template.
3. Incorrect concat  implementation. Check the task. Rewrite tests.
4. Not all PBT tests implemented. You need to check all monoid properties.
5. test_add_and_remove — you don’t actually check add and remove function. You need to check that data actually changed inside. Rewrite it.
6. Make `capacity` argument optimal for UnrolledLinkedList constructor.
7. Your iterator implementation is limited. Test that the two iterators on one data structure should work in parallel correctly.
0.All the above tasks are completed!

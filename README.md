
# GROUP -> HDU123 - Liu Riheng & Chen Weite - lab 1 - variant 1

# Student number

Liu Riheng 212320037
Chen Weite 212320039

## Laboratory work description

Lab1 includes the definition of unrolled linked list data structure
and the implementation of
data structure related mutable algorithms.
We implemented at least 18 methods. Then we test the data structure
and its algorithms using unit tests and PBT tests.
After GitHub active, we passed all tests.

## Project structure

- `UnrolledLinkedList.py` -- implementation of `UnrolledLinkedList`

and `Node` class with more than 18 methods.

- `ull_test.py` -- unit and PBT tests for `UnrolledLinkedList`.

- .github/workflows/check.yml -- for GitHub active.

## Contribution

- Liu Riheng
1. Define data structures and implement basic methods.
2. Implement `ull_test.py` which include unit and PBT tests.
3. Complete readme and GitHub active.

- Chen Weite
1. Implement other methods of UnrolledLinkedList.
2. Check code style and unify code formatting.
3. Collect the resources required by lab1.

## Changelog

- 13.04.2022 - 0
1. Initial.
2. Implement `UnrolledLinkedList.py` and `ull_test.py`.
3. GitHub active successfully.
4. Update README.

- 25.04.2022 - 0
1. Module has been renamed.
2. Updated GitHub action configuration from the template.
3. Rewritten concat method.
4. Tested all monoid properties with PBT.
5. Rewritten test_add_and_remove method.
6. Make `capacity` argument optimal for UnrolledLinkedList constructor.
7. Rewrite the iterator.

- 25.04.2022 - 1
1. All the above tasks are completed!

- 02.05.2022 - 0
1. Rename `ull_test.py` to `unrolled_linked_list_test.py`.
2. Add test associativity in sequence of concatenations.
3. Add test which demonstrates how capacity can increase.

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:40:54 2022

@author: liurh
"""


class Node:
    def __init__(self):
        self.length = 0
        self.array = []
        self.next = None


class Next:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.offset >= len(self.wrapped.to_list()):
            raise (StopIteration)
        else:
            item = self.wrapped.to_list()[self.offset]
            self.offset += 1
            return item


class UnrolledLinkedList:
    def __init__(self, capacity=4):
        # maximum capacity of an array in node
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.ull_iter = []
        self.s = []
        self.wrapped = self

    def __iter__(self):
        return Next(self.wrapped)
    
    # this method inserts the given value in the list
    def add(self, value):
        if self.head is None:
            self.head = Node()
            self.head.array.append(value)
            self.head.length += 1
            self.tail = self.head
        elif self.tail.length + 1 <= self.capacity:
            self.tail.array.append(value)
            self.tail.length += 1
        else:
            new_node = Node()
            half_length = self.tail.length//2
            tmp = self.tail.array[half_length:]
            new_node.array.extend(tmp)
            new_node.array.append(value)
            # Update
            new_node.length = len(new_node.array)
            self.tail.length = half_length
            self.tail.next = new_node
            self.tail = new_node

    # prints all the elements of the unrolled linked list
    def traversal(self):
        temp = self.head
        while temp:
            for i in range(0, temp.length):
                print(temp.array[i], end="\t")
            print()
            temp = temp.next


    def remove(self, value, ull_type='value'):
        # find the given value and delete it 
        temp = self.head
        count = -1
        while temp:
            for i in range(0, temp.length):
                count += 1
                con1 = (type(temp.array[i]) == dict)
                con2 = (ull_type == 'dict')
                if con1 & con2:
                    temp.array[i] = list(temp.array[i].keys())[0]
                elif (ull_type == 'list'):
                    if(count == value):
                        temp.array[i] = value
                    else:
                        continue
                if temp.array[i] == value:
                    temp.array.pop(i)
                    temp.array.append(None)
                    temp.length -= 1
                    while temp.length < (self.capacity//2) and temp.next:
                        temp.array[temp.length] = temp.next.array.pop(0)
                        temp.length +=1
                        temp.next.length -= 1
                    if temp.next and temp.next.length < (self.capacity//2):
                        t = temp.length
                        q = temp.next.length
                        temp.array[t:t+q] = temp.next.array[:q]
                        temp.length += temp.next.length
                        temp.next = temp.next.next
                    return
            temp = temp.next
        raise ValueError(f'Value {value} does not exist in the list')

    def to_list(self):
        # organize the data with an array
        p = self.head
        arr = []
        while p:
            arr.extend(p.array[0:p.length])
            p = p.next
        return arr

    def from_list(self, arr=[]):
        # add a list to UnrolledLinkedList
        for cyi in range(len(arr)):
            self.add(arr[cyi])

    def size(self):
        return len(self.to_list())

    def reverse(self):
        ull_list = self.to_list()
        ull_list.reverse()
        self = UnrolledLinkedList(self.capacity)
        self.from_list(ull_list)
        return self

    def is_member(self, value):
        p = self.head
        while p:
            if(value in p.array):
                # if value is in p.array, find successfully
                return True
            p = p.next
        # if not in the UnrolledLinkedList...
        return False

    def set_element(self, idx, value):
        # update an element according index and value
        ull_list = self.to_list()
        ull_list[idx] = value
        self = UnrolledLinkedList(self.capacity)
        self.from_list(ull_list)
        return self

    def ull_filter(self, condition='iseven'):
        if (condition == 'iseven'):
            [self.remove(cyi,'list') for cyi in range(self.size()//2)]

    def ull_map(self,function):
        p = self.head
        while p:
            for cyi in range(p.length):
                p.array[cyi] = function(p.array[cyi])
            p = p.next

    def ull_reduce(self,function):
        # iterative processing
        ull_list = self.to_list()
        for _ in range( len(ull_list)-1 ):
            ull_list[0] = function(ull_list[0], ull_list[1])
            ull_list.pop(1)
        return ull_list[0]

    def empty(self):
        self = None
        return self

    def concat(self, obj, empty=None):
        newobj = UnrolledLinkedList()
        newobj.from_list(self.to_list())
        if empty is not None:
            empty = newobj.empty()
        if newobj is None:
            return obj
        elif obj is None:
            return newobj
        else:
            olist = obj.to_list()
            for elist in olist:
                newobj.add(elist)
            return newobj

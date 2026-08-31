from __future__ import print_function
import math

class MinHeap:
    def __init__(self):
        self.arr = []

    def left(self, i): return 2 * i + 1

    def right(self, i): return 2 * i + 2

    def parent(self, i): return (i - 1) // 2
    
    def get_min(self):
        return self.arr[0] if self.arr else None
    
    def insert(self, k):
        self.arr.append(k)
        i = len(self.arr) - 1
        
        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    def decrease_key(self, i, new_val):
        self.arr[i] = new_val
        
        while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    def extract_min(self):
        if len(self.arr) <= 0: return None
        if len(self.arr) == 1: return self.arr.pop()
        
        res = self.arr[0]
        self.arr[0] = self.arr.pop() 
        self.min_heapify(0)
        return res

    def delete_key(self, i):
      
        self.decrease_key(i, -float('inf'))
        
        self.extract_min()

    def min_heapify(self, i):
        l, r, n = self.left(i), self.right(i), len(self.arr)
        smallest = i
        
        if l < n and self.arr[l] < self.arr[smallest]: smallest = l
        if r < n and self.arr[r] < self.arr[smallest]: smallest = r
          
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)

if __name__== "__main__":
    h = MinHeap()
    h.insert(3)
    h.insert(2)
    h.delete_key(1)
    h.insert(15)
    h.insert(5)
    h.insert(4)
    h.insert(45)

    print(h.extract_min(), end=" ") 
    print(h.get_min(), end=" ") 
    
    h.decrease_key(2, 1)
    print(h.extract_min())
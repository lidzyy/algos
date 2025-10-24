"""
    O que é uma Linked List?
        head -> [A] -> [B] -> [C] -> None

    Head: Linked List [A] -> [B] -> [C]
    node: tem um valor e aponta para o proximo node [A] -> 
    head.val: valores de cada node
    head.next: aponta para o proximo node
"""

class Node:
    def __init__(self, val, next = None):
       self.val = val # valor
       self.next = next # proximo node

class SinglyLinkedList:
    def __init__(self):
        self.head = None # aponta para o primeiro node
        self.n = 0 # tamanho da lista

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.n == 0
    
    def push_front(self, x):
       new_node = Node(x)
       new_node.next = self.head
       self.head = new_node
       self.n += 1

    def to_list(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out 
             
    def pop_front(self):
        if self.head == None:
            raise IndexError("pop from empty list")
        x = self.head.val # 30
        self.head = self.head.next # passa a ser 20, o 30 sai fora da lista
        self.n -= 1
        return x # return do valor removido

    def find(self, x):                
        cur = self.head
        while cur:
            if cur.val == x:
               return True
            cur = cur.next             
        return False

    def remove(self, x):
        if self.head is None:
            return False

        if self.head.val == x:
           self.head = self.head.next 
           self.n -=1
           return True
        
        prev = self.head
        cur = self.head.next
        while cur:
            if cur.val == x:
                prev.next = cur.next # remove cur da lista
                self.n -= 1
                return True
            prev = cur # <- Avanca prev
            cur = cur.next # <- Avanca cur
        return False

s = SinglyLinkedList()
s.push_front(10)
# 10 
s.push_front(20)
# 20 .. 10 
s.push_front(30)
# 30 .. 20 .. 10

print(len(s))         # 3
print(s.head.val)     # 30
print(s.head.next.val) # 20
print(s.to_list()) # 30 20 10
print(s.find(999)) # False
print(s.find(20)) # True
print(s.remove(20)) # True
print(s.remove(33)) # False
print(s.to_list()) # 30 10
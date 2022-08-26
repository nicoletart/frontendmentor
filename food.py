from distutils.command.build import build
from random import randint

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def getEl(self):
        return self.data

    def getNext(self):
        return self.next

class Bucket:
   def __init__(self):
      self.bucket=[]
   def update(self, key):
      found=False
      for i,k in enumerate(self.bucket):
         if key==k:
            self.bucket[i]=key
            found=True
            break
      if not found:
         self.bucket.append(key)
   def get(self, key):
      for k in self.bucket:
         if k==key:
            return True
      return False
   def remove(self, key):
      for i,k in enumerate(self.bucket):
         if key==k:
            del self.bucket[i]
class HashSet:
   def __init__(self):
      self.key_space = 2096
      self.hash_table=[Bucket() for i in range(self.key_space)]
   def add(self, key):
     # hash_key=key%self.key_space
      hash_key = abs(hash(key)) % (self.key_space)
      self.hash_table[hash_key].update(key)
   def remove(self, key):
      #hash_key=key%self.key_space
      hash_key = abs(hash(key)) % (10 ** 8)
      hash_key = abs(hash(key)) % (self.key_space)
   def contains(self, key):
      hash_key = abs(hash(key)) % (self.key_space)
      return self.hash_table[hash_key].get(key)

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    @property
    def values(self):
        return [node.value for node in self]
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head



food1 = {}
burger_ing = ["lettuce", "tomato", "bread"]
food1[tuple(burger_ing)] = "burger"

hotdog_ing = ["bread", "sausage"]
food1[tuple(hotdog_ing)] = "hotdog"

chocolate_ing = ["milk"]
food1[tuple(chocolate_ing)] = "chocolate"

global fridge
global final_recipes
fridge = []
final_recipes = []

def empty_fridge():
    fridge.clear()
    final_recipes.clear()

def add_food(ex):
    num = 0
    input_string = ex
    items = input_string.split()
    fridge.extend(items)
    return fridge

def print_fridge():
    print(fridge)

def listToString(st):
    str1 = ", " 
    return (str1.join(st))

def lookInFridge(s):
    new = []
    for i in s:
        if i not in new:
            i = i.lower()
            new.append(i)
    return new

def check():
    map = HashSet()
    global final_recipes
    final_recipes = []
    f = lookInFridge(fridge)
    for i in f:
        map.add(i)
    for key, value in food1.items():
        num = 0
        for item in key:
            if (map.contains(item)):
                num += 1
                if num == len(key):
                    final_recipes.append(value)
        
    #print((final_recipes))
  

def generator ():
    if (final_recipes == []):
        return("No meal can be made with these ingredients")
    else:
        return(final_recipes[randint(0, len(final_recipes)-1)])




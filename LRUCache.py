class Node:
  def __init__(self, key, val):
    self.key, self.val = key, val
    self.prev, self.next = None, None
    
class LRUCache:
  def __init__(self, capacity:int):
    self.cap = capacity
    self.cache = {}
    
    self.left, self.right = Node(0,0), Node(0,0)
    self.left.next, self.right.prev = self.right, self.left
    
  def remove(self, node:Node):
    prev,next = node.prev, node.next
    prev.next = next
    next.prev = prev
    
  def add(self, node:Node):
    prev = self.right.prev
    self.right.prev = node 
    prev.next = node
    node.prev, node.next = prev, self.right
  
  def get(self, key:int) -> key:
    # make it mru when we do get
    if key in self.cache:
      self.remove(self.cache[key]) # unlinks the adjacent nodes
      self.insert(self.cache[key])
      return self.cache[key].val
    return -1
  
  def put(self, key:int, value:int) -> None:
    if key in self.cache:
      self.remove(self.cache[key])
    self.cache[key] = Node # add the node to the hashmap
    self.put(self.cache[key]) # relinks the node as the mru
    
    if len(self.cache) > self.cap:
      lru = self.left.next
      self.remove(lru)
      del self.cache[lru.key]
    

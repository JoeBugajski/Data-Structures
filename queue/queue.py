# class Queue: # Using an array
#   def __init__(self):
#     self.size = 0
#     # what data structure should we
#     # use to store queue elements?
#     self.read = 0
#     self.write = 0
#     self.storage = [] 

#   def enqueue(self, item):
#     if self.read == self.write:
#         self.storage.clear()
#         self.storage.append(item)
#         self.write = 1
#         self.read = 0
#     else:
#         self.storage.append(item)
#         self.write += 1
  
#   def dequeue(self):
#     if self.read == self.write:
#         return None
#     else:
#         x = self.storage[self.read]
#         self.read += 1
#         return x

#   def len(self):
#     if self.read == self.write:
#         return 0
#     else:
#         return self.write - self.read

class Queue: # Using a linked-list
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = [] 

  def enqueue(self, item):
    pass
  
  def dequeue(self):
    pass

  def len(self):
    pass

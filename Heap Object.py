def parent(i): return (i + 1)//2 - 1

class heap(object):
  
  def __init__(self, li):
    self.li = li
    self.heap_size = 0
    self.length = len(li)

  def max_heapify(self, i):
    "Maintain the heap below the node i without recursive call"
    large = i
    left = 2*(i+1) - 1
    right = 2*(i+1)
    if left < self.heap_size and self.li[left] > self.li[large]:
      large = left
    if right < self.heap_size and self.li[right] > self.li[large]:
      large = right
    while large != i:
      self.li[large], self.li[i] = self.li[i], self.li[large]
      
      i = large
      left = 2*(i+1) - 1
      right = 2*(i+1)
      if left < self.heap_size and self.li[left] > self.li[large]:
        large = left
      if right < self.heap_size and self.li[right] > self.li[large]:
        large = right
    return

  def build_max_heap(self):
    self.heap_size = self.length
    n_2 = self.heap_size // 2
    for i in xrange(n_2 - 1, -1, -1):
      self.max_heapify(i)
    return

  def sort(self):
    "Sort the entire list from small to large"
    self.build_max_heap()
    for i in xrange(self.length - 1, 0, -1):
      self.li[0], self.li[i] = self.li[i], self.li[0]
      self.heap_size -= 1
      self.max_heapify(0)
    self.heap_size = 0
    return

  def first(self):
    return self.li[0]

  def extract_max(self):
    "Return the max item and the heap size"
    if self.heap_size < 1:
      print 'No element in heap'
      return 0 #heap underflow
    maxv = self.li[0]
    self.li[0] = self.li[self.heap_size - 1]
    self.heap_size -= 1
    self.max_heapify(0)
    return maxv

  def heap_list(self):
    "Return the portion of the list that is actually a heap"
    return self.li[0:self.heap_size]
  
  def shrink(self):
    "Delete the portion of the list that is not in the heap"
    del self.li[self.heap_size:self.length]
    self.length = len(self.li)
    return

  def max_heapify_up(self, i):
    "Swap the key with the parent if the key is larger"
    i_par = parent(i)
    while i > 0 and self.li[i_par] < self.li[i]:
      self.li[i_par], self.li[i] = self.li[i], self.li[i_par]
      i = i_par
      i_par = parent(i)
    return
  
  def change_key(self, i, key):
    "Change the key of the node i"
    if key < self.li[i]:
      self.li[i] = key
      self.max_heapify(i)
    elif key > self.li[i]:
      self.li[i] = key
      self.max_heapify_up(i)
    return

  def max_heap_insert(self, key):
    'insert key, add new space to the list if necessary'
    self.heap_size += 1
    if self.length < self.heap_size:
      self.li.append(key)
      self.length = len(self.li)
    else:
      self.li[self.heap_size - 1] = key
    self.max_heapify_up(self.heap_size - 1)
    return

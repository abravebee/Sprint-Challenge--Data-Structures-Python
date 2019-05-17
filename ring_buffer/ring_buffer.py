class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    length = len(self.storage)
    #if the current storage is at capacity
    for i in range (0, length):
        if self.storage[i] == None:
            self.storage[i] = item
            print(f"for i self.storage: {self.storage}")
            return
    #append to current oldest index
    self.storage[self.current] = item
    #next index is now the oldest
    if self.current == self.capacity-1:
        self.current = 0
    else:
        self.current += 1    
    pass

  def get(self):
    # have a result array
    result = []
    # for each element
    for element in self.storage:
        # check that element is not none
        if element is not None:
            # append to result array
            result.append(element)
    # return array
    return result
    pass

buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get())   # should return ['d', 'e', 'f']

buffer.append('g')
buffer.append('h')
buffer.append('i')

print(buffer.get())
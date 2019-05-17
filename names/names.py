import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        pass

# searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
    def contains(self, target):
        # compare target to root
        if target == self.value:
            return True
        # if it's smaller, check left side
        elif target < self.value:
            # first check that there is a left side; if not, return False
            if not self.left:
                return False
            # else, if it doesn't match the left side, call contains on left side with same target
            elif target != self.left:
                return self.left.contains(target)
            else:
                return True
        # else, check right side
        elif target > self.value:
            # first check that there is a right side; if not, return False
            if not self.right:
                return False
            # else, if it doesn't match the right side, call contains on right side with same target
            elif target != self.right:
                return self.right.contains(target)
            else:
                return True            
        pass


duplicates = []

# ~20 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# ~0.33 seconds!!
# plug in first value to root
tree = BinarySearchTree(names_1[0])
# add first file's names to tree
for name in names_1:
    tree.insert(name)
for name in names_2:
    # use contain search function to find duplicates
    if tree.contains(name):
        # add duplicates to list
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


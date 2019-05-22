Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
    O(n) because the for loop runs linearly based on the capacity input to the class.

2. What is the space complexity of your ring buffer's `append` function?
    O(1) because the capacity is always the same and we're not adding extra space when appending values, only replacing space already taken up.

3. What is the runtime complexity of your ring buffer's `get` method?
    O(n) because we have another for loop going through the whole storage.

4. What is the space complexity of your ring buffer's `get` method?
    O(n) because the result array grows depending upon the values in storage.

5. What is the runtime complexity of the provided code in `names.py`?
    O(n^2) for nested for loops.

6. What is the space complexity of the provided code in `names.py`?
    O(n) because the duplicates array grows based on the values in the inputs.

7. What is the runtime complexity of your optimized code in `names.py`?
    O(n log n) because binary search trees are lovely, but we also have to search it for every element in names_2.

8. What is the space complexity of your optimized code in `names.py`?
    O(n^2) because I have to store all the names_1 values in the tree and then the duplicates array also grows based on input.
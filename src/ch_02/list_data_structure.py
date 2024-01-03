"""
The time complexity of various functions of a list can be summarized as follows using the Big O
notation:

• Inserting an element: The insertion of an element at the end of a list typically has a
constant time complexity, denoted as O(1). This means the time taken for this operation
remains fairly consistent, irrespective of the list’s size.

• Deleting an element: Deleting an element from a list can have a time complexity of O(n)
in its worst-case scenario. This is because, in the least favorable situation, the program
might need to traverse the entire list before removing the desired element.

• Slicing: When we slice a list or extract a portion of it, the operation can take time proportional
to the size of the slice; hence, its time complexity is O(n).

• Element retrieval: Finding an element within a list, without any indexing, can require
scanning through all its elements in the worst case. Thus, its time complexity is also O(n).

• Copying: Creating a copy of the list necessitates visiting every element once, leading to
a time complexity of O(n).
"""

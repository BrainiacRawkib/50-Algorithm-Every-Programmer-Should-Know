"""
The time complexity of various functions of tuples can be summarized as follows (using Big O
notation):

• Accessing an element: Tuples allow direct access to their elements via indexing. This
operation is constant time, O(1), meaning the time taken remains consistent regardless
of the tuple’s size.

• Slicing: When a portion of a tuple is extracted or sliced, the operation’s efficiency is proportional
to the size of the slice, resulting in a time complexity of O(n).

• Element retrieval: Searching for an element in a tuple, in the absence of any indexing
aid, might require traversing all its elements in the worst-case scenario. Hence, its time
complexity is O(n).

• Copying: Duplicating a tuple, or creating its copy, requires iterating through each element
once, giving it a time complexity of O(n).

Note: Wherever possible, immutable data structures (such as tuples) should be preferred
over mutable data structures (such as lists) due to performance. Especially when
dealing with big data, immutable data structures are considerably faster than mutable
ones. When a data structure is passed to a function as immutable, its copy does
not need to be created as the function cannot change it. So, the output can refer to
the input data structure. This is called referential transparency and improves the
performance. There is a price we pay for the ability to change data elements in lists
and we should carefully analyze whether it is really needed so we can implement
the code as read-only tuples, which will be much faster.
"""

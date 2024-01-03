"""
For Python dictionaries, the time complexities for various operations are listed here:

• Accessing a value by key: Dictionaries are designed for fast look-ups. When you have
the key, accessing the corresponding value is, on average, a constant time operation, O(1).
This holds true unless there’s a hash collision, which is a rare scenario.

• Inserting a key-value pair: Adding a new key-value pair is generally a swift operation
with a time complexity of O(1).

• Deleting a key-value pair: Removing an entry from a dictionary, when the key is known,
is also an O(1) operation on average.

• Searching for a key: Verifying the presence of a key, thanks to hashing mechanisms, is
usually a constant time, O(1), operation. However, worst-case scenarios could elevate
this to O(n), especially with many hash collisions.

• Copying: Creating a duplicate of a dictionary necessitates going through each key-value
pair, resulting in a linear time complexity, O(n).
"""

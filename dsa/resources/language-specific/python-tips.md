# Python Tips for DSA

## Built-in Data Structures

### List (Array)
```python
# Creation
arr = [1, 2, 3]
arr = list(range(10))  # [0,1,2,...,9]

# Operations
arr.append(4)          # O(1) amortized
arr.extend([5, 6])     # Add multiple
arr.insert(0, 0)       # O(n)
arr.pop()              # Remove last: O(1)
arr.pop(0)             # Remove first: O(n)
arr.remove(2)          # Remove by value: O(n)
arr.reverse()          # In-place reverse
arr.sort()             # In-place sort
sorted(arr)            # Return sorted copy
```

### Dictionary (Hash Map)
```python
# Creation
d = {'a': 1, 'b': 2}
d = dict(a=1, b=2)
d = {x: x**2 for x in range(5)}  # Dict comprehension

# Operations
d['c'] = 3             # O(1) avg
d.get('a', default)    # Safe access
d.pop('a')             # Remove
d.update({'d': 4})     # Merge
d.keys()               # Keys view
d.values()             # Values view
d.items()              # (key, value) pairs
```

### Set
```python
# Creation
s = {1, 2, 3}
s = set([1, 2, 2, 3])  # {1, 2, 3}
s = {x for x in range(5)}  # Set comprehension

# Operations
s.add(4)               # O(1) avg
s.remove(1)            # O(1), raises error if not found
s.discard(1)           # O(1), no error if not found
s.pop()                # Remove arbitrary
s1 & s2                # Intersection
s1 | s2                # Union
s1 - s2                # Difference
s1 ^ s2                # Symmetric difference
```

### Deque
```python
from collections import deque

d = deque([1, 2, 3])
d.append(4)            # Add right: O(1)
d.appendleft(0)        # Add left: O(1)
d.pop()                # Remove right: O(1)
d.popleft()            # Remove left: O(1)
```

## Collections Module

### Counter
```python
from collections import Counter

# Frequency counting
s = "mississippi"
Counter(s)  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Most common
Counter(s).most_common(2)  # [('i', 4), ('s', 4)]

# Dictionary-like operations
c = Counter(a=2, b=3)
c['a']  # 2
```

### defaultdict
```python
from collections import defaultdict

# Avoid KeyError
d = defaultdict(list)
d['a'].append(1)  # No error

# Grouping
d = defaultdict(list)
for word in words:
    d[len(word)].append(word)
```

### OrderedDict
```python
from collections import OrderedDict

# Maintains insertion order (Python 3.7+ dict does this by default)
d = OrderedDict()
d['first'] = 1
d['second'] = 2
```

## String Operations

### String Methods
```python
s = "hello world"

# Case
s.upper()              # "HELLO WORLD"
s.lower()              # "hello world"
s.capitalize()         # "Hello world"
s.title()              # "Hello World"

# Searching
s.find('o')            # 4 (first index)
s.rfind('o')           # 7 (last index)
s.index('o')           # 4 (raises error if not found)
s.count('l')           # 3

# Manipulation
s.replace('world', 'python')  # "hello python"
s.split()              # ['hello', 'world']
'-'.join(['a', 'b'])   # 'a-b'
s.strip()              # Remove whitespace
```

### String Formatting
```python
# f-strings (Python 3.6+)
name = "Alice"
f"Hello, {name}!"

# Format method
"Hello, {}!".format(name)

# Formatting options
f"{value:.2f}"         # 2 decimal places
f"{value:05d}"         # Pad with zeros
```

## List Comprehensions

```python
# Basic
[x*2 for x in range(5)]  # [0, 2, 4, 6, 8]

# With condition
[x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Nested
[[x for x in range(3)] for _ in range(3)]  # 2D list

# With enumeration
[(i, v) for i, v in enumerate(['a', 'b', 'c'])]
```

## Lambda Functions

```python
# Simple function
square = lambda x: x**2

# With sorting
sorted(arr, key=lambda x: x[1])
sorted(arr, key=lambda x: -x)  # Descending

# With map
list(map(lambda x: x*2, range(5)))

# With filter
list(filter(lambda x: x > 2, range(5)))
```

## Useful Functions

### max/min
```python
max([1, 5, 3])         # 5
max([1, 5, 3], key=lambda x: -x)  # Minimum instead
max('abc')             # 'c'

min(arr)
```

### sorted
```python
sorted([3, 1, 2])      # [1, 2, 3]
sorted([3, 1, 2], reverse=True)  # [3, 2, 1]
sorted(arr, key=lambda x: x[0])  # Sort by first element
```

### zip
```python
a = [1, 2, 3]
b = ['a', 'b', 'c']
list(zip(a, b))  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

### enumerate
```python
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)
```

## Slicing

```python
arr = [0, 1, 2, 3, 4, 5]

arr[1:4]               # [1, 2, 3]
arr[:3]                # [0, 1, 2]
arr[3:]                # [3, 4, 5]
arr[-1]                # 5 (last element)
arr[::2]               # [0, 2, 4] (every 2nd)
arr[::-1]              # [5, 4, 3, 2, 1, 0] (reverse)
```

## Performance Tips

### Avoid
```python
# Slow: list concatenation
result = []
for x in range(1000):
    result = result + [x]  # O(n²)

# Fast: append
result = []
for x in range(1000):
    result.append(x)  # O(1) amortized
```

### Use Sets for Membership
```python
# Slow: O(n)
if x in [1, 2, 3, 4, 5]:
    pass

# Fast: O(1)
if x in {1, 2, 3, 4, 5}:
    pass
```

### List vs Generator
```python
# Creates entire list in memory
[x*2 for x in range(1000000)]

# Generator: lazy evaluation
(x*2 for x in range(1000000))
```

## Debugging Tips

```python
# Print with variable name
x = 5
print(f"{x=}")  # x=5

# Assert
assert x > 0, "x must be positive"

# Breakpoint
breakpoint()  # Python 3.7+

# Type hints
def two_sum(nums: list, target: int) -> list:
    pass
```

## Common Patterns

### Iterate backwards
```python
for i in range(len(arr)-1, -1, -1):
    print(arr[i])

# Or
for item in reversed(arr):
    print(item)
```

### Two pointer pattern
```python
left, right = 0, len(arr) - 1
while left < right:
    # Process
    left += 1
    right -= 1
```

### Sliding window
```python
left = 0
for right in range(len(arr)):
    # Add arr[right]
    while condition:
        # Remove arr[left]
        left += 1
```

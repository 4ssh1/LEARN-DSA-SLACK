# Optimization Techniques Discussion

## Time Complexity Optimization

### 1. Reduce Operations
- Avoid nested loops when possible
- Use hash maps for O(1) lookups
- Replace linear search with binary search

**Example: Two Sum**
```python
# Naive: O(n²)
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]

# Optimized: O(n)
seen = {}
for i, num in enumerate(nums):
    if target - num in seen:
        return [seen[target - num], i]
    seen[num] = i
```

### 2. Use Appropriate Data Structures
- Arrays for random access: O(1)
- Hash tables for searching: O(1) avg
- Trees for sorted data: O(log n)
- Heaps for priority: O(log n)

### 3. Divide and Conquer
- Merge Sort vs Bubble Sort
- Binary Search vs Linear Search
- Reduces complexity from O(n²) to O(n log n)

### 4. Dynamic Programming
- Avoid recalculating subproblems
- Memoization: store computed results
- Tabulation: build up solutions

**Example: Fibonacci**
```python
# Naive: O(2^n)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# DP Memoization: O(n)
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

## Space Complexity Optimization

### 1. In-Place Algorithms
- Modify input array directly
- Swap elements instead of creating new arrays
- Reduces space from O(n) to O(1)

**Example: Reverse Array**
```python
# Extra space: O(n)
reversed_arr = arr[::-1]

# In-place: O(1)
left, right = 0, len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
```

### 2. Optimize Data Structures
- Use arrays instead of linked lists when possible
- Store only necessary information
- Compress data representation

### 3. Stream Processing
- Process data without loading everything
- Reduce memory footprint
- Useful for large datasets

## Pattern Recognition

### Sliding Window
- Converts O(n*m) to O(n)
- Maintain window of relevant elements
- Expand and contract as needed

### Two Pointers
- Converts O(n²) to O(n)
- Traverse from opposite ends
- Meet in the middle

### Hash Maps
- Converts O(n²) searching to O(n)
- Trade space for time
- Perfect for frequency counting

## Optimization Trade-offs

### Time vs Space
- Extra space for faster execution
- Cache results to avoid recomputation
- Choose based on constraints

### Readability vs Performance
- Simple solutions might be sufficient
- Optimize only bottlenecks
- Profile before optimizing

### Development Speed vs Execution Speed
- Quick solution first
- Optimize if needed
- Don't premature optimize

## Common Optimization Mistakes

### 1. Over-Engineering
- Don't optimize until you need to
- Profile to find real bottlenecks
- Start with clear solution

### 2. Wrong Data Structure
- Array vs Linked List
- Hash vs Tree
- Wrong choice adds overhead

### 3. Redundant Operations
- Check if computation needed
- Cache expensive results
- Reuse calculations

### 4. Ignoring Constants
- O(n) with large constant slower than O(n log n)
- Profile real performance
- Constants matter in practice

## Optimization Checklist

- [ ] Solution works correctly
- [ ] Identified bottlenecks
- [ ] Considered data structures
- [ ] Applied optimization patterns
- [ ] Profiled for improvement
- [ ] Trade-offs acceptable
- [ ] Code remains readable
- [ ] Tested edge cases

# Week 01: Array Basics

## Overview

Arrays are the fundamental data structure in computer science. This week covers array operations, traversal, searching, and classic array problems to build a strong foundation.

## Learning Objectives

- Understand array structure and memory layout
- Master basic array operations (access, insert, delete)
- Implement searching algorithms (linear, binary)
- Solve classic array manipulation problems
- Optimize solutions for time and space complexity

## Array Fundamentals

### What is an Array?
- Contiguous memory locations storing elements of same type
- Zero-indexed (in most languages)
- Fixed or dynamic size (depending on language)
- O(1) access time, O(n) insertion/deletion

### Basic Operations

#### Access
```python
arr = [1, 2, 3, 4, 5]
element = arr[0]  # O(1)
```

#### Insert
```python
# Insert at end: O(1)
arr.append(6)  # [1, 2, 3, 4, 5, 6]

# Insert at position: O(n)
arr.insert(2, 10)  # [1, 2, 10, 3, 4, 5, 6]
```

#### Delete
```python
# Remove by value: O(n)
arr.remove(10)  # [1, 2, 3, 4, 5, 6]

# Remove by index: O(n)
arr.pop(0)  # [2, 3, 4, 5, 6]
```

#### Search
```python
# Linear search: O(n)
if 3 in arr:
    index = arr.index(3)

# Binary search: O(log n) - requires sorted array
```

## Key Patterns

### Pattern 1: Two Sum
```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Pattern 2: Best Time to Buy and Sell Stock
```python
def maxProfit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    
    return max_profit
```

### Pattern 3: Contains Duplicate
```python
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
    # Or: use seen set with loop
```

## Time and Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Access | O(1) | O(1) |
| Search | O(n) or O(log n) | O(1) |
| Insertion | O(n) | O(1) |
| Deletion | O(n) | O(1) |

## Common Data Structures

### Sorted vs Unsorted
- Unsorted: O(1) insert, O(n) search
- Sorted: O(n) insert, O(log n) search

### Dynamic Arrays
- Automatically resize when full
- Amortized O(1) append
- Languages: Python list, Java ArrayList, C++ vector

## Problems

See [problems.md](problems.md) for this week's challenges.

## Resources

- [Complexity Cheatsheet](../../resources/complexity-cheatsheet.md)
- [Problem Solving Template](../../resources/problem-solving-template.md)
- [Solution Approaches](solutions/)
- [Community Solutions](community-solutions/)

## Tips

1. **Understand the constraint:** Is array sorted?
2. **Space-time trade-off:** Hash map for O(1) lookup
3. **In-place modification:** Minimize space usage
4. **Edge cases:** Empty array, single element, duplicates
5. **Test thoroughly:** Various sizes and values

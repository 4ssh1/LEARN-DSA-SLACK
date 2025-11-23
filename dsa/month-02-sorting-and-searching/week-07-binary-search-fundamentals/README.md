# Week 07: Binary Search Fundamentals

## Overview

Binary search is one of the most important algorithms in computer science. It efficiently searches sorted data in O(log n) time. This week covers the fundamentals and common patterns.

## Learning Objectives

- Understand binary search algorithm and its requirements
- Implement standard binary search correctly
- Analyze edge cases and boundary conditions
- Know when binary search is applicable
- Master left and right pointer updates

## Core Concept

Binary search divides the search space in half at each step:
- Compare target with middle element
- Eliminate half the remaining elements
- Repeat until found or search space empty

## Algorithm

```python
def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1      # Search right half
        else:
            right = mid - 1     # Search left half
    
    return -1  # Not found
```

## Key Points

### Prerequisites
- Array must be sorted
- Must have random access (arrays, not linked lists)

### Time Complexity
- O(log n) - each iteration eliminates half the elements
- Example: 1 million elements → ~20 iterations

### Space Complexity
- O(1) - iterative version (no extra space)
- O(log n) - recursive version (call stack)

## Variations

### Find First Occurrence
```python
def findFirst(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### Find Last Occurrence
```python
def findLast(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

## Common Mistakes

1. **Infinite loop:** Using `mid = (left + right) // 2` without proper updates
2. **Off-by-one:** Wrong boundary conditions (`left < right` vs `left <= right`)
3. **Overflow:** Very large sums (use `mid = left + (right - left) // 2`)
4. **Unsorted data:** Binary search requires sorted input
5. **Duplicate handling:** Need special logic for duplicates

## Problems

See [problems.md](problems.md) for this week's challenges.

## Resources

- [Binary Search Template](../../templates/binary-search-template.md)
- [Complexity Cheatsheet](../../resources/complexity-cheatsheet.md)
- [Solution Approaches](solutions/)
- [Community Solutions](community-solutions/)

## Tips

1. **Verify sorted:** Always check if input is sorted
2. **Use template:** Follow the standard pattern
3. **Avoid overflow:** Use `mid = left + (right - left) // 2`
4. **Test boundaries:** Test with first, last, and middle elements
5. **Edge cases:** Empty array, single element, target not found

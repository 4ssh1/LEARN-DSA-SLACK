# Week 08: Binary Search Variations

## Overview

This week covers advanced binary search techniques and variations that handle special cases like rotated arrays, search with duplicates, and finding boundaries in complex scenarios.

## Learning Objectives

- Apply binary search to rotated arrays
- Handle duplicate elements in binary search
- Find peak elements and boundaries
- Solve complex search problems
- Master edge case handling

## Variations

### 1. Search in Rotated Sorted Array

**Concept:** Array is sorted but rotated at a pivot point.

```python
def searchRotated(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Determine which side is sorted
        if nums[left] <= nums[mid]:
            # Left side is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right side is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

---

### 2. Search in Rotated Array with Duplicates

**Concept:** Similar to rotated array but with duplicate elements.

```python
def searchRotatedWithDuplicates(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return True
        
        # Handle duplicates - shrink boundaries
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return False
```

---

### 3. Find Peak Element

**Concept:** Find an element greater than its neighbors.

```python
def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] < nums[mid + 1]:
            left = mid + 1  # Peak is on right
        else:
            right = mid     # Peak is on left or mid
    
    return left
```

---

### 4. Find Minimum in Rotated Sorted Array

**Concept:** Find minimum element in rotated sorted array.

```python
def findMin(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1      # Min is on right
        else:
            right = mid         # Min is on left or mid
    
    return nums[left]
```

---

### 5. Find Minimum with Duplicates

**Concept:** Find minimum in rotated array with duplicates.

```python
def findMinWithDuplicates(nums):
    left, right = len(nums) - 1
    
    while left > 0 and nums[left] == nums[left - 1]:
        right -= 1
    
    while left > 0 and nums[0] == nums[left]:
        left -= 1
    
    if nums[0] <= nums[left]:
        return nums[0]
    
    # Standard binary search on rotated
    left = 0
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]
```

## Key Patterns

| Problem | Key Insight |
|---------|------------|
| Rotated Array | Identify sorted half first |
| Duplicates | Shrink boundaries when equal |
| Peak Element | Compare with neighbor |
| Minimum | Look for transition point |

## Complexity Analysis

- **Time:** O(log n) for most, O(n) worst case with many duplicates
- **Space:** O(1)

## Problems

See [problems.md](problems.md) for this week's challenges.

## Resources

- [Binary Search Template](../../templates/binary-search-template.md)
- [Complexity Cheatsheet](../../resources/complexity-cheatsheet.md)
- [Solution Approaches](solutions/)
- [Community Solutions](community-solutions/)

## Tips

1. **Identify the pattern:** What makes this array special?
2. **Determine sorted half:** Always know which side is sorted
3. **Handle duplicates carefully:** Extra conditions needed
4. **Trace examples:** Work through rotated arrays step by step
5. **Edge cases:** Single element, all duplicates, no rotation

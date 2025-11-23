# Binary Search Template

A template for implementing binary search and its variations on sorted arrays.

## Core Concept

Binary search divides the search space in half at each step, achieving O(log n) time complexity. Only works on sorted data.

## Pattern 1: Standard Binary Search

### Template

```python
def binarySearch(arr, target):
    """Find target in sorted array, return index or -1"""
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

### Key Points
- **Termination:** `while left <= right`
- **Mid calculation:** `mid = (left + right) // 2` or `mid = left + (right - left) // 2` (avoids overflow)
- **Update:** `left = mid + 1` or `right = mid - 1` (don't use `mid`)

### Time & Space
- **Time:** O(log n)
- **Space:** O(1)

---

## Pattern 2: Left Boundary (First Occurrence)

### Template

```python
def findFirst(arr, target):
    """Find first occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1      # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### When to Use
- Find first element >= target
- Find first occurrence of element
- Find start of range

### Example: Find First Bad Version

```python
def firstBadVersion(n):
    """Find first bad version"""
    left, right = 1, n
    
    while left < right:
        mid = (left + right) // 2
        
        if isBadVersion(mid):
            right = mid        # Could be the answer
        else:
            left = mid + 1     # Bad is further right
    
    return left
```

---

## Pattern 3: Right Boundary (Last Occurrence)

### Template

```python
def findLast(arr, target):
    """Find last occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1      # Keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### When to Use
- Find last element <= target
- Find last occurrence of element
- Find end of range

---

## Pattern 4: Insert Position

### Template

```python
def searchInsert(arr, target):
    """Find position to insert target in sorted array"""
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left
```

### When to Use
- Find insert position for new element
- Find closest element
- Find range

---

## Common Variations

### 1. Search in Rotated Sorted Array
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

### 2. Find Peak Element
```python
def findPeak(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] < nums[mid + 1]:
            left = mid + 1      # Peak is on right
        else:
            right = mid         # Peak is on left or mid
    
    return left
```

### 3. Find Min in Rotated Array
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

### 4. Sqrt(x)
```python
def mySqrt(x):
    if x < 2:
        return x
    
    left, right = 2, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # Return floor of sqrt
```

---

## Debugging Checklist

- [ ] Is the array sorted?
- [ ] What should be returned when target not found?
- [ ] Are boundaries inclusive/exclusive?
- [ ] Is mid calculation correct?
- [ ] Are left/right updates correct?
- [ ] What are edge cases? (empty, single element, duplicates)

## Tips

1. **Avoid overflow:** Use `mid = left + (right - left) // 2`
2. **Think boundaries:** Know if searching inclusive or exclusive
3. **Test off-by-one:** Verify boundary conditions
4. **Duplicates:** Handle carefully, may need linear scan fallback
5. **Practice:** Visualize the search space shrinking

# Week 03: Sliding Window

## Overview

The sliding window technique is an efficient approach for solving substring, subarray, and range problems. It maintains a contiguous window of elements and slides it across the data structure to achieve optimal time complexity.

## Learning Objectives

- Understand fixed-size and variable-size sliding windows
- Identify problems suitable for sliding window approach
- Implement sliding window patterns efficiently
- Optimize solutions from O(n²) to O(n)
- Handle edge cases and boundary conditions

## Concepts

### Fixed-Size Window
- Window size remains constant
- Slide through the array, removing left element and adding right element
- Useful for finding max/min of subarrays

### Variable-Size Window
- Window size changes based on conditions
- Expand right boundary to include elements
- Shrink left boundary when condition is violated

### Two-Pointer Window
- Left and right pointers move based on different conditions
- Often combined with hash maps for character tracking

## Key Patterns

### Pattern 1: Maximum Sum of K Elements
```python
def maxSumSubarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Pattern 2: Longest Without Repeating
```python
def longestWithoutRepeating(s):
    char_index = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### Pattern 3: Minimum Window
```python
def minWindow(s, t):
    from collections import Counter
    
    char_count = Counter(t)
    required = len(char_count)
    
    left = 0
    formed = 0
    window_counts = {}
    result = float("inf"), None, None
    
    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in char_count and window_counts[char] == char_count[char]:
            formed += 1
        
        while left <= right and formed == required:
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            
            window_counts[s[left]] -= 1
            if s[left] in char_count and window_counts[s[left]] < char_count[s[left]]:
                formed -= 1
            left += 1
    
    return "" if result[0] == float("inf") else s[result[1]:result[2] + 1]
```

## Time and Space Complexity

- **Time:** O(n) - each element visited at most twice
- **Space:** O(m) - where m is size of character set or unique elements

## Problems

See [problems.md](problems.md) for this week's challenges.

## Resources

- [Sliding Window Template](../../templates/sliding-window-template.md)
- [Solution Approaches](solutions/)
- [Community Solutions](community-solutions/)
- [Explanations](explanations/)

## Tips

1. **Identify the window:** What defines a valid window?
2. **Expand right:** Add elements until condition met
3. **Shrink left:** Remove elements when window becomes invalid
4. **Track state:** Use hash map or counter for character frequency
5. **Edge cases:** Empty string, all same characters, no valid window

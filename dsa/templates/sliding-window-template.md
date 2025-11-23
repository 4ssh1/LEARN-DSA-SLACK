# Sliding Window Template

A template for implementing the sliding window technique to solve substring, subarray, and range problems.

## Core Concept

A sliding window is a fixed-size or variable-size window that slides through a data structure (usually an array or string) to solve problems efficiently in O(n) time.

## Pattern 1: Fixed-Size Sliding Window

### Template

```python
def fixedWindowSize(arr, k):
    """Find maximum sum of k consecutive elements"""
    if len(arr) < k:
        return None
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        # Remove leftmost element and add new rightmost
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### When to Use
- Maximum sum of k elements
- Average of contiguous subarrays
- Maximum consecutive ones
- Repeating character replacement

### Example: Maximum Average Subarray

```python
def findMaxAverage(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum / k
```

---

## Pattern 2: Variable-Size Sliding Window

### Template

```python
def variableWindowSize(s, chars):
    """Find shortest substring containing all unique chars"""
    if not s:
        return ""
    
    char_count = {}
    left = 0
    result = ""
    min_len = float('inf')
    
    for right in range(len(s)):
        # Add character to window
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Shrink window from left
        while is_valid(char_count, chars):
            # Update result
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
            
            # Remove leftmost character
            char_count[s[left]] -= 1
            left += 1
    
    return result
```

### When to Use
- Minimum window substring
- Longest substring without repeating characters
- Longest substring with at most k distinct characters
- Longest subarray with target sum

---

## Pattern 3: Two Pointers Sliding Window

### Template

```python
def twoPointerWindow(arr):
    """Two pointers expanding/contracting window"""
    left = 0
    result = 0
    
    for right in range(len(arr)):
        # Expand window with right pointer
        
        # Contract window with left pointer while condition
        while condition:
            left += 1
        
        # Process current window
        result = max(result, right - left + 1)
    
    return result
```

### Example: Longest Substring Without Repeating Characters

```python
def lengthOfLongestSubstring(s):
    char_index = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        if s[right] in char_index:
            # Move left pointer past previous occurrence
            left = max(left, char_index[s[right]] + 1)
        
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

---

## Common Window Problems

### 1. Maximum Sum of K Elements
```python
# Fixed window - see Pattern 1
```

### 2. Minimum Window Substring
```python
def minWindow(s, t):
    from collections import Counter
    
    if not s or not t:
        return ""
    
    dict_t = Counter(t)
    required = len(dict_t)
    
    left = 0
    formed = 0
    window_counts = {}
    result = float("inf"), None, None
    
    for right in range(len(s)):
        character = s[right]
        window_counts[character] = window_counts.get(character, 0) + 1
        
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        
        while left <= right and formed == required:
            character = s[left]
            
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            
            left += 1
    
    return "" if result[0] == float("inf") else s[result[1]:result[2] + 1]
```

### 3. Longest Repeating Character Replacement
```python
def characterReplacement(s, k):
    char_count = {}
    left = 0
    max_length = 0
    max_char_count = 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_char_count = max(max_char_count, char_count[s[right]])
        
        # If window size - max frequent char > k, shrink
        while right - left + 1 - max_char_count > k:
            char_count[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

---

## Complexity Analysis

- **Time:** O(n) - each element visited at most twice (left and right pointers)
- **Space:** O(m) - where m is the size of character set or unique elements

## Key Tips

1. **Initialization:** Set up left = 0, right = 0 initially
2. **Expansion:** Always expand with right pointer
3. **Contraction:** Shrink with left pointer when needed
4. **Update:** Process result at each step
5. **Edge Cases:** Handle empty input, single character, all duplicates

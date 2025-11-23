# Two Pointers Template

A template for implementing two-pointer techniques to solve array and string problems.

## Pattern 1: Two Pointers from Both Ends

### Concept
Start with pointers at the beginning and end of an array/string, then move them towards each other based on conditions.

### Template

```python
def twoPointersBothEnds(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Process current elements
        if condition(arr[left], arr[right]):
            # Move based on logic
            left += 1
        else:
            right -= 1
    
    return result
```

### When to Use
- Finding pairs with specific sum
- Validating palindromes
- Container problems
- Reverse operations

### Example: Valid Palindrome

```python
def isValidPalindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        
        # Compare characters
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
```

---

## Pattern 2: Slow and Fast Pointers

### Concept
One pointer moves slower than the other, useful for cycle detection and finding specific positions.

### Template

```python
def slowFastPointers(arr):
    slow = 0
    fast = 0
    
    while fast < len(arr) and fast + 1 < len(arr):
        # Move pointers
        slow += 1
        fast += 2  # or other increment
        
        # Check condition
        if condition(slow, fast):
            return result
    
    return result
```

### When to Use
- Detecting cycles in linked lists
- Finding middle element
- Remove duplicates
- Finding Kth element from end

### Example: Remove Duplicates

```python
def removeDuplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    
    j = 0  # pointer for next unique element
    
    for i in range(1, len(nums)):  # i is the fast pointer
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    
    return j + 1
```

---

## Pattern 3: Same Direction Pointers

### Concept
Both pointers move in the same direction but at different speeds or positions.

### Template

```python
def sameDirectionPointers(arr):
    i = 0
    j = 1
    
    while j < len(arr):
        if condition(arr[i], arr[j]):
            # Do something
            pass
        
        i += 1
        j += 1
    
    return result
```

### When to Use
- Comparing adjacent elements
- Sliding over array
- Partition operations

---

## Common Patterns & Tricks

### 1. Finding a Pair with Target Sum
```python
def findPair(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None
```

### 2. Reverse an Array
```python
def reverse(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

### 3. Check Palindrome
```python
def isPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

---

## Complexity Analysis

- **Time:** O(n) - typically linear since each element visited once
- **Space:** O(1) - constant space, no extra data structures

## Tips

1. Sort the array if needed for comparison
2. Consider edge cases: empty, single element, duplicates
3. Use meaningful variable names (left/right, slow/fast, i/j)
4. Make sure pointers actually move towards the goal
5. Validate termination conditions

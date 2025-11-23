# Week 04: String Manipulation

## Overview

String manipulation is a fundamental skill in programming and interviews. This week covers various techniques for efficiently processing and transforming strings, including pattern matching, encoding/decoding, and string transformations.

## Learning Objectives

- Master common string operations and methods
- Implement string searching algorithms
- Handle edge cases in string problems
- Optimize string manipulation solutions
- Apply previous techniques (two pointers, sliding window) to strings

## Key Concepts

### String Basics
- Strings are immutable in most languages (Python, Java)
- Character access: O(1), string concatenation: O(n)
- Common methods: split, join, replace, find, substring

### Pattern Matching
- Brute force: O(n*m)
- KMP algorithm: O(n+m)
- Rabin-Karp: O(n+m) average

### String Encoding/Decoding
- URL encoding, Base64, hex encoding
- Compress/decompress strings
- Encode/decode patterns

### String Transformations
- Anagrams
- Palindromes
- Case conversions
- Reversals

## Common Patterns

### Pattern 1: Palindrome Check
```python
def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
```

### Pattern 2: Anagram Check
```python
def isAnagram(s, t):
    return sorted(s) == sorted(t)
    # Or: from collections import Counter
    # return Counter(s) == Counter(t)
```

### Pattern 3: Group Anagrams
```python
def groupAnagrams(strs):
    from collections import defaultdict
    groups = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())
```

### Pattern 4: Longest Common Prefix
```python
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    
    return strs[0]
```

### Pattern 5: String Compression
```python
def compress(chars):
    """Compress string in-place"""
    write = 0
    i = 0
    
    while i < len(chars):
        char = chars[i]
        count = 0
        
        while i < len(chars) and chars[i] == char:
            count += 1
            i += 1
        
        chars[write] = char
        write += 1
        
        if count > 1:
            count_str = str(count)
            for c in count_str:
                chars[write] = c
                write += 1
    
    return write
```

## Time and Space Complexity

- **String operations:**
  - Concatenation: O(n)
  - Slicing: O(n)
  - Searching: O(n*m) naive, O(n+m) with KMP
  - Sorting: O(n log n)

- **Space:** O(1) to O(n) depending on operations

## Problems

See [problems.md](problems.md) for this week's challenges.

## Resources

- [Complexity Cheatsheet](../../resources/complexity-cheatsheet.md)
- [Two Pointers Template](../../templates/two-pointers-template.md)
- [Solution Approaches](solutions/)
- [Community Solutions](community-solutions/)
- [Explanations](explanations/)

## Tips

1. **Use built-in functions:** sorted(), reversed(), count()
2. **String immutability:** Work with lists or builders when modifying
3. **Character frequency:** Use Counter or dictionary
4. **Optimization:** Consider sorting or hashing
5. **Edge cases:** Empty strings, single characters, duplicates

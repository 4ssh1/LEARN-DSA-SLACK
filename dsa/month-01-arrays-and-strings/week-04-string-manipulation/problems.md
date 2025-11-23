# Week 04: String Manipulation - Problems

## Problem Set

### Problem 1: Valid Anagram
**Difficulty:** Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

**Example:**
```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Constraints:**
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters

---

### Problem 2: Group Anagrams
**Difficulty:** Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

**Example:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Constraints:**
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters

---

### Problem 3: Longest Common Prefix
**Difficulty:** Easy

Write a function to find the longest common prefix string amongst an array of strings.

**Example:**
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

**Constraints:**
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters

---

### Problem 4: Reverse String
**Difficulty:** Easy

Write a function that reverses a string. The input string is given as an array of characters s.

**Example:**
```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Constraints:**
- 1 <= s.length <= 10^5
- s[i] is a printable ascii character

---

### Problem 5: String Compression
**Difficulty:** Medium

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive duplicate characters in chars:
- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

**Example:**
```
Input: chars = ["a","a","b","b","c","c","c"]
Output: 6, and chars is modified to ["a","2","b","2","c","3"]
```

**Constraints:**
- 1 <= chars.length <= 2000
- chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol

---

### Problem 6: Isomorphic Strings
**Difficulty:** Easy

Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.

**Example:**
```
Input: s = "egg", t = "add"
Output: true
Explanation: The occurrences of "e", "g", and "d" in "egg" map to "a", "d", and "d" respectively.
```

**Constraints:**
- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s and t consist of any valid ascii character

## Submission Guidelines

1. Choose at least 3 problems to solve
2. Implement in your preferred language
3. Place solution in the appropriate `solutions/[language]/` folder
4. Include time and space complexity analysis
5. Test with provided examples and edge cases
6. Consider multiple approaches and trade-offs

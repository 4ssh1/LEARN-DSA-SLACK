# Week 03: Sliding Window - Problems

## Problem Set

### Problem 1: Longest Substring Without Repeating Characters
**Difficulty:** Medium

Given a string s, find the length of the longest substring without repeating characters.

**Example:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Constraints:**
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces

---

### Problem 2: Minimum Window Substring
**Difficulty:** Hard

Given two strings s and t, return the minimum window in s which will contain all the characters in t.

**Example:**
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window is "BANC".
```

**Constraints:**
- 1 <= s.length, t.length <= 10^5
- s and t consist of English letters

---

### Problem 3: Longest Repeating Character Replacement
**Difficulty:** Medium

Given a string s and an integer k, you can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times. Return the length of the longest substring containing the same letter you can get after performing the above operations.

**Example:**
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

**Constraints:**
- 1 <= s.length <= 10^5
- s consists of only uppercase English characters
- 0 <= k <= s.length

---

### Problem 4: Permutation in String
**Difficulty:** Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

**Example:**
```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Constraints:**
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters

---

### Problem 5: Fruits Into Baskets
**Difficulty:** Medium

You are visiting a farm that has unlimited number of two types of fruits represented by characters 'A' and 'B' respectively. The same type of fruit will always appear consecutively, and the farm is represented by an array fruits where fruits[i] is the type of fruit you encounter as you visit the farm from left to right. You want to put as many fruits as possible into your two baskets such that each basket is full before moving on. However, you can only put the same type of fruit into each basket. You start with any index of your choice and you can rearrange the fruits in any order.

**Example:**
```
Input: fruits = [1,2,1]
Output: 3
Explanation: You can pick from all 3 trees.
```

**Constraints:**
- 1 <= fruits.length <= 10^5
- fruits[i] is 1 or 2

---

### Problem 6: Max Consecutive Ones III
**Difficulty:** Medium

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

**Example:**
```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1,1] - Flip the first two 0s.
```

**Constraints:**
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
- 0 <= k <= nums.length

## Submission Guidelines

1. Choose at least 3 problems to solve
2. Implement in your preferred language
3. Place solution in the appropriate `solutions/[language]/` folder
4. Include time and space complexity analysis
5. Test with provided examples and edge cases
6. Explain your sliding window approach

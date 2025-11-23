# C++ Tips for DSA

## STL Containers

### Vector (Dynamic Array)
```cpp
#include <vector>

vector<int> v;
v.push_back(1);             // Add to end: O(1) amortized
v.pop_back();               // Remove from end: O(1)
v[0];                       // Access: O(1)
v.at(0);                    // Safe access with bounds check
v.size();                   // Get size
v.clear();                  // Remove all
v.empty();                  // Check if empty
v.resize(5);                // Change size
v.reserve(10);              // Preallocate capacity

// Initialization
vector<int> v1(5, 0);       // 5 zeros
vector<int> v2 = {1, 2, 3}; // Initialize with values
vector<vector<int>> matrix(5, vector<int>(3, 0));  // 2D
```

### Map (Ordered, Red-Black Tree)
```cpp
#include <map>

map<int, int> m;
m[5] = 10;                  // Insert/access: O(log n)
m.insert({5, 10});          // Alternative insert
m.erase(5);                 // Remove: O(log n)
m.find(5);                  // Find: O(log n)
m.count(5);                 // Check existence: O(log n)
m.size();                   // Get size
m.clear();                  // Remove all

// Iteration
for (auto& [key, val] : m) {
    cout << key << " " << val << endl;
}
```

### Unordered_map (Hash Map)
```cpp
#include <unordered_map>

unordered_map<int, int> m;
m[5] = 10;                  // Insert/access: O(1) average
m.erase(5);                 // Remove: O(1) average
m.find(5);                  // Find: O(1) average
m.count(5);                 // Check: O(1) average

// Better for DSA (usually)
// Average case much faster than map
```

### Set (Unique, Ordered)
```cpp
#include <set>

set<int> s;
s.insert(5);                // Insert: O(log n)
s.erase(5);                 // Remove: O(log n)
s.find(5);                  // Find: O(log n)
s.count(5);                 // Check: O(log n)
s.size();                   // Get size
s.empty();                  // Check if empty

// Iteration (sorted order)
for (int val : s) {
    cout << val << endl;
}
```

### Unordered_set (Hash Set)
```cpp
#include <unordered_set>

unordered_set<int> s;
s.insert(5);                // Insert: O(1) average
s.erase(5);                 // Remove: O(1) average
s.find(5);                  // Find: O(1) average
s.count(5);                 // Check: O(1) average
```

### Queue & Stack
```cpp
#include <queue>
#include <stack>

// Queue (FIFO)
queue<int> q;
q.push(1);                  // Add to back: O(1)
q.front();                  // Get front: O(1)
q.pop();                    // Remove front: O(1)
q.empty();                  // Check if empty
q.size();                   // Get size

// Stack (LIFO)
stack<int> s;
s.push(1);                  // Add to top: O(1)
s.top();                    // Get top: O(1)
s.pop();                    // Remove top: O(1)
s.empty();                  // Check if empty
s.size();                   // Get size
```

### Priority Queue
```cpp
#include <queue>

// Max heap (default)
priority_queue<int> pq;
pq.push(5);                 // Add: O(log n)
pq.top();                   // Get max: O(1)
pq.pop();                   // Remove max: O(log n)

// Min heap
priority_queue<int, vector<int>, greater<int>> minPq;
minPq.push(5);              // Add: O(log n)
minPq.top();                // Get min: O(1)
minPq.pop();                // Remove min: O(log n)
```

### Deque (Double-ended Queue)
```cpp
#include <deque>

deque<int> d;
d.push_back(1);             // Add to back: O(1)
d.push_front(0);            // Add to front: O(1)
d.pop_back();               // Remove from back: O(1)
d.pop_front();              // Remove from front: O(1)
d[0];                       // Access: O(1)
```

## Algorithms

### Sorting
```cpp
#include <algorithm>

vector<int> arr = {3, 1, 4, 1, 5};

// Sort ascending
sort(arr.begin(), arr.end());

// Sort descending
sort(arr.begin(), arr.end(), greater<int>());

// Custom comparator
sort(arr.begin(), arr.end(), [](int a, int b) {
    return a > b;  // Descending
});

// Sort objects
struct Person {
    int age;
    string name;
};

vector<Person> people;
sort(people.begin(), people.end(), [](const Person& a, const Person& b) {
    return a.age < b.age;
});
```

### Search
```cpp
#include <algorithm>

// Binary search (requires sorted array)
vector<int> arr = {1, 2, 3, 4, 5};
binary_search(arr.begin(), arr.end(), 3);  // true

// Find first occurrence
auto it = lower_bound(arr.begin(), arr.end(), 3);  // Iterator to 3

// Find first greater
auto it = upper_bound(arr.begin(), arr.end(), 3);  // Iterator to 4

// Find element
auto it = find(arr.begin(), arr.end(), 3);  // Iterator to 3
if (it != arr.end()) { }  // Found
```

### Other Common
```cpp
#include <algorithm>

// Count
int count = count(arr.begin(), arr.end(), 3);

// Count if
int count = count_if(arr.begin(), arr.end(), [](int x) {
    return x > 2;
});

// Reverse
reverse(arr.begin(), arr.end());

// Min/Max
int minVal = *min_element(arr.begin(), arr.end());
int maxVal = *max_element(arr.begin(), arr.end());

// Fill
fill(arr.begin(), arr.end(), 0);

// Accumulate (sum)
#include <numeric>
int sum = accumulate(arr.begin(), arr.end(), 0);
```

## String Operations

```cpp
#include <string>

string s = "hello";

// Access
s[0];                       // 'h'
s.at(0);                    // Safe access
s.length();                 // 5
s.size();                   // 5
s.empty();                  // false

// Modification
s += "world";               // Concatenate
s.append(" world");         // Append
s.insert(5, " ");           // Insert at position
s.erase(5, 1);              // Erase 1 char at pos 5
s.replace(0, 5, "bye");     // Replace

// Search
s.find("llo");              // Position of substring
s.find('l');                // Position of character
s.substr(0, 3);             // Get substring

// Case
transform(s.begin(), s.end(), s.begin(), ::toupper);     // Uppercase
transform(s.begin(), s.end(), s.begin(), ::tolower);     // Lowercase

// Compare
s.compare("hello");         // 0 if equal
s == "hello";               // true
```

## Useful Patterns

### Two Pointer
```cpp
vector<int> arr = {1, 2, 3, 4, 5};
int left = 0, right = arr.size() - 1;

while (left < right) {
    if (arr[left] + arr[right] == target) {
        return {left, right};
    } else if (arr[left] + arr[right] < target) {
        left++;
    } else {
        right--;
    }
}
```

### Sliding Window
```cpp
int maxLen = 0;
unordered_map<int, int> charCount;

int left = 0;
for (int right = 0; right < s.length(); right++) {
    charCount[s[right]]++;
    
    while (charCount.size() > k) {
        charCount[s[left]]--;
        if (charCount[s[left]] == 0) {
            charCount.erase(s[left]);
        }
        left++;
    }
    
    maxLen = max(maxLen, right - left + 1);
}
```

### DFS
```cpp
void dfs(TreeNode* node, int targetSum, int current, vector<int>& path) {
    if (!node) return;
    
    path.push_back(node->val);
    current += node->val;
    
    if (!node->left && !node->right && current == targetSum) {
        result.push_back(path);
    } else {
        dfs(node->left, targetSum, current, path);
        dfs(node->right, targetSum, current, path);
    }
    
    path.pop_back();
}
```

### BFS
```cpp
#include <queue>

queue<TreeNode*> q;
q.push(root);

while (!q.empty()) {
    int size = q.size();
    
    for (int i = 0; i < size; i++) {
        TreeNode* node = q.front();
        q.pop();
        
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
    }
}
```

## Lambda Functions

```cpp
// Basic
[](int x) { return x * 2; }

// Capture by value
int multiplier = 2;
auto fn = [multiplier](int x) { return x * multiplier; };

// Capture all by value
auto fn = [=](int x) { return x * multiplier; };

// Capture all by reference
auto fn = [&](int x) { return x * multiplier; };

// Use in sort
sort(arr.begin(), arr.end(), [](int a, int b) {
    return a > b;  // Descending
});

// Use in find_if
auto it = find_if(arr.begin(), arr.end(), [](int x) {
    return x > 5;
});
```

## Performance Tips

### Reserve Space
```cpp
// Bad: vector grows dynamically
vector<int> v;
for (int i = 0; i < 1000000; i++) {
    v.push_back(i);  // Reallocates many times
}

// Good: preallocate
vector<int> v;
v.reserve(1000000);
for (int i = 0; i < 1000000; i++) {
    v.push_back(i);  // No reallocation
}
```

### Use Appropriate Container
```cpp
// Frequent lookups: unordered_map (O(1)) > map (O(log n))
// Insertion/deletion at start: deque > vector
// Frequent insertion/deletion: list (but slow random access)
// Unique elements: set/unordered_set
```

### Pass by Reference
```cpp
// Bad: copy
void process(vector<int> arr) { }

// Good: reference
void process(const vector<int>& arr) { }
void process(vector<int>& arr) { }
```

## Common Mistakes

```cpp
// Mistake: Comparison issue
if (a = b) { }              // Assignment, not comparison!
if (a == b) { }             // Correct

// Mistake: Off-by-one
for (int i = 0; i <= n; i++) {  // Usually should be i < n
}

// Mistake: Uninitialized pointer
int* ptr;                   // Uninitialized!
*ptr = 5;                   // Crash!
int* ptr = nullptr;         // Better

// Mistake: Wrong operator precedence
if (a && b || c) { }        // && has higher precedence
```

## Useful Headers

```cpp
#include <vector>           // Dynamic array
#include <map>              // Ordered map
#include <unordered_map>    // Hash map
#include <set>              // Ordered set
#include <unordered_set>    // Hash set
#include <queue>            // Queue/Priority queue
#include <stack>            // Stack
#include <deque>            // Double-ended queue
#include <algorithm>        // Sort, find, etc.
#include <numeric>          // Accumulate, etc.
#include <string>           // String operations
#include <cmath>            // Math functions
#include <iostream>         // I/O
#include <cassert>          // Assertions
```

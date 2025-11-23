# DFS/BFS Template

Templates for implementing Depth-First Search (DFS) and Breadth-First Search (BFS) for graph and tree problems.

## DFS: Depth-First Search

### Pattern 1: Recursive DFS

#### Template

```python
def dfs_recursive(node, visited):
    """Recursive DFS traversal"""
    if node in visited:
        return
    
    visited.add(node)
    process(node)  # Do something with node
    
    for neighbor in node.neighbors:
        dfs_recursive(neighbor, visited)
```

#### Example: Clone Graph

```python
def cloneGraph(node):
    if not node:
        return None
    
    visited = {}
    
    def dfs(node):
        if node in visited:
            return visited[node]
        
        # Create clone of current node
        clone = Node(node.val)
        visited[node] = clone
        
        # Process neighbors
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)
```

### Pattern 2: Iterative DFS with Stack

#### Template

```python
def dfs_iterative(start):
    """Iterative DFS using stack"""
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        
        if node in visited:
            continue
        
        visited.add(node)
        result.append(node.val)
        
        # Add neighbors to stack (reverse order for correct traversal)
        for neighbor in reversed(node.neighbors):
            if neighbor not in visited:
                stack.append(neighbor)
    
    return result
```

### Pattern 3: DFS with Backtracking

#### Template

```python
def dfs_backtrack(path, remaining):
    """DFS with backtracking"""
    # Base case: solution found
    if not remaining:
        result.append(path[:])
        return
    
    for i in range(len(remaining)):
        # Choose
        path.append(remaining[i])
        new_remaining = remaining[:i] + remaining[i+1:]
        
        # Explore
        dfs_backtrack(path, new_remaining)
        
        # Unchoose
        path.pop()
```

#### Example: Permutations

```python
def permute(nums):
    result = []
    
    def dfs(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for num in nums:
            if num not in path:
                path.append(num)
                dfs(path)
                path.pop()
    
    dfs([])
    return result
```

### DFS Complexity
- **Time:** O(V + E) where V is vertices, E is edges
- **Space:** O(V) for recursion stack or visited set

---

## BFS: Breadth-First Search

### Pattern 1: Standard BFS with Queue

#### Template

```python
from collections import deque

def bfs(start):
    """Standard BFS traversal"""
    visited = {start}
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
```

#### Example: Level Order Traversal

```python
def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result
```

### Pattern 2: BFS for Shortest Path

#### Template

```python
def bfs_shortest_path(start, end, graph):
    """Find shortest path using BFS"""
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        node, path = queue.popleft()
        
        if node == end:
            return path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None
```

#### Example: Shortest Path in Grid

```python
def shortestPath(grid, start, end):
    from collections import deque
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = {start}
    queue = deque([(start, 0)])
    
    while queue:
        (x, y), dist = queue.popleft()
        
        if (x, y) == end:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and
                (nx, ny) not in visited and grid[nx][ny] == 0):
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))
    
    return -1
```

### BFS Complexity
- **Time:** O(V + E) where V is vertices, E is edges
- **Space:** O(V) for queue and visited set

---

## Common Problems

### 1. Number of Islands (DFS)
```python
def numIslands(grid):
    if not grid:
        return 0
    
    count = 0
    
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'  # Mark as visited
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    
    return count
```

### 2. Word Ladder (BFS)
```python
def ladderLength(beginWord, endWord, wordList):
    from collections import deque, defaultdict
    
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    
    neighbors = defaultdict(list)
    
    for word in wordList + [beginWord]:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            neighbors[pattern].append(word)
    
    queue = deque([(beginWord, 1)])
    visited = {beginWord}
    
    while queue:
        word, length = queue.popleft()
        
        if word == endWord:
            return length
        
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            for neighbor in neighbors[pattern]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, length + 1))
    
    return 0
```

### 3. Combination Sum (Backtracking)
```python
def combinationSum(candidates, target):
    result = []
    
    def dfs(path, start, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            dfs(path, i, remaining - candidates[i])
            path.pop()
    
    dfs([], 0, target)
    return result
```

---

## DFS vs BFS

| Aspect | DFS | BFS |
|--------|-----|-----|
| Data Structure | Stack | Queue |
| Implementation | Recursive/Iterative | Iterative |
| Space | O(h) - height for recursion | O(w) - width of level |
| Best For | All paths, cycles, connectivity | Shortest path, level order |
| Memory | Often less for deep graphs | More for wide graphs |

## Tips

1. **DFS:** Use for finding all solutions, detecting cycles
2. **BFS:** Use for shortest path, level-by-level traversal
3. **Backtracking:** DFS variant for exploring all possibilities
4. **Mark visited:** Avoid infinite loops in cycles
5. **Time limits:** Be aware of exponential backtracking time

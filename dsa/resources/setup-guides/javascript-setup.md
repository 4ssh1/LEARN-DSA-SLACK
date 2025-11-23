# JavaScript Setup Guide

## Node.js Installation

### Windows

1. **Download Node.js**
   - Visit [nodejs.org](https://nodejs.org/)
   - Download LTS version
   - Run installer

2. **Verify Installation**
   ```bash
   node --version
   npm --version
   ```

### macOS

```bash
# Using Homebrew
brew install node

# Verify
node --version
npm --version
```

### Linux (Ubuntu/Debian)

```bash
# Using apt
sudo apt update
sudo apt install nodejs npm

# Or use nvm (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install node
```

## Project Setup

### Initialize Project

```bash
# Create directory
mkdir dsa-practice
cd dsa-practice

# Initialize npm
npm init -y

# Or with specific name
npm init --name=dsa-practice
```

### Create Project Structure

```
dsa-practice/
├── node_modules/
├── src/
│   ├── week01/
│   │   ├── twoSum.js
│   │   └── bestTime.js
│   └── week02/
├── tests/
│   ├── week01.test.js
│   └── week02.test.js
├── package.json
├── .gitignore
└── README.md
```

## Essential Packages

### Install Common Packages

```bash
# Testing framework
npm install --save-dev jest

# Linting
npm install --save-dev eslint

# Code formatting
npm install --save-dev prettier

# All at once
npm install --save-dev jest eslint prettier
```

### package.json Configuration

```json
{
  "name": "dsa-practice",
  "version": "1.0.0",
  "description": "DSA learning practice",
  "main": "index.js",
  "scripts": {
    "test": "jest",
    "lint": "eslint src/",
    "format": "prettier --write src/"
  },
  "devDependencies": {
    "jest": "^29.0.0",
    "eslint": "^8.0.0",
    "prettier": "^3.0.0"
  }
}
```

## Testing Setup

### Jest Configuration

```bash
# Install jest
npm install --save-dev jest

# Initialize jest
npx jest --init
```

### Write Tests

```javascript
// twoSum.test.js
const twoSum = require('../src/twoSum');

describe('twoSum', () => {
  test('finds two numbers that sum to target', () => {
    expect(twoSum([2, 7, 11, 15], 9)).toEqual([0, 1]);
  });

  test('returns empty array if no solution', () => {
    expect(twoSum([1, 2], 5)).toEqual([]);
  });
});
```

### Run Tests

```bash
# Run all tests
npm test

# Run specific test file
npm test -- twoSum.test.js

# Watch mode
npm test -- --watch
```

## IDE Setup

### VS Code

1. **Install Extensions**
   - ES7+ React/Redux/React-Native snippets
   - ESLint
   - Prettier - Code formatter
   - Thunder Client (for API testing)

2. **Settings (settings.json)**
```json
{
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true
  },
  "eslint.validate": ["javascript"],
  "eslint.format.enable": true
}
```

### WebStorm

1. Built-in support for JavaScript
2. Configure: Settings → Languages & Frameworks → JavaScript
3. Enable ESLint

## Running Code

### Direct Execution

```bash
# Run JavaScript file
node solution.js

# REPL
node
> console.log("Hello")
> .exit
```

### Using npm Scripts

```bash
# Add to package.json
"scripts": {
  "dev": "node src/solution.js",
  "start": "node index.js"
}

# Run
npm run dev
```

## Debugging

### Using Node Debugger

```bash
# Start in debug mode
node inspect solution.js

# Commands
c       - continue
n       - next
s       - step into
o       - step out
l       - list source
p variable - print variable
```

### Using Console

```javascript
console.log('Value:', value);
console.table(array);         // Table format
console.time('label');        // Start timer
console.timeEnd('label');     // End timer
console.assert(condition);    // Assert
```

## Performance Profiling

### Timing Code

```javascript
console.time('label');
// Code to measure
console.timeEnd('label');

// Or
const start = performance.now();
// Code
const end = performance.now();
console.log(`Time: ${end - start}ms`);
```

### Using Profiler

```bash
# Run with profiler
node --prof solution.js

# Analyze
node --prof-process isolate-*.log > analysis.txt
```

## Common Commands

```bash
# Install package
npm install package_name

# Install dev dependency
npm install --save-dev package_name

# Update packages
npm update

# List installed packages
npm list

# Remove package
npm uninstall package_name

# Clear cache
npm cache clean --force

# Global install
npm install -g package_name
```

## Troubleshooting

### Module Not Found
```bash
# Clear node_modules and reinstall
rm -rf node_modules
npm install
```

### Permission Denied
```bash
# Use sudo for global
sudo npm install -g package

# Or fix npm permissions
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
```

### Version Conflicts
```bash
# Check version
npm list package_name

# Install specific version
npm install package_name@1.2.3
```

## Tips

1. Use Node 14+ for best compatibility
2. Keep node_modules out of git (use .gitignore)
3. Lock versions with package-lock.json
4. Use npm scripts for common tasks
5. Test frequently during development

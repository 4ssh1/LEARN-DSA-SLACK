# Python Setup Guide

## Installation

### Windows

1. **Download Python**
   - Visit [python.org](https://www.python.org/)
   - Download Python 3.9 or later
   - Run the installer

2. **Add to PATH**
   - Check "Add Python to PATH" during installation
   - Verify: `python --version`

### macOS

```bash
# Using Homebrew
brew install python3

# Verify
python3 --version
```

### Linux (Ubuntu/Debian)

```bash
# Update package manager
sudo apt update

# Install Python
sudo apt install python3 python3-pip

# Verify
python3 --version
```

## Virtual Environment

### Create Virtual Environment

```bash
# Create venv
python -m venv dsa_env

# Activate (Windows)
dsa_env\Scripts\activate

# Activate (macOS/Linux)
source dsa_env/bin/activate
```

### Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install common packages
pip install pytest numpy pandas

# Create requirements file
pip freeze > requirements.txt
```

## IDE Setup

### VS Code

1. **Install Extensions**
   - Python (Microsoft)
   - Pylance
   - Python Debugger

2. **Configure Interpreter**
   - Ctrl+Shift+P → "Python: Select Interpreter"
   - Choose virtual environment

3. **Settings (settings.json)**
```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```

### PyCharm

1. **Create Project**
   - File → New Project
   - Select interpreter or create venv

2. **Configure**
   - File → Settings → Project → Python Interpreter
   - Add packages via interface

## Testing Setup

### pytest

```bash
# Install
pip install pytest

# Create test file
# test_solution.py
def test_two_sum():
    assert two_sum([2,7,11,15], 9) == [0, 1]

# Run tests
pytest test_solution.py
```

### unittest (Built-in)

```python
import unittest

class TestSolution(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2,7,11,15], 9), [0, 1])

if __name__ == '__main__':
    unittest.main()
```

## Essential Packages

```bash
# Data structures and utilities
pip install numpy pandas

# Testing
pip install pytest pytest-cov

# Code quality
pip install black flake8 pylint

# Profiling
pip install line_profiler memory_profiler
```

## Running Code

### Simple Execution

```bash
# Run Python file
python solution.py

# Run Python interactively
python

# Or with venv
python -m solution.py
```

### Debugging

```python
# Using pdb
import pdb
pdb.set_trace()  # Break point

# Or use Python debugger
python -m pdb solution.py
```

## Performance Profiling

### Time Profiling

```bash
# Using timeit
python -m timeit 'sum(range(100))'

# Or in code
import timeit
timeit.timeit('sum(range(100))', number=100000)
```

### Memory Profiling

```bash
# Install
pip install memory-profiler

# Profile
python -m memory_profiler solution.py
```

## Project Structure

```
dsa-practice/
├── venv/                 # Virtual environment
├── solutions/
│   ├── week01/
│   │   ├── two_sum.py
│   │   └── best_time.py
│   └── week02/
├── tests/
│   ├── test_week01.py
│   └── test_week02.py
├── requirements.txt
└── README.md
```

## Common Commands

```bash
# Create venv
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Activate venv (Unix)
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# List installed packages
pip list

# Freeze requirements
pip freeze > requirements.txt

# Deactivate venv
deactivate

# Remove venv
rm -rf venv  # Unix
rmdir /s venv  # Windows
```

## Troubleshooting

### Module Not Found
```bash
# Ensure venv is activated
pip install package_name
```

### Permission Denied
```bash
# Try with --user flag
pip install --user package_name
```

### Version Conflicts
```bash
# Specify version
pip install package_name==1.2.3

# Check installed version
pip show package_name
```

## Tips

1. Always use virtual environment
2. Keep requirements.txt updated
3. Use consistent Python version
4. Test code regularly
5. Profile before optimizing

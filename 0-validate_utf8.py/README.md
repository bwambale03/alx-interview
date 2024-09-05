# UTF-8 Validation

This project contains a Python method to validate if a given data set represents valid UTF-8 encoding.

## Concepts Covered
- **Bitwise Operations**: Manipulating bits with AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), and shifts (`<<`, `>>`).
- **UTF-8 Encoding**: Handling multi-byte characters and ensuring valid encoding patterns.
- **Data Representation**: Working with the least significant bits of integers.
- **List Manipulation**: Iterating through and accessing list elements in Python.
- **Boolean Logic**: Applying logical operations to check conditions.

## Requirements
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.
- Files should follow PEP 8 style and be executable.
- First line of all Python scripts must be `#!/usr/bin/python3`.

## Task
Implement `def validUTF8(data):` to validate UTF-8 encoding.

## Usage Example
```python
data = [229, 65, 127, 256]
print(validUTF8(data)) # False

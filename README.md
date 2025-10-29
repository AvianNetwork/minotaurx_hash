# minotaurx_hash

A Python C extension module for the MinotaurX proof-of-work hash function. This module provides high-performance cryptographic hashing used in blockchain mining.

## Features

- **Fast C implementation** - Compiled C extension for optimal performance
- **Python 3.6+** - Modern Python support (Python 2 no longer supported)
- **Deterministic** - Same input always produces the same output
- **32-byte output** - Produces 256-bit hash digests
- **Cross-platform** - Works on Linux, macOS, and Windows

## Prerequisites

### Linux (Ubuntu/Debian)

```bash
sudo apt-get install python3-dev build-essential
```

### macOS

```bash
xcode-select --install
```

### Windows

- Install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) or Visual Studio Community
- Or use MinGW-w64

## Installation

### From Source

Clone the repository and install:

```bash
git clone https://github.com/AvianNetwork/minotaurx_hash.git
cd minotaurx_hash
pip install -e .
```

### For Development

Install in editable mode with development tools:

```bash
pip install -e ".[dev]"
```

## Usage

```python
import minotaurx_hash
from binascii import hexlify, unhexlify

# Input must be exactly 80 bytes (typical blockchain block header)
input_data = unhexlify('700000005d385ba114d079970b29a9418fd0549e7d68a95c7f168621a314201000000000578586d149fd07b22f3a8a347c516de7052f034d2b76ff68e0d6ecff9b77a45489e3fd511732011df0731000')

# Generate hash
hash_result = minotaurx_hash.getPoWHash(input_data)

# Display as hex string
print(hexlify(hash_result).decode())
# Output: 43ea5f3eaaac756aaa2711a18c234e13038dd3b1462aae1aa710bb158f4acca9
```

## API Reference

### `getPoWHash(data: bytes) -> bytes`

Computes the MinotaurX proof-of-work hash.

**Parameters:**

- `data` (bytes): Input data, must be exactly 80 bytes

**Returns:**

- `bytes`: 32-byte hash digest

**Raises:**

- `TypeError`: If input is not bytes
- `ValueError`: If input length is not exactly 80 bytes

## Testing

Run the comprehensive test suite:

```bash
# Using unittest
python test.py

# Or using unittest discovery
python -m unittest discover

# Or using pytest (if installed)
pytest test.py -v
```

The test suite includes:

- Known hash vector validation
- Output format and size verification
- Determinism checking
- Invalid input handling

## Building Wheels

Build distribution wheels for all supported platforms:

```bash
pip install cibuildwheel
cibuildwheel --output-dir wheelhouse
```

This requires Docker on Linux or can use native build tools on macOS/Windows.

## Supported Python Versions

- Python 3.6+
- CPython only (PyPy not supported due to C extension)

## Algorithm Details

MinotaurX combines multiple hash algorithms in a deterministic graph traversal:

- **Base algorithms**: BLAKE, BMW, CubeHash, Echo, Fugue, Grøstl, HAMSI, JH, Keccak, Luffa, SHABAL, SHAvite, SIMD, Skein, Whirlpool, SHA-2
- **CPU-hardening**: yespower algorithm at leaf nodes
- **Traversal**: Binary tree path determined by intermediate hash outputs
- **Output**: Final 32 bytes of the result hash

For more details on the algorithm, see the comments in `minotaurx.c`.

## Contributing

Contributions are welcome! Please ensure:

- Code follows existing style conventions
- Changes include tests
- All tests pass: `python test.py`

## License

Licensed under the MIT/X11 software license. See the [LICENSE](LICENSE) file for details.

## Authors

- Original Minotaur algorithm: The Litecoin Cash Core developers
- MinotaurX implementation: The Avian Core developers
- Contributors: Shafil Alam and others

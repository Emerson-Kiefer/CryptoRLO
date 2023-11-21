# cryptogame Library

The `cryptogame` library provides a collection of cryptographic games for educational and testing purposes. These games simulate various security scenarios and can be used to understand and evaluate the security properties of cryptographic primitives.

## Folder Structure

The library is organized into the following structure:

```plaintext
cryptogame/
|-- games/
|   |-- __init__.py
|   |-- uf_cma.py
|   |-- ind_cpa.py
|   |-- int_ctxt.py
|   |-- prf.py
|   |-- ufcma.py
|-- tools/
|   |-- __init__.py
|   |-- aes.py
|   |-- block_cipher.py
|   |-- modes_of_operation.py
|   |-- utils.py
|-- __init__.py
|-- simulate.py
```

### Games Submodule

The games submodule contains modules for each cryptographic game.

- `uf_cma.py`: Universal Forgery under Chosen-Message Attack (UF-CMA) game.
- `ind_cpa.py`: Indistinguishability under Chosen-Plaintext Attack (IND-CPA) game.
- `int_ctxt.py`: Integrity under Chosen-Ciphertext Attack (INT-CTXT) game.
- `prf.py`: Pseudorandom Function (PRF) game.
- `ufcma.py`: Universal Forgery under Chosen-Message Attack (UF-CMA) game.

### Tools Submodule

The tools submodule contains utility modules and implementations of cryptographic primitives used in the games.

- `aes.py`: Implementation of the Advanced Encryption Standard (AES) algorithm.
- `block_cipher.py`: Generic implementation of a block cipher.
- `modes_of_operation.py`: Implementations of various modes of operation for block ciphers.
- `utils.py`: Utility functions used across the library.

### Simulation Submodule

The simulate submodule contains the Simulate class, which provides methods for simulating different cryptographic games and calculating the advantage of an adversary against various security notions.

- `simulate.py`: The Simulate class.


### Usage Examples

For detailed usage examples and demonstrations of each cryptographic game, refer to the corresponding Jupyter Notebook files in the `games` folder.

- [UF-CMA Game Example](/uf_cma.ipynb)
- [IND-CPA Game Example](/ind_cpa.ipynb)
- [INT-CTXT Game Example](/int_ctxt.ipynb)
- [PRF Game Example](/prf.ipynb)
- [UFCMA Game Example](/ufcma.ipynb)

### Acknowledgments

This library is created for educational purposes. Feel free to contribute, report issues, or suggest improvements. Happy coding!


# cryptogame Library

The `cryptogame` library provides a collection of cryptographic games for educational and testing purposes. These games simulate various security scenarios and can be used to understand and evaluate the security properties of cryptographic primitives.

## Folder Structure

The library is organized into the following structure:

```plaintext
cryptogame/
|-- games/
|   |-- ufcma.py
|   |-- indcpa.py
|   |-- intctxt.py
|   |-- prf.py
|   |-- cr.py
|-- tools/
|   |-- aes.py
|   |-- block_cipher.py
|   |-- modes_of_operation.py
|   |-- utils.py
|-- simulate.py
```

### Games Submodule

The games submodule contains modules for each cryptographic game.

- `uf_cma.py`: UF-CMA game.
- `ind_cpa.py`: Indistinguishability under Chosen-Plaintext Attack (IND-CPA) game.
- `int_ctxt.py`: Integrity under Chosen-Ciphertext Attack (INT-CTXT) game.
- `prf.py`: Pseudorandom Function (PRF) game.
- `cr.py`: CR game

### Tools Submodule

The tools submodule contains utility modules and implementations of cryptographic primitives used in the games.

- `aes.py`: Implementation of the Advanced Encryption Standard (AES) algorithm - has evaluate and inverse functions. 
- `block_cipher.py`: Generic implementation of a block cipher has evaluate and inverse functions. 
- `modes_of_operation.py`: Implementations of various modes of operation for block ciphers.
- `utils.py`: Utility functions used across the library.

### Simulation Submodule

The simulate submodule contains the Simulate class, which provides methods for simulating different cryptographic games and calculating the advantage of an adversary against various security notions.

- `simulate.py`: The Simulate class.


### Usage Examples

For detailed usage examples and demonstrations of each cryptographic game, refer to the corresponding Jupyter Notebook files in the `test` folder.

- [UF-CMA Game Example](/RLO/mac.ipynb)
- [IND-CPA Game Example](/RLO/indcpa.ipynb)
- [INT-CTXT Game Example](/RLO/intctxt.ipynb)
- [PRF Game Example](/RLO/prf.ipynb)
- [CR Game Example](/RLO/hash.ipynb)

### Acknowledgments

This library is created for educational purposes. Feel free to contribute, report issues, or suggest improvements. Happy coding!


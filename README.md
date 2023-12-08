# cryptogame Library

The `cryptogame` library provides a collection of cryptographic games for educational and testing purposes. These games simulate various security scenarios and can be used to understand and evaluate the security properties of cryptographic primitives. The library allows to define protocols/ primitives and the adversary attacking the primitive. Currently it supports SK crypto. 


Note: The library only supports binary strings eg '00001' or '11111000'. 
Eg; `BlockCipher.evaluate(key = '0001', msg = '1111')`

A good starting point to understand the lib would be `tests/hash.ipynb`. 

# Installation

Python Version >= 3.8

pip install -i https://test.pypi.org/simple/ cryptogame==0.0.7

[https://test.pypi.org/project/playcrypt/0.0.7/]


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

The games submodule contains modules for each cryptographic game. Each game has functions for initialize, finalize and the oracles as defined in the lectures. 

- `uf_cma.py`: UF-CMA game.
- `ind_cpa.py`: Indistinguishability under Chosen-Plaintext Attack (IND-CPA) game.
- `int_ctxt.py`: Integrity under Chosen-Ciphertext Attack (INT-CTXT) game.
- `prf.py`: Pseudorandom Function (PRF) game.
- `cr.py`: CR game

### Tools Submodule

The tools submodule contains utility modules and implementations of cryptographic primitives used in the games.

- `aes.py`: Implementation of the Advanced Encryption Standard (AES) algorithm - has evaluate and inverse functions. 
- `block_cipher.py`: Generic implementation of a block cipher has evaluate and inverse functions. 
- `modes_of_operation.py`: Implementations of various modes of operation for block ciphers and MACs. 
- `utils.py`: Utility functions used across the library. Functions `xor(c1,c2): returns the bitwise xor of c1 and c2` and `random_bits(length): returns a binary string of size length`.

### Simulation Submodule

The simulate submodule contains the Simulate class, which provides methods for simulating different cryptographic games. The simulator computes the advantage of an adversary against various security notions.

- `simulate.py`: The Simulate class.

- Ref to 


### Usage Examples

For detailed usage examples and demonstrations of each cryptographic game, refer to the corresponding Jupyter Notebook files in the `test` folder.

- [UF-CMA Game Example](/src/test/mac.ipynb)
- [IND-CPA Game Example](/src/test/indcpa.ipynb)
- [INT-CTXT Game Example](/src/test/intctxt.ipynb)
- [PRF Game Example](/src/test/prf.ipynb)
- [CR Game Example](/src/test/hash.ipynb)

### Acknowledgments

This library is created for educational purposes. Feel free to contribute, report issues, or suggest improvements. Happy coding!


# Usage
## Please refer other games in tests/ .ipynb
```
from cryptogame.tools.utils import random_bits
from cryptogame.tools.AES import *
from cryptogame.game.indcpa import *
from cryptogame.game.int_ctxt import *
from simulate import *

key_len = 128
block_len = 128
aes = AES(key_len, block_len)


def enc(key, m):
	if len(m) != 512:
		return None

	ce_0 = random_bits(128)
	cm_0 = '0' * 128
	c = ce_0
	for i in range(4):
		encrypted_block = aes.evaluate(key, xor(ce_0, m[i * block_len: (i + 1) * block_len]))
		ce_0 = encrypted_block  ## updating ce_0 for ce[i-1]
		c += encrypted_block

		cm_i = aes.evaluate(key, xor(cm_0, m[i * block_len: (i + 1) * block_len]))
		cm_0 = cm_i
	return (c, cm_i)


def dec(key, c):
	cipher, t = c
	if len(cipher) != 640:
		return None
	cm_0 = '0' * 128
	ce_0 = cipher[:block_len]
	ce = cipher[block_len:]
	m_i = str()
	for i in range(4):
		decrypted_block = xor(aes.inverse(key, ce[i * block_len: (i + 1) * block_len]), ce_0)
		m_i += decrypted_block
		ce_0 = ce[i * block_len: (i + 1) * block_len]

		cm_i = aes.evaluate(key, xor(cm_0, decrypted_block))
		cm_0 = cm_i
	if cm_i == t:
		return m_i
	else:
		return None


### Is SE IND-CPA secure?

game_indcpa = INDCPA(enc, dec, 128, 128, 10)
game_indcpa._initialize()


def adv_indcpa(game):
	# ========= Your Code goes here =======================
	x = random_bits(512)
	y = random_bits(512)

	q1 = game.LR(x, x)
	c1, t1 = q1

	q2 = game.LR(x, y)
	c2, t2 = q2
	# =====================================================
	if t1 == t2:
		return 1
	else:
		return 0


game_indcpa.finalize(adv_indcpa(game_indcpa))
s = Simulate(game_indcpa, adv_indcpa)
s.simulate_INDCPA(verbose=True)

game_intctxt = INTCTXT(enc, dec, 128, 20)
game_intctxt._initialize()

def adv_intctxt(game: INTCTXT):
	#========= Your Code goes here =======================
	x = '0'*512
	cipher, tag = game.Enc(x)
	c_0 = '0'*128
	c_1 = cipher[1*128:2*128]
	c_2 = cipher[2*128: 3*128]
	c_3 = cipher[3*128 : 4*128]
	c_4 = cipher[4*128: 5*128]
	c_prime = c_0 + c_1 + c_2 + c_3 + c_4
	t_prime = c_4
	# =====================================================
	return (c_prime, t_prime)

game_intctxt.finalize(adv_intctxt(game_intctxt))
s = Simulate(game_intctxt, adv_intctxt)
s.simulate_intctxt(verbose= True)
```

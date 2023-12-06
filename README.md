# CryptoRLO
PlayCrypt collection of cryptography games and simulators implemented in Python, used for the UCSD CSE 107 Introduction to Cryptography course. Documentation is available at https://ucsdcse107.github.io/playcrypt/. See the "Getting Started" section for installation help.

The block cipher game is in src. 

# Installation

pip install -i https://test.pypi.org/simple/ cryptogame==0.0.3

[https://test.pypi.org/project/playcrypt/0.0.3/]

# Usage
```
from cryptogame.games.game_kr import *
from cryptogame.ideal.block_cipher import *
import itertools
from cryptogame.simulator import kr_sim

key_length = 4 ## user defined
block_length = 4 ## user defined
queries = 1 ## user defined

def exhaustive_key_search(block_cipher:BlockCipher, game:GameKR, message:list, ciphertext:list): ## this is the function adversary will run to determine the key

	consistent_keys = []
	all_keys = generate_binary_strings(key_length)
	for k in all_keys:
		count = 0
		for i, m in enumerate(message):
			if block_cipher.ciphers[(k, m)] == list(ciphertext)[i]:
				count += 1
		if count == len(message):
			consistent_keys.append(k)
	return consistent_keys

b = BlockCipher(key_len=key_length, block_len=block_length)
# print(b.ciphers)

## Game Starts here

g = GameKR(queries=queries, block_cipher=b, key_len= key_length, block_len=block_length)
g.initialize() ## this is the initialize phase that the challenger runs
print("key", g.key)


## adversary make q queries on its choice of message. we will consider random message here:: this has to be simulated


messages = list()
ciphertexts = list()
for i in range(queries):
	m_i = random_string(block_length)
	c_i = g.fn(m_i)
	messages.append(m_i)
	ciphertexts.append(c_i)

## adversary now runs exhaustive_key_search / does a random guess to output k_prime

# # if random guess
# k_prime = random_string(key_length)

## if adversary runs exhaustive_key_search
k_prime = exhaustive_key_search(b, g,messages, ciphertexts)
print(k_prime)

# now k_prime is passed on the the finalize procedure  of the game
# result = g.finalize(key_guess=k_prime)
# print(result)
## simulating the game for n number of times
```

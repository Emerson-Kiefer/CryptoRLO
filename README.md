# CryptoRLO
PlayCrypt collection of cryptography games and simulators implemented in Python, used for the UCSD CSE 107 Introduction to Cryptography course. Documentation is available at https://ucsdcse107.github.io/playcrypt/. See the "Getting Started" section for installation help.

The block cipher game is in src. 

# Installation

pip install -i https://test.pypi.org/simple/ cryptogame==0.0.7

[https://test.pypi.org/project/playcrypt/0.0.7/]

# Usage
## Please refer other games in other .ipynb
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

try:
	from block_cipher import *
	from AES import *
	from utils import *
except:
	from cryptogame.tools.block_cipher import *
	from cryptogame.tools.AES import *
	from cryptogame.tools.utils import *

class ECB:

	def __init__(self, function: Function) -> None:
		self.f = function

	def encrypt(self, key,  M):
		m = len(M)//self.f.block_len
		assert m*self.f.block_len == len(M), "message needs to be a multiple of block length"
		c = ''
		for i in range(m):
			c += self.f.evaluate(key, M[i * self.f.block_len : (i + 1) * self.f.block_len])
		return c
	
	def decrypt(self, key, C):
		m = ''
		c = len(C)//self.f.block_len
		assert c*self.f.block_len == len(C), "Cipher needs to be a multiple of block length"
		
		for i in range(c):
			m += self.f.inverse(key, C[i*self.f.block_len : (i + 1) * self.f.block_len ])
		return m


class CBC:
	def __init__(self, function: Function) -> None:
		self.f = function
	
	def encrypt(self, key, M):
		m = len(M) // self.f.block_len
		assert m * self.f.block_len == len(M), "message needs to be a multiple of block length"

		c_0 = random_bits(self.f.block_len)
		c = c_0
		for i in range(m):
			encrypted_block = self.f.evaluate(key, xor(M[i * self.f.block_len : (i + 1) * self.f.block_len], c_0))
			c_0 = encrypted_block
			c += encrypted_block
		return c
	
	def decrypt(self, key, C):
		m = ''
		c = len(C)//self.f.block_len
		assert c*self.f.block_len == len(C), "Cipher needs to be a multiple of block length"
		
		c_0 = C[:self.f.block_len]
		for i in range(c):
			decrypted_block = self.f.inverse(key, C[i*self.f.block_len : (i + 1) * self.f.block_len])
			m += xor(decrypted_block, c_0)
			c_0 = C[i*self.f.block_len : (i + 1) * self.f.block_len]
		return m[self.f.block_len:]
	


class CTR:
	def __init__(self, function: Function) -> None:
		self.f = function
	
	def encrypt(self, key, M):
		m = len(M) // self.f.block_len
		assert m * self.f.block_len == len(M), "message needs to be a multiple of block length"

		c_0 = random_bits(self.f.block_len)
		c = c_0
		for i in range(m):
			pad = self.f.evaluate(key, ctr_add(c_0, i + 1, len(c_0)))
			c += xor(pad, M[i * self.f.block_len : (i + 1) * self.f.block_len])
		return c
	
	def decrypt(self, key, C):
		m = ''
		c_0 = C[:self.f.block_len]
		C = C[self.f.block_len:]

		c = len(C)//self.f.block_len
		assert c*self.f.block_len == len(C), "Cipher needs to be a multiple of block length"
		
		for i in range(c):
			decrypted_pad = self.f.evaluate(key, ctr_add(c_0, i + 1, len(c_0)))
			m += xor(decrypted_pad, C[(i)*self.f.block_len : (i + 1) * self.f.block_len])
		return m

class CBC_MAC:

	def __init__(self, function: Function) -> None:
		self.f = function

	def Tag_gen(self, key, message):
		c_0 = '0'*self.f.block_len
		m = len(message) // self.f.block_len
		assert len(message) == m*self.f.block_len, "Message needs to be a multiple of block length"
		for i in range(m):
			c_i = self.f.evaluate(key, xor(c_0, message[i * self.f.block_len : (i + 1) * self.f.block_len]))
			c_0 = c_i
		return c_i
	
class ECBC_MAC:

	def __init__(self, function) -> None:
		self.f = function

	def Tag_gen(self, key, message):
		k_in = key[:self.f.block_len]
		k_out = key[self.f.block_len:]
		c_0 = '0'* self.f.block_len

		m = len(message) // self.f.block_len
		assert len(message) == m*self.f.block_len, "Message needs to be a multiple of block length"
		for i in range(m):
			c_i = self.f.evaluate(k_in, xor(c_0, message[i * self.f.block_len : (i + 1) * self.f.block_len]))
			c_0 = c_i
		return self.f.evaluate(k_out, c_i)

	




if __name__ == '__main__':
	function = BlockCipher(5, 5)
	block_ecb = CTR(function)
	d = block_ecb.encrypt('10101', '1010100000'*5)
	print(d)
	inv = block_ecb.decrypt('10101', d)
	print(inv)


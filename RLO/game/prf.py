from tools.utils import *
from tools.block_cipher import *

class PRF:

	def __init__(self, prf , key_len: int, msg_len: int, max_queries: int) -> None:
		self._prf = prf
		self._random = BlockCipher(key_len, msg_len)
		self.max_queries = max_queries
		
		self.query_set = []
		self.key_len = key_len
		self.msg_len = msg_len

	def _initialize(self):
		self.queries = 0
		self._k = random_bits(self.key_len)
		self._b = random_bits(1) ## 0 is the real world, 1 is the random world
		# self._b = '1'

	def Fn(self, m):
		m = str(m)
		self.queries += 1
		self.query_set.append(m)
		if len(m) != self.msg_len:
			raise ValueError(f"Message lengths must be the same. Expected {len(self.msg_len)} got {len(m)}")
		
		if self.queries > self.max_queries:
			raise SyntaxError("Number of queries exceed the maximum queries allowed")
		
		if self._b == str(0):
			return self._prf(self._k, m)
		else:
			return self._random.block_cipher(self._k, m)
		


	def finalize(self, guess):
		guess = str(guess)
		if guess == self._b:
			return True
		else: 
			return False



from tools.utils import *

class INDCPA:

	def __init__(self, enc, dec, key_len: int, msg_len: int, max_queries: int) -> None:
		self._enc = enc
		self._dec = dec
		self.max_queries = max_queries
		self.query_set = []
		self.key_len = key_len
		self.msg_len = msg_len
	

	def _initialize(self):
		self.queries = 0
		self._k = random_bits(self.key_len)
		self._b = random_bits(1)
		

	def LR(self, m_0, m_1):
		m_0 = str(m_0)
		m_1 = str(m_1)
		self.queries += 1
		self.query_set.append((m_0, m_1))
		if len(m_0) != len(m_1):
			raise ValueError("Message lengths must be the same")
		
		if self.queries > self.max_queries:
			raise ValueError("Number of queries exceed the maximum queries allowed")
		
		if self._b == str(0):
			return self._enc(self._k, m_0)
		else:
			return self._enc(self._k, m_1)
		
	def finalize(self, guess):
		guess = str(guess)
		if guess == self._b:
			return True
		else: 
			return False



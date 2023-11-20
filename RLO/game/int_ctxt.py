from tools.utils import random_bits

class INTCTXT:

	def __init__(self, enc, dec, key_len: int, max_queries: int) -> None:
		self._enc = enc
		self._dec = dec
		self.max_queries = max_queries
		self.key_len = key_len

	def _initialize(self):
		self.query_set = []
		self.queries = 0
		self._k = random_bits(self.key_len)
		self._b = random_bits(1)
		

	def Enc(self, m):
		self.queries += 1
		self.query_set.append(m)
	
		if self.queries > self.max_queries:
			raise ValueError("Number of queries exceed the maximum queries allowed")
		
		c = self._enc(self._k, m)
		self.query_set.append(c)
		return c
		
		
	def finalize(self, C):
		
		m = self._dec(self._k, C)
		if C not in self.query_set and m != None:
			return True
		else: 
			return False


from tools.utils import random_bits

class UFCMA:

	def __init__(self, mac , key_len: int, max_queries: int) -> None:
		self._mac = mac
		self.max_queries = max_queries
		self.key_len = key_len


	def _initialize(self):
		self.queries = 0
		self.query_set = []
		self._k = random_bits(self.key_len)
		

	def Tag(self, m):
		self.queries += 1
		self.query_set.append(m)
	
		if self.queries > self.max_queries:
			raise ValueError("Number of queries exceed the maximum queries allowed")
		
		return self._mac(self._k, m)

	def finalize(self, message, tag):
		if message in self.query_set:
			return False
		else:
			return (self.Tag(message) == tag)



from tools.utils import random_bits

class CR:

	def __init__(self, hash_function,  key_len: int,) -> None:
		self.key_len = key_len
		self.h = hash_function
		self.messages = []

	def _initialize(self):
		self._k = random_bits(self.key_len)
		return self._k
		

	def finalize(self, x1, x2):
		if x1 == x2:
			return False
		else:
			return (self.h(self._k, x1) == self.h(self._k, x2))
	



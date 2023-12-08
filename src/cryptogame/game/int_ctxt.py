from cryptogame.tools.utils import random_bits

class INTCTXT:
	"""
    The INTCTXT class represents an Integrity under Chosen-Ciphertext Attack (INT-CTXT) game.

    Attributes:
        enc: The encryption function used in the game.
        dec: The decryption function used in the game.
        key_len (int): The length of the encryption key.
        max_queries (int): The maximum number of queries allowed in the game.

    Methods:
        __init__(self, enc, dec, key_len: int, max_queries: int) -> None:
            Initializes a new Integrity under Chosen-Ciphertext Attack (INT-CTXT) game instance
            with the specified encryption and decryption functions, key length, and maximum allowed queries.

        _initialize(self):
            Private method to initialize the game by generating a random key and a random bit.

        Enc(self, m):
            Simulates a game query by encrypting the provided plaintext message and updating the query set.

        finalize(self, C):
            Finalizes the game by checking if the provided ciphertext is not in the query set and can be decrypted.

    Usage:
        For usage check intctxt.ipynb
    """

	def __init__(self, enc, dec, key_len: int, max_queries: int) -> None:
		self._enc = enc
		self._dec = dec
		self.max_queries = max_queries
		self.key_len = key_len

	def _initialize(self):
		"""
        Private method to initialize the game by generating a random key and a random bit.
        """
		self.query_set = []
		self.queries = 0
		self._k = random_bits(self.key_len)
		self._b = random_bits(1)
		

	def Enc(self, m):
		"""
        Simulates the Enc oracle by encrypting the provided plaintext message and updating the query set.

        Parameters:
            m: The plaintext message to be encrypted.

        Returns:
            str: The ciphertext corresponding to the provided plaintext message.
        """
		self.queries += 1
		self.query_set.append(m)
	
		if self.queries > self.max_queries:
			raise ValueError("Number of queries exceed the maximum queries allowed")
		
		c = self._enc(self._k, m)
		self.query_set.append(c)
		return c
		
		
	def finalize(self, C):
		"""
        Finalizes the game by checking if the provided ciphertext is not in the query set and can be decrypted.

        Parameters:
            C: The ciphertext to be finalized.

        Returns:
            bool: True if the ciphertext is not in the query set and can be decrypted, False otherwise.
        """
		m = self._dec(self._k, C)
		if C not in self.query_set and m != None:
			return True
		else: 
			return False


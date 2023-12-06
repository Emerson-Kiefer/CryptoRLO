from cryptogame.tools.block_cipher import *

class PRF:
	"""
    The PRF class represents a Pseudorandom Function (PRF) game.

    Attributes:
        prf: The pseudorandom function used in the game.
        _random: ideal block cipher
        key_len (int): The length of the key used in the pseudorandom function and block cipher.
        msg_len (int): The length of the messages processed by the pseudorandom function and block cipher.
        max_queries (int): The maximum number of queries allowed in the game.
        query_set: A list to store messages used in queries.

    Methods:
        __init__(self, prf, key_len: int, msg_len: int, max_queries: int) -> None:
            Initializes a new Pseudorandom Function (PRF) game instance with the specified PRF,
            key length, message length, and maximum allowed queries.

        _initialize(self):
            Private method to initialize the game by generating a random key and a random bit.

        Fn(self, m):
            Simulates a Fn oracle by evaluating the pseudorandom function on the provided message.

        finalize(self, guess):
            Finalizes the game by checking if the guess matches the randomly chosen bit.

    Usage:
        For usage check prf.ipynb
    """

	def __init__(self, prf , key_len: int, msg_len: int, max_queries: int) -> None:
		self._prf = prf
		self._random = BlockCipher(key_len, msg_len)
		self.max_queries = max_queries
		
		self.query_set = []
		self.key_len = key_len
		self.msg_len = msg_len

	def _initialize(self):
		"""
        Private method to initialize the game by generating a random key and a random bit.
        """
		self.queries = 0
		self._k = random_bits(self.key_len)
		self._b = random_bits(1) ## 0 is the real world, 1 is the random world
		# self._b = '1'

	def Fn(self, m):
		"""
        Simulates the Fn oracle by evaluating the pseudorandom function on the provided message.

        Parameters:
            m: The message on which the pseudorandom function is applied.

        Returns:
            str: The result of applying the pseudorandom function on the message.
        """
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
		"""
        Finalizes the game by checking if the guess matches the randomly chosen bit.

        Parameters:
            guess: The guessed bit.

        Returns:
            bool: True if the guess matches the chosen bit, False otherwise.
        """
		guess = str(guess)
		if guess == self._b:
			return True
		else: 
			return False



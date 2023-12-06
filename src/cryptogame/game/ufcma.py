from cryptogame.tools.utils import random_bits

class UFCMA:

	"""
    The UFCMA class represents a UFCMA game.

    Attributes:
        mac: The message authentication code (MAC) used in the game.
        key_len (int): The length of the key used in the MAC.
        max_queries (int): The maximum number of queries allowed in the game.

    Methods:
        __init__(self, mac, key_len: int, max_queries: int) -> None:
            Initializes a new Universal Forgery under Chosen-Message Attack (UF-CMA) game instance
            with the specified MAC, key length, and maximum allowed queries.

        _initialize(self):
            Private method to initialize the game by generating a random key.

        Tag(self, m):
            Simulates a tag generation oracle by computing the MAC of the provided message.

        finalize(self, message, tag):
            Finalizes the game by checking if the message was not queried before and if the provided tag is valid.

    Usage:
        For usage check mac.ipynb
    """

	def __init__(self, mac , key_len: int, max_queries: int) -> None:
		self._mac = mac
		self.max_queries = max_queries
		self.key_len = key_len


	def _initialize(self):
		"""
        Private method to initialize the game by generating a random key.
        """
		self.queries = 0
		self.query_set = []
		self._k = random_bits(self.key_len)
		

	def Tag(self, m):
		"""
        Simulates a teg gen oracle by computing the MAC of the provided message.

        Parameters:
            m: The message for which the MAC is computed.

        Returns:
            str: The MAC of the provided message.
        """
		self.queries += 1
		self.query_set.append(m)
	
		if self.queries > self.max_queries:
			raise ValueError("Number of queries exceed the maximum queries allowed")
		
		return self._mac(self._k, m)

	def finalize(self, message, tag):
		"""
        Finalizes the game by checking if the message was not queried before and if the provided tag is valid.

        Parameters:
            message: The message to be finalized.
            tag: The MAC tag to be validated.

        Returns:
            bool: True if the message was not queried before and the tag is valid, False otherwise.
        """
		if message in self.query_set:
			return False
		else:
			return (self.Tag(message) == tag)



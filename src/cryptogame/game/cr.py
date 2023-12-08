from cryptogame.tools.utils import random_bits

class CR:
	"""
    The CR class represents a Collision Resistance (CR) game for hash functions.

    Attributes:
        hash_function: User defined hash function
        key_len (int): The length of the random key used in the collision resistance game.
        messages: A list to store committed messages.

    Methods:
        __init__(self, hash_function, key_len: int) -> None:
            Initializes a new Collision Resistance game instance with the specified hash function and key length.

        _initialize(self):
            Private method to generate and set a random key of the specified length.

        finalize(self, x1, x2):
            Finalizes the collision resistance game by comparing the hash values of two provided values with the generated key.

    Usage:
        # Example usage of the Collision Resistance game
		def hash_function():
			...

        cr_instance = CR(hash_function=hash_function, key_len=16)
        cr_instance._initialize()

		def adv(cr_instance):
			...
			return x1, x2

        result = cr_instance.finalize(x1, x2)
    """

	def __init__(self, hash_function,  key_len: int,) -> None:
		self.key_len = key_len
		self.h = hash_function
		self.messages = []

	def _initialize(self):
		"""
        Private method to generate and set a random key of the specified length.

        Returns:
            str: The generated random key.
        """

		self._k = random_bits(self.key_len)
		return self._k
		

	def finalize(self, x1, x2):
		"""
        Finalizes the collision resistance game by computing the function on the inputs and the key.

        Parameters:
            x1: The first value to be compared.
            x2: The second value to be compared.

        Returns:
            bool: True if the hash values are equal, False otherwise.
        """

		if x1 == x2:
			return False
		else:
			return (self.h(self._k, x1) == self.h(self._k, x2))
	



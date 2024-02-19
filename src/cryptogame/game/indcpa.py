from cryptogame.tools.utils import *

class INDCPA:

	"""
    The INDCPA class represents an Indistinguishability under Chosen-Plaintext Attack (IND-CPA) game.

    Attributes:
        enc: The encryption function used in the game.
        dec: The decryption function used in the game.
        key_len (int): The length of the encryption key.
        msg_len (int): The length of the plaintext messages.
        max_queries (int): The maximum number of queries allowed in the game.
        query_set: A list to store pairs of plaintext messages used in queries.

    Methods:
        __init__(self, enc, dec, key_len: int, msg_len: int, max_queries: int) -> None:
            Initializes a new IND-CPA game instance with the specified encryption and decryption functions,
            key length, message length, and maximum allowed queries.

        _initialize(self):
            Private method to initialize the game by generating a random key and a random bit.

        LR(self, m_0, m_1):
            Simulates a game query by encrypting one of the provided plaintext messages based on a random bit.

        finalize(self, guess):
            Finalizes the game by checking if the guess matches the randomly chosen bit.

    Usage:
        # Example usage of the IND-CPA game
		b = BlockCipher(10, 5)
		def enc(key, m, block_cipher = b):
			
			q = len(m) // block_cipher.block_len
			C_t = []
			for i in range(q):
				ct = block_cipher.evaluate(key, m[i*block_cipher.block_len:(i+1)*block_cipher.block_len])
				C_t.append(ct)
			return C_t

		def dec():
			pass

		game = INDCPA(ecb_enc, ecb_dec, key_len=10,msg_len=5, max_queries=2)
		game._initialize()

		def adv(game):
			q1 = game.LR('00000', '00000')
			q2 = game.LR('00000', '10000')

			if q1 == q2:
				return 1
			else:
				return 0
		guess = adv(game)

		game.finalize(guess)
    """

	def __init__(self, enc, dec, key_len: int, msg_len: int, max_queries: int) -> None:
		self._enc = enc
		self._dec = dec
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
		self._b = random_bits(1)
		

	def LR(self, m_0, m_1):
		"""
        Simulates the LR oracle by encrypting one of the provided plaintext messages based on a random bit.

        Parameters:
            m_0: The first plaintext message.
            m_1: The second plaintext message.

        Returns:
            str: The ciphertext corresponding to the chosen plaintext message.
        """
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



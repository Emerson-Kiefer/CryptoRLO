try:
	from utils import random_bits
	from functions import *
except:
	from tools.utils import random_bits, generate_binary_strings
	from tools.functions import *


class BlockCipher(Function):
	
	def __init__(self, key_len, block_len) -> None:
		super().__init__()
		self.key_len = key_len
		self.block_len = block_len
		self.messages = {}
		self.ciphers = {}

	def evaluate(self, key, plaintext):
		"""
        Evaluate the block cipher. Implements an ideal block cipher

        Parameters:
            key (str): The key used for encryption.
            plaintext (str): The plaintext to encrypt.

        Returns:
            str: The ciphertext resulting from the encryption.
        
        Raises:
            ValueError: If the key length does not match the specified key length.
            ValueError: If the plaintext length does not match the specified block length.
        """
		key = str(key)
		self.key  = key
		plaintext = str(plaintext)
		
		if len(key) != self.key_len:
			raise ValueError("Key length do not match key")
		
		if len(plaintext) != self.block_len:
			raise ValueError("plaintext length do not match Block length")

		try:
			return self.ciphers[(key, plaintext)]
		except:
			ct = random_bits(self.block_len)

			try:
				while (key, ct) in self.messages:
					ct = random_bits(self.block_len)
			except:
				pass

			self.messages[(key, ct)] = plaintext
			self.ciphers[(key, plaintext)] = ct
			return ct
		
	def inverse(self, key, ciphertext):
		"""
        Computing the  blockcipher inverse BlockCipher.

        Parameters:
            key (str): The key used for decryption.
            ciphertext (str): The ciphertext to decrypt.

        Returns:
            str: The plaintext resulting from the decryption.
        
        Raises:
            ValueError: If the ciphertext length does not match the block length.
        """


		if len(ciphertext) != self.block_len:
			raise ValueError("Ciphertext length do not match block length")
		try: 
			return self.messages[(key, ciphertext)]
		except:
			
			pt = random_bits(self.block_len)

			try:
				while (key, pt) in self.ciphers:
					pt = random_bits(self.block_len)
			except:
				pass

			self.messages[(key, ciphertext)] = pt
			self.ciphers[(key, pt)] = ciphertext
			return pt


if __name__ == "__main__":
    #Example usage:
    key = '0'*128  # 128-bit key
    plaintext = '0'*128  # 64-bit plaintext

    # Encrypt
    aes = BlockCipher(128, 128)
    ciphertext = aes.evaluate(key, plaintext)
    print("Encrypted message (binary):", ciphertext)

    # Decrypt
    decrypted_message = aes.inverse(key, ciphertext)
    print("Decrypted message (binary):", decrypted_message)
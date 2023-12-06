try:
    from Crypto.Cipher import AES as AES_C
    from functions import *
except:
	from Crypto.Cipher import AES as AES_C
	from cryptogame.tools.functions import *



class AES(Function):
    def __init__(self, key_len, block_len) -> None:
        super().__init__()
        self.key_len = key_len
        self.block_len = block_len

    def evaluate(self, key, plaintext):
        """
        Encrypts m with AES in ECB mode.

        :param k: should be a binary string of length 128, 192, or 256
        :param m: should be a binary string of length multiple of 128
        :return: cipher text as binary string
        """
        k = bytes(int(key[i:i+8], 2) for i in range(0, len(key), 8))
        cipher = AES_C.new(k, mode=AES_C.MODE_ECB)
        plaintext_bytes = bytes(int(plaintext[i:i+8], 2) for i in range(0, len(plaintext), 8))
        ciphertext = cipher.encrypt(plaintext_bytes)
        return ''.join(format(byte, '08b') for byte in ciphertext)

    def inverse(self, key, ciphertext):
        """
        Decrypts c with AES in ECB mode.

        :param k: should be a binary string of length 128, 192, or 256
        :param c: should be a binary string of length multiple of 128
        :return: plaintext as binary string
        """
        k = bytes(int(key[i:i+8], 2) for i in range(0, len(key), 8))
        cipher = AES_C.new(k, mode=AES_C.MODE_ECB)
        ciphertext_bytes = bytes(int(ciphertext[i:i+8], 2) for i in range(0, len(ciphertext), 8))
        decrypted_data = cipher.decrypt(ciphertext_bytes)
        return ''.join(format(byte, '08b') for byte in decrypted_data)



if __name__ == "__main__":
    #Example usage:
    key = '0'*128  # 128-bit key
    plaintext = '0'*128  # 64-bit plaintext

    # Encrypt
    aes = AES(128, 128)
    ciphertext = aes.evaluate(key, plaintext)
    print("Encrypted message (binary):", ciphertext)

    # Decrypt
    decrypted_message = aes.inverse(key, ciphertext)
    print("Decrypted message (binary):", decrypted_message)

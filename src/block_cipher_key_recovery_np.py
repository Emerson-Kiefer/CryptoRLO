import random
import numpy as np

def print_search_table(search_table):
    print('[', end='')
    flag = False
    for row in search_table:
        print('\n [', end='') if flag else print('[', end='')
        flag = True
        for val in row:
            if np.isnan(val):
                print('', end=' ')
            else:
                print(val, end=' ')
        print(']', end ='')
    print(']')


def exhaustive_key_search_interactive():
    K = 5  # Number of block ciphers
    M = 8  # Number of messages
    key_recovery_table = np.array([random.sample(list(range(M)), len(list(range(M)))) for _ in range(K)])
    search_table = np.full(key_recovery_table.shape, np.nan)

    true_key = random.randint(0, K)
    
    true_block_cipher = lambda message: key_recovery_table[true_key][message]
    block_cipher = lambda key, message: key_recovery_table[key][message]

    # print(key_recovery_table)
    # print_search_table(search_table)
    # print(true_key)

    while(1):
        key = int(input("Insert key for block cipher: "))
        message = int(input("Insert message for block cipher: "))
        output = block_cipher(key, message)
        print("E_" + str(key) + "(" + str(message) + ") = " + str(output))
        search_table[key][message] = output
        print_search_table(search_table)
        print("E_k(" + str(message) + ") = " + str(true_block_cipher(message)))

exhaustive_key_search_interactive()
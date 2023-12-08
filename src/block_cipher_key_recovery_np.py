import random
import numpy as np

def print_table(table):
    print("\nE_y(x) values:", end='\n    ')

    for i in range(table.shape[1]): 
        print(str(i) + " ", end='')
    flag = False
    i = 0
    for row in table:
        print("\n  ", end='') if i != table.shape[0] // 2 else print("\ny ", end='')
            
        print( str(i) + '[', end='') 
        flag = True
        for val in row:
            if np.isnan(val):
                print(' ', end=' ')
            else:
                print(int(val), end=' ')
        print(']', end ='')
        i += 1
    print("\n    " + '  ' * (table.shape[1] // 2) + 'x')

def print_action_list():
    print("Actions: (Enter option int 1-3)")
    print(" - 1: E_y(x) | Send message x to block cipher y ")
    print(" - 2: E_k(x) | Send message x to block cipher with target key k")
    print(" - 3: Show table")
    print(" - 4: Guess key | Terminates game")
    print(" - 5: Print action list again")

def block_cipher_action(block_cipher):
    print("\nE_y(x)")
    key = int(input("y = "))
    message = int(input("x = "))
    cipher = block_cipher(key, message)
    print("E_" + str(key) + "(" + str(message) + ") =" + str(cipher))
    return key, message, cipher

def true_block_cipher_action(true_block_cipher):
    print("\nE_k(x)")
    message = int(input("x = "))
    cipher = true_block_cipher(message)
    print("E_k(" + str(message) + ") =" + str(cipher))

def guess_key(true_key, key_recovery_table):
    print("\nEnter your guess for the key k for E_k")
    guess = input("Guess: ")
    if guess == str(true_key):
        print("\nCorrect!")
    else:
        print("\nIncorrect!")
    print("Correct Key: " + str(true_key) + "\n")
    print("Block cipher used was E_" + str(true_key))

    print("Table of keys and messages -  Notice that there may be consistent keys")
    print_table(key_recovery_table)
    exit()


def exhaustive_key_search_interactive():
    K = 5  # Number of block ciphers
    M = 8  # Number of messages
    key_recovery_table = np.array([random.sample(list(range(M)), len(list(range(M)))) for _ in range(K)])
    search_table = np.full(key_recovery_table.shape, np.nan)

    true_key = random.randint(0, K - 1)
    true_block_cipher = lambda message: key_recovery_table[true_key][message]
    block_cipher = lambda key, message: key_recovery_table[key][message]


    print_action_list()
    while(1):
        action = input("\nAction: ")
        if action == "1":
            key, message, cipher = block_cipher_action(block_cipher)
            search_table[key][message] = cipher
        
        if action == "2":
            true_block_cipher_action(true_block_cipher)
        
        if action == "3":
            print_table(search_table)
        
        if action == "4":
            guess_key(true_key, key_recovery_table)
        
        if action == "5":
            print_action_list()
        




exhaustive_key_search_interactive()
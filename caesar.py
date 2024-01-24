import sys

def encrypt(message, k):
    alpha = []
    for x in message:
        numer = ord(x)
        char = numer + k
        if
        alpha.append(chr(char))
    return alpha

def decrypt(message, k):
    for x in message:
        numer = ord(x)
        char = numer - k
        print(chr(char))
    return

if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])
    
    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)
import sys

def encrypt(message, k):
    alpha_encrypt = []
    for x in message:
        numer = ord(x)
        char = numer + k
        if char < 97:
            char += 26
        elif char > 122:
            char -= 26
        alpha_encrypt.append(chr(char))
        encrypt_string = ''.join(alpha_encrypt)
    return encrypt_string

def decrypt(message, k):
    alpha_decrypt = []
    for x in message:
        numer = ord(x)
        char = numer - k
        if char < 97:
            char += 26
        elif char > 122:
            char -= 26
        alpha_decrypt.append(chr(char))
        decrypt_string = ''.join(alpha_decrypt)
    return decrypt_string

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
"""
mkp
week 5
example 2
"""

def encrypt(ciphertext, plaintext_list):
    key = 3
    for ch in plaintext_list:
        num_val = ord(ch) - 97
        new_ch_val = (num_val + key) % 26 + 97
        new_ch = chr(new_ch_val)
        ciphertext.append(new_ch)
        
def main():
    print('This program encrypts lower cases only. Don not use space.')
    plaintext = input("Enter string to encrypt: ")
    ciphertext = []
    plaintext_list = list(plaintext)
    encrypt(ciphertext, plaintext_list)
    print(plaintext_list)
    print(ciphertext)


main()

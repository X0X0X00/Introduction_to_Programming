"""
mkp
week 5
example 2
"""

def main():
    print('This program encrypts lower cases only. Don not use space.')
    plaintext = input("Enter string to encrypt: ")
    key = 3
    ciphertext = ""
    for ch in plaintext:
        num_val = ord(ch) - 97
        new_ch_val = (num_val + key) % 26 + 97
        new_ch = chr(new_ch_val)
        ciphertext = ciphertext + new_ch
    print(ciphertext)

main()

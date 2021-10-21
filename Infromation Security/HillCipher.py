#!/usr/bin/env python
# coding: utf-8

# In[15]:


key_matrix = [[0] * 2 for i in range(2)]
inverse_key_matrix = [[0] * 2 for i in range(2)]


def get_key_matrix(key):
    k = 0
    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = ord(key[k]) % 65
            k += 1


def get_inverse_key_matrix():
    global inverse_key_matrix
    det = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % 26
    for i in range(26):
        if (det * i) % 26 == 1:
            det = i
            break
    inverse_key_matrix = [[key_matrix[1][1] * det % 26, -1 * key_matrix[0][1] * det % 26],
                          [-1 * key_matrix[1][0] * det % 26, key_matrix[0][0] * det % 26]]


def encrypt(msg):
    result = ""
    msg = msg.replace(" ", "")
    if len(msg) % 2 != 0:
        msg += "0"

    k = 0
    while k < len(msg):
        vector = [ord(msg[k]) - ord('A') + 1, ord(msg[k + 1]) - ord('A') + 1]
        k += 2
        vector = [(key_matrix[0][0] * vector[0] + key_matrix[0][1] * vector[1]) % 26,
                  (key_matrix[1][0] * vector[0] + key_matrix[1][1] * vector[1]) % 26]
        cipher_text = [chr(vector[i] + ord('A') - 1) for i in range(2)]
        result += ''.join(cipher_text)
    return result


def decrypt(msg):
    result = ""
    if len(msg) % 2 != 0:
        msg += "0"
    k = 0
    while k < len(msg):
        vector = [ord(msg[k]) - ord('A') + 1, ord(msg[k + 1]) - ord('A') + 1]
        k += 2
        vector = [(inverse_key_matrix[0][0] * vector[0] + inverse_key_matrix[0][1] * vector[1]) % 26,
                  (inverse_key_matrix[1][0] * vector[0] + inverse_key_matrix[1][1] * vector[1]) % 26]
        cipher_text = [chr(vector[i] + ord('A') - 1) for i in range(2)]
        result += ''.join(cipher_text)

    return result


def main():
    key = 'BBBC'
    get_key_matrix(key)
    get_inverse_key_matrix()

    while True:
        print("\nMENU: \n1. Encode \n2. Decode \n3. Exit")
        choice = input("\nEnter your choice : ")

        if choice == '1':
            msg = input("Enter the message : ")
            encode = encrypt(msg.upper())
            print("Encoded message",encode)

        elif choice == '2':
            msg = input("Enter the encoded-message : ")
            decode = decrypt(msg.upper())
            print("Decoded message",decode)

        elif choice == '3':
            break

        else:
            print("\nInvalid Choice! Please enter 1 or 2 or 3.")


if __name__ == '__main__':
    main()


# In[ ]:





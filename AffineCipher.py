#!/usr/bin/env python
# coding: utf-8

# In[9]:


def encrypt(a, b, msg):
    result = ""
    for char in msg:
        if char.isupper():
            if char != ' ':
                x = ord(char) - 65
                result += chr((a * x + b) % 26 + 65)
            else:
                result += char
        else:
            if char != ' ':
                x = ord(char) - 97
                result += chr((a * x + b) % 26 + 97)
            else:
                result += char
    return result


def decrypt(a, b, msg):
    a_inverse = 0
    result = ""
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break

    for char in msg:
        if char.isupper():
            if char != " ":
                result += chr((a_inverse * (ord(char) + 65 - b) % 26) + 65)
            else:
                result += char
        else:
            if char != " ":
                result += chr((a_inverse * (ord(char) + 97 - b) % 26) + 97)
            else:
                result += char

    return result


def main():
    a = 5
    b = 7
    while True:
        print("\nMENU: \n1. Encode \n2. Decode \n3. Exit")
        choice = input("\nEnter your choice : ")

        if choice == '1':
            msg = input("Enter the message : ")
            encode = encrypt(a, b, msg)
            print("Encoded message",encode)

        elif choice == '2':
            msg = input("Enter the encoded-message : ")
            decode = decrypt(a, b, msg)
            print("Decoded message",decode)

        elif choice == '3':
            break

        else:
            print("\nInvalid Choice! Please enter 1 or 2 or 3.")


if __name__ == '__main__':
    main()


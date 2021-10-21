#!/usr/bin/env python
# coding: utf-8

# In[12]:


def encrypt(msg, key):
    result = ""

    for char in msg:
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    return result


def decrypt(msg, key):
    return encrypt(msg, 26-key)


def main():
    key = int(input("Enter Key: "))
    while True:
        print("\nMENU: \n1. Encode \n2. Decode \n3. Exit")
        choice = input("\nEnter your choice : ")

        if choice == '1':
            msg = input("Enter the message : ")
            encode = encrypt(msg, key)
            print("Encoded message",encode)

        elif choice == '2':
            msg = input("Enter the encoded-message : ")
            decode = decrypt(msg, key)
            print("Decoded message",decode)

        elif choice == '3':
            break

        else:
            print("\nInvalid Choice! Please enter 1 or 2 or 3.")


if __name__ == '__main__':
    main()


# In[ ]:





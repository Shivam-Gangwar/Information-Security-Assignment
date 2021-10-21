#!/usr/bin/env python
# coding: utf-8

# In[25]:


import operator
Text = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
def get_key(iteration: int, ch: str) -> int:
    return ord(ch) - ord(Text[iteration])


def decryption(message, key):
    decode = ""
    for ch in message:
        if ch.isspace():
            decode += " "
        else:
            decode += chr(((ord(ch) - ord('A') - key) % 26) + ord('A'))
    return decode


def freq_attack(message: str) -> str:
    frequency = {}
    for ch in message:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    sorted_x = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(20):
        if i == len(sorted_x):
            break
        key = get_key(i, sorted_x[i][0])
        print(decryption(message, key))

    

if __name__=='__main__':
    words = 'B TJNQMF NFTTBHF'
    freq_attack(words)


# In[ ]:





# In[ ]:





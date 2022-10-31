#variable containing the alphabet
x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#defining the function main
def main():
    #getting the phrase from the user
    message = input('enter message:\n')
    #getting the key from the user
    key = input('enter your key:\n')
    #getting the mode from the user to encrypt or decrypt
    mode = input('encrypt or decrypt\n')
   #encrypting or decrypting using function
    if mode == 'encrypt':
       cipher = encryptMessage(message, key)
    elif mode == 'decrypt':
       cipher = decryptMessage(message, key)
    #printing the new phrase
    print(cipher)

#
def encryptMessage (messages, keys):  
    return cipherMessage(messages, keys, 'encrypt')


## def decryptMessage(keys,messages):
##     return cipherMessage(keys, messages, 'decrypt')
def decryptMessage(messages, keys):
    return cipherMessage(messages, keys, 'decrypt')


## def cipherMessage (keys, messages, mode):
def cipherMessage (messages, keys, mode):
    cipher = []
    k_index = 0
    key = keys.upper()
    for i in messages:
        text = x.find(i.upper())
        ## if text != -1:
        if mode == 'encrypt':
             text += x.find(key[k_index])
             key += i.upper()  # add current char to keystream

        elif mode == 'decrypt':
             text -= x.find(key[k_index])
             key += x[text]  # add current char to keystream
        text %= len(x)
        ## k_index +
        k_index += 1
        ## if k_index == len(key):
        ##     k_index = 0
        ## else:
        cipher.append(x[text])
    return ''.join(cipher)

if __name__ == "__main__":
    main()
    
def caesar_encryp(key, text):
    if key > 26:
        key = key % 26
    ans = ''
    for symb in text:
        if ord(symb) >= ord('a') and ord(symb) <= ord('z'):
            if ord(symb) + key > ord('z'):
                ans += chr((ord(symb) + key) - 26)
            else:
                ans += chr(ord(symb) + key)
        elif ord(symb) >= ord('A') and ord(symb) <= ord('Z'):
            if ord(symb) + key > ord('Z'):
                ans += chr((ord(symb) + key) - 26)
            else:
                ans += chr(ord(symb) + key)
        else:
            ans += symb
    return ans

def correct_key(key):
    new_key = ""
    for symb in key.upper():
        if ord(symb) >= 65 and ord(symb) <= 90:
            new_key += symb
    return new_key

def correct_len_key(text, key):
    len_text = len(text)
    len_key = len(key)
    if len_key < len_text:
        key += key * ((len_text - len_key) // len_key) + key[:((len_text - len_key) % len_key)]
    elif len_key > len_text:
        key = key[:len_text] 
    return key

def vigenere_encryp(text, key):
    ans = ""
    for symb in range(len(text)):
        if ord(text[symb]) >= 65 and ord(text[symb]) <= 90:
            ans += chr((ord(text[symb]) + ord(key[symb]) - 130) % 26 + 65)
        else:
            ans += text[symb]
    return ans

def verman_encryp(key,text):
    ans = ""
    for symb in range(len(text)):
        ans += str(chr(((ord(text[symb]) - 32) ^ (ord(key[symb]) - 32) + 32) % 128))
    return ans

def caesar_decod(key,text):
    if key > 26:
        key = key % 26
    ans=''
    for symb in text:
        if ord(symb) >= ord('a') and ord(symb) <= ord('z'):
            if ord(symb) - key < ord('a'):
                ans += chr((ord(symb) - key) + 26)
            else:
                ans += chr(ord(symb) - key)
        elif ord(symb) >= ord('A') and ord(symb) <= ord('Z'):
            if ord(symb) - key < ord('A'):
                ans += chr((ord(symb) - key) + 26)
            else:
                ans += chr(ord(symb) - key)
        else:
            ans += symb
    return ans

'''
returns an array where the i element is 
the frequency of use of i letter in the text 
'''
def percentage_letters(text):
    perc_letters = [0] * 26
    count = 0
    for simv in text:
        if ord(simv) >= 65 and ord(simv) <= 90:
            perc_letters[ord(simv) - 65] += 1
            count += 1
        if ord(simv) >= 97 and ord(simv) <= 122:
            perc_letters[ord(simv) - 97] += 1 
            count += 1
    for i in range(25):
        if perc_letters[i] > 0:
            perc_letters[i] = perc_letters[i] * 10000 // count
    return perc_letters

'''
returns an array where the i element is the sum of the modulus of 
the difference between the frequency of use of letters in English (list_1) 
and the frequency of use of letters in the text when shifted by i (list_2) 
'''
def inaccuracy(list_1, list_2):
    minn = [0] * 26
    for i in range(26):
        summ = 0
        for j in range(26):
            summ += abs(list_2[j] - list_1[(j + i) % 26])
        minn[i] = summ
    return minn

'''
returns min val of that array (where the i element is the sum of the modulus of 
the difference between the frequency of use of letters in English 
and the frequency of use of letters in the text when shifted by i), 
so return the most likely key
'''
def minn(keys):
    key = 0
    minn = keys[0]
    for i in range(26):
        if keys[i] < minn:
            minn = keys[i]
            key = i
    return key

def vigenere_decon(n, key):
    ans = ""
    for i in range(len(n)):
        if ord(n[i]) >= 65 and ord(n[i]) <= 90:
            ans += chr((ord(n[i]) - ord(key[i])) % 26 + 65)
        else:
            ans += n[i]
    return ans

def opening(path: str):
    file = path.encode("ISO-8859-1")
    text = open(file, 'r', encoding="utf-8").read()
    file.close()
    return text

def enter(strr):
    print("Want to open code with a file? 1 or 0")
    op = input("Enter - ")
    if op == "0":
        print(strr)
        text = input() 
    elif op == "1":
        j = input("Enter the file name - ")
        text = opening(j)
    else:
        print("Incorrect data entered")
    return text

'''
array where the i element is the frequency of use of i letter in English * 100
'''
frequency_alfavit = [817, 149, 278, 425, 1270, 223, 202, 609, 697, 15, 77, 403, 241, 675, 751, 193, 10, 599, 633, 906, 276, 98, 236, 15, 197, 7]   

print("If you want to encrypt, enter - 1, if you want to decrypt-2")
command = input("Enter - ")
if command == "1":
    print("choose an encryption method:")
    print("Caesar Cipher - 1, Vigenere Cipher - 2, Vernam Cipher - 3") 
    cipher = input("Enter - ")
    if cipher == "1":
        key = int(input("Enter the key (it should be a whole number) - "))
        text = enter("Enter the text (from the symbols of the ASCII table) - ")            
        print(caesar_encryp(key, text))
    elif cipher == "2":
        key = input("Enter the key (must contain letters) - ")
        text = enter("Enter the text (from the symbols of the ASCII table) - ").upper() 
        norm_key = correct_key(key)
        key = correct_len_key(text, norm_key)
        print(vigenere_encryp(text, key))
    elif cipher == "3":
        key = input("Enter the key (from 32 symbols of the ASCII table) - ")
        text = enter("Enter the text (from 32 symbols of the ASCII table) - ") 
        norm_key = correct_len_key(text, key)
        print(verman_encryp(norm_key, text)) 
    else:
        print("Incorrect data entered")
elif command == "2":
    print("select decryption method:")
    print("Caesar Cipher - 1, Vigenere Cipher - 2, Vernam Cipher - 3") 
    cipher = input("Enter - ")
    if cipher == "1":
        print("If you have a key, enter - 1, if not - 0")
        is_key = input("Enter - ")
        if is_key == "1":        
            key = int(input("Enter the key (it should be a whole number) - "))
            text = enter("Enter the text (from the symbols of the ASCII table) - ")   
            print(caesar_decod(key, text))
        elif is_key == "0":
            text = enter("Enter the text (from the symbols of the ASCII table) - ")
            l = percentage_letters(text)
            keys = inaccuracy(l, frequency_alfavit)
            lucky_key = minn(keys) 
            print(caesar_decod(lucky_key, text))
        else:
            print("Incorrect data entered") 
            
    elif cipher == "2":
        key = input("Enter the key (must contain letters) - ")
        text = enter("Enter the text (from the symbols of the ASCII table) - ").upper()   
        norm_key = correct_key(key)
        key = correct_len_key(text, norm_key)
        print(vigenere_decon(text, key))
    elif cipher == "3":
        key = input("Enter the key (from 32 symbols of the ASCII table) - ")
        text = enter("Enter the text (from 32 symbols of the ASCII table) - ") 
        norm_key = correct_len_key(text, key)
        print(verman_encryp(norm_key, text)) 
    else:
        print("Incorrect data entered")    
else:
    print("Incorrect data entered") 
    
def cipher(k, n):
    if k > 26:
        k = k % 26
    ans = ''
    for i in n:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            if ord(i) + k > ord('z'):
                ans += chr((ord(i) + k) - 26)
            else:
                ans += chr(ord(i) + k)
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            if ord(i) + k > ord('Z'):
                ans += chr((ord(i) + k) - 26)
            else:
                ans += chr(ord(i) + k)
        else:
            ans += i
    return ans

def correct(s):
    ss = ""
    for i in s.upper():
        if ord(i) >= 65 and ord(i) <= 90:
            ss += i
    return ss

def key(n, s):
    len_n = len(n)
    len_s = len(s)
    if len_s < len_n:
        s += s * ((len_n - len_s) // len_s) + s[:((len_n - len_s) % len_s)]
    elif len_s > len_n:
        s = s[:len_n] 
    return s

def conect(n, k):
    ans = ""
    for i in range(len(n)):
        if ord(n[i]) >= 65 and ord(n[i]) <= 90:
            ans += chr((ord(n[i]) + ord(k[i]) - 130) % 26 + 65)
        else:
            ans += n[i]
    return ans

def verman(s,n):
    ans = ""
    for i in range(len(n)):
        ans += str(chr(((ord(n[i]) - 32) ^ (ord(s[i]) - 32) + 32) % 128))
    return ans

def decipher(k,n):
    if k > 26:
        k = k % 26
    ans=''
    for i in n:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            if ord(i) - k < ord('a'):
                ans += chr((ord(i) - k) + 26)
            else:
                ans += chr(ord(i) - k)
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            if ord(i) - k < ord('A'):
                ans += chr((ord(i) - k) + 26)
            else:
                ans += chr(ord(i) - k)
        else:
            ans += i
    return ans

def frequency_word(n):
    s_list = [0] * 26
    count = 0
    for simv in n:
        if ord(simv) >= 65 and ord(simv) <= 90:
            s_list[ord(simv) - 65] += 1
            count += 1
        if ord(simv) >= 97 and ord(simv) <= 122:
            s_list[ord(simv) - 97] += 1 
            count += 1
    for i in range(25):
        if s_list[i] > 0:
            s_list[i] = s_list[i] * 10000 // count
    return s_list

def delta(l, a):
    minn = [0] * 26
    for k in range(26):
        summ = 0
        for i in range(26):
            summ += abs(a[i] - l[(i + k) % 26])
        minn[k] = summ
    return minn

def minn(key):
    k = 0
    minn = key[0]
    for i in range(26):
        if key[i] < minn:
            minn = key[i]
            k = i
    return k

def deconect(n, k):
    ans = ""
    for i in range(len(n)):
        if ord(n[i]) >= 65 and ord(n[i]) <= 90:
            ans += chr((ord(n[i]) - ord(k[i])) % 26 + 65)
        else:
            ans += n[i]
    return ans

def opening(path: str):
    file = path.encode("ISO-8859-1")
    text = open(file, 'r', encoding="utf-8").read()
    return text

frequency_alfavit = [817, 149, 278, 425, 1270, 223, 202, 609, 697, 15, 77, 403, 241, 675, 751, 193, 10, 599, 633, 906, 276, 98, 236, 15, 197, 7]   

print("If you want to encrypt, enter - 1, if you want to decrypt-2")
command = input("Enter - ")
if command == "1":
    print("choose an encryption method:")
    print("Caesar Cipher - 1, Vigenere Cipher - 2, Vernam Cipher - 3") 
    shifr = input("Enter - ")
    if shifr == "1":
        k = int(input("Enter the key (it should be a whole number) - "))
        print("Want to open code with a file? 1 or 0")
        op = input("Enter - ")
        if op == "0":
            n = input("Enter the text (from the symbols of the ASCII table) - ") 
        elif op == "1":
            j = input("Enter the file name - ")
            n = opening(j)
        else:
            print("Incorrect data entered")
            
        print(cipher(k, n))
    elif shifr == "2":
        k = input("Enter the key (must contain letters) - ")
        print("Want to open code with a file? 1 or 0")
        op = input("Enter - ")
        if op == "0":
            n = input("Enter the text (from the symbols of the ASCII table) - ") 
        elif op == "1":
            j = input("Enter the file name - ")
            n = opening(j)
        else:
            print("Incorrect data entered")    
            
        ss = correct(k)
        n = n.upper()
        k = key(n, ss)
        sh = (conect(n, k))
        print(sh)
    elif shifr == "3":
        k = input("Enter the key (from 32 symbols of the ASCII table) - ")
        print("Want to open code with a file? 1 or 0")
        op = input("Enter - ")
        if op == "0":
            n = input("Enter the text (from 32 symbols of the ASCII table) - ")
        elif op == "1":
            j = input("Enter the file name - ")
            n = opening(j)
        else:
            print("Incorrect data entered")  
            
        ss = key(n, k)
        sh = (verman(ss,n))
        print(sh) 
    else:
        print("Incorrect data entered")
elif command == "2":
    print("select decryption method:")
    print("Caesar Cipher - 1, Vigenere Cipher - 2, Vernam Cipher - 3") 
    shifr = input("Enter - ")
    if shifr == "1":
        print("If you have a key, enter - 1, if not - 0")
        kk = input("Enter - ")
        if kk == "1":        
            k = int(input("Enter the key (it should be a whole number) - "))
            print("Want to open code with a file? 1 or 0")
            op = input("Enter - ")
            if op == "0":
                n = input("Enter the text (from the symbols of the ASCII table) - ") 
            elif op == "1":
                j = input("Enter the file name - ")
                n = opening(j)
            else:
                print("Incorrect data entered") 
                
            print(decipher(k, n))
        elif kk == "0":
            print("Want to open code with a file? 1 or 0")
            op = input("Enter - ")
            if op == "0":
                n = input("Enter the text (from the symbols of the ASCII table) - ") 
            elif op == "1":
                j = input("Enter the file name - ")
                n = opening(j)
            else:
                print("Incorrect data entered") 
                
            l = frequency_word(n)
            keys = delta(l, frequency_alfavit)
            key = minn(keys) 
            print(decipher(key, n))
        else:
            print("Incorrect data entered") 
            
    elif shifr == "2":
        k = input("Enter the key (must contain letters) - ")
        print("Want to open code with a file? 1 or 0")
        op = input("Enter - ")
        if op == "0":
            n = input("Enter the text (from the symbols of the ASCII table) - ") 
        elif op == "1":
            j = input("Enter the file name - ")
            n = opening(j)
        else:
            print("Incorrect data entered")
            
        ss = correct(k)
        n = n.upper()
        k = key(n, ss)
        sh = (deconect(n, k))
        print(sh)
    elif shifr == "3":
        k = input("Enter the key (from 32 symbols of the ASCII table) - ")
        print("Want to open code with a file? 1 or 0")
        op = input("Enter - ")
        if op == "0":
            n = input("Enter the text (from the symbols of the ASCII table) - ") 
        elif op == "1":
            j = input("Enter the file name - ")
            n = opening(j)
        else:
            print("Incorrect data entered")
        
        ss = key(n, k)
        sh = (verman(ss,n))
        print(sh) 
    else:
        print("Incorrect data entered")    
else:
    print("Incorrect data entered") 
    
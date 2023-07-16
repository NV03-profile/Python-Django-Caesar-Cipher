text=input("Enter text: ")
key=int(input("Enter a number for shifting: "))
print("Text to be encrypted:",text)
def encrypt(text,key):
    ct=""
    for char in text:
        if char.isalpha():
            s=ord(char)+key                #encryption=(x+n)mod26
            if char.isupper():
                if s>ord('Z'):
                    s=s-26
                enc=chr(s)
            else:
                #if char.islower():
                if s>ord('z'):
                    s=s-26
                enc=chr(s)
            ct=ct+enc
        else:
            ct=ct+char
    return ct
c=encrypt(text,key)
print("Encrypted Text:",c)

def decrypt(ct,key):
    pt=""
    for char in ct:
        if char.isalpha():
            s=ord(char)-key                #decryption=(x-n)mod26
            if char.isupper():
                if s<ord('A'):
                    s=s+26
                dec=chr(s)
            else:
                if s<ord('a'):
                    s=s+26
                dec=chr(s)
            pt=pt+dec
        else:
            pt=pt+char
    return pt
d=decrypt(c,key)
#print("Decrypted Text:",d)

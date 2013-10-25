SHIFT=1

def encrypt( raw ):
    ret = ''
    for char in raw:
        ret+=chr( ord(char)+SHIFT )
    return ret

def decrypt( raw ):
    ret = ''
    for char in raw:
        ret+=chr( ord(char)-SHIFT )
    return ret
   
if __name__=="__main__":
    raw = input("input : ")
    encrypted = encrypt( raw )
    print("encrypted : " + encrypted)
   
    decrypted = decrypt( encrypted )
    print("decrypted : " + decrypted)
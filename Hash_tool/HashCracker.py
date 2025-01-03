
import hashlib

print("[1] md5\n[2] sha1\n[3] sha224\n[4] sha256\n[5] sha384\n[6] sha512\n[7] sha3_224\n[8] sha3_256\n[9] sha3_384\n[10] sha3_512\n")

chooseNum = int(input("Choose hash type: "))
i = input("Enter hash: ")

hashType = [hashlib.md5, hashlib.sha1, hashlib.sha224, hashlib.sha256, 
            hashlib.sha384, hashlib.sha512, hashlib.sha3_224, hashlib.sha3_256, 
            hashlib.sha3_384, hashlib.sha3_512]

# Main function is working but i need to give it a way to chose what type of hash it is.
with open("passwordList.txt", "r") as file:
    for line in file.readlines():
        word = line.split()
        h = hashType[chooseNum - 1](word[0].encode('utf-8')).hexdigest()
        if h == i:
            print(f"Password: {line}")
            break
        else:
            pass

# Example of hashed password
# master = fc613b4dfd6736a7bd268c8a0e74ed0d1c04a959f59dd74ef2874983fd443fc9

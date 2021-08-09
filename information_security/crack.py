import hashlib

hash = "3c2223212b6dde34bcf86b580bdb71d4"

f = open("pw.txt", "r")
lst = f.read().split()

for i in lst:
    md5Hash = hashlib.md5(i.encode())
    if(md5Hash.hexdigest() == hash):
        print(i)
        break

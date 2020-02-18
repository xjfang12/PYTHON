import hashlib
import sys
aaa = sys.argv[1]


def Calcsha1(filepath):
    with open(filepath, 'rb') as f:
        sha1obj = hashlib.md5()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        print(hash)
        return hash
    print(f)


Calcsha1(aaa)

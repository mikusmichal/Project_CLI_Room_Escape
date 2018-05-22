import hashlib
import sys

m = hashlib.sha256()
m.update(bytearray(sys.argv[1], 'utf8'))
print(m.digest())

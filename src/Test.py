import hashlib
import base64

str1 = b'ashwin'
str2 = b'ashwin'


hash = hashlib.sha512()
hash.update(str1)
md1 = hash.hexdigest()
hash.update(str2)
md2 = hash.hexdigest()

print(md1)
print(md2)

from crypto import Crypto

ct = Crypto()

result, table = ct.encrypt_file("test.txt")

print(result)

result = ct.decrypt_file("test.txt", table)

print(result)
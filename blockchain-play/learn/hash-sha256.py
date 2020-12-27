from hashlib import sha256

data = b"Some variable length data"
print(sha256(data).hexdigest())
data = b"Some variable length data2"
print(sha256(data).hexdigest())

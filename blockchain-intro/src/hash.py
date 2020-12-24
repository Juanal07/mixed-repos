from hashlib import sha256

data = b"Some variable length data"  # la b antes del string implica que se guardara como una variable tipo byte no str
print(sha256(data).hexdigest())
data = b"Some variable length data2"
print(sha256(data).hexdigest())

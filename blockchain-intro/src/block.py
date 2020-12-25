import time
from hashlib import sha256
import json
from json.encoder import JSONEncoder


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        blockJSONData = json.dumps(self, indent=4, cls=BlockEncoder)
        return sha256(blockJSONData.encode()).hexdigest()

    def __str__(self):
        """
        toString method of the object Block
        """
        return 'Index: ' + str(self.index) + '\n' \
               + 'Transactions: ' + ''.join(str(e) for e in self.transactions) + '\n' \
               + 'Time: ' + time.ctime(self.timestamp) + '\n' \
               + 'Previous_hash: ' + str(self.previous_hash) + '\n' \
               + 'Nonce: ' + str(self.nonce) + '\n' \
               + 'Hash: ' + str(self.hash)


class BlockEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

    # https://pynative.com/make-python-class-json-serializable/

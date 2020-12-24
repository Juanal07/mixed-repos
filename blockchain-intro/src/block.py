from hashlib import sha256
import json


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return 'Index: ' + str(self.index) + '\n' \
            + 'Transactions: ' + str(self.transactions) + '\n' \
            + 'Time: ' + str(self.timestamp) + '\n' \
            + 'previous_hash: ' + str(self.previous_hash) + '\n' \
            + 'nonce: ' + str(self.nonce)



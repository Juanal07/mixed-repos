import bitcoin
import ecdsa
from bitcoin import privtoaddr


class Wallet:
    def __init__(self):
        random_hex = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1).to_string().hex()
        self.private_key = bitcoin.encode_privkey(bitcoin.decode_privkey(random_hex, 'hex'), 'wif_compressed')
        self.public_key = privtoaddr(random_hex)

    def amount(self, blockchain):
        amount = 0
        for block in blockchain.chain:
            for tr in block.transactions:
                if tr.recipient == self.public_key:
                    amount += tr.amount
                if tr.sender == self.public_key:
                    amount -= tr.amount
        return amount

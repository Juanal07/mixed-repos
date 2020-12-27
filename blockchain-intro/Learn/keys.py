import bitcoin as bitcoin
from bitcoin import pubtoaddr, privtopub, privtoaddr
import ecdsa

priv_hex = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1).to_string().hex()
wif = bitcoin.encode_privkey(bitcoin.decode_privkey(priv_hex, 'hex'), 'wif_compressed')
print('Private key (hex): ', priv_hex)
print('Private address: ', wif)

pub_hex = bitcoin.privtopub(priv_hex)
print('Public key (hex): ', pub_hex)
print('Public address: ', privtoaddr(priv_hex))


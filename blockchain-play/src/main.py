from blockchain import Blockchain
from transaction import Transaction
from wallet import Wallet


def main():
    blockchain = Blockchain()
    wallet1 = Wallet()
    wallet2 = Wallet()

    tri1 = Transaction('COINBASE', wallet2.public_key, 50)
    tri2 = Transaction('COINBASE', wallet1.public_key, 50)
    blockchain.add_new_transaction(tri1)
    blockchain.add_new_transaction(tri2)
    blockchain.mine()

    tr = Transaction(wallet1.public_key, wallet2.public_key, 3)
    tr5 = Transaction(wallet1.public_key, wallet2.public_key, 6)
    tr2 = Transaction('Pedro', 'Lucas', 2)
    tr3 = Transaction('Lucas', 'Antonio', 1)
    tr4 = Transaction('Juan', 'Lucas', 3)

    blockchain.add_new_transaction(tr2)
    blockchain.add_new_transaction(tr5)
    blockchain.add_new_transaction(tr)
    blockchain.mine()
    blockchain.add_new_transaction(tr3)
    blockchain.mine()
    print(blockchain.chain[0])
    print('-----------------------')
    print(blockchain.chain[1])
    print('-----------------------')
    print(blockchain.last_block)
    print('-----------------------')
    blockchain.add_new_transaction(tr4)
    blockchain.mine()
    print(blockchain.last_block)
    print('-----------------------')
    print('Saldo wallet1: ', wallet1.amount(blockchain))
    print('Saldo wallet2: ', wallet2.amount(blockchain))


if __name__ == '__main__':
    main()

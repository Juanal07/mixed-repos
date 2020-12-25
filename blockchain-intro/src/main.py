from blockchain import Blockchain
from transaction import Transaction


def main():
    blockchain = Blockchain()

    tr = Transaction('Juan', 'Antonio', 3)
    tr2 = Transaction('Pedro', 'Lucas', 2)
    tr3 = Transaction('Lucas', 'Antonio', 1)

    blockchain.add_new_transaction(tr)
    blockchain.add_new_transaction(tr2)
    blockchain.mine()
    blockchain.add_new_transaction(tr3)
    blockchain.mine()
    print(blockchain.chain[0])
    print(blockchain.chain[1])
    print(blockchain.last_block)


if __name__ == '__main__':
    main()

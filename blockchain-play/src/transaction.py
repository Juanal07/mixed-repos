import time


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.timestamp = time.time()
        self.amount = amount

    def validate(self):
        """
        Checks if a transaction is valid
        :return: <bool> True if it is valid, False if not.
        """
        # Prevent stealing by creating negative transactions
        if self.amount < 0:
            return False

        return True

    def __str__(self):
        """
        toString method of the object Transaction
        """
        return 'Sender: ' + str(self.sender) + ', ' \
               + 'Amount: ' + str(self.amount) + ', ' \
               + 'Recipient: ' + str(self.recipient) + ', ' \
               + 'Time: ' + time.ctime(self.timestamp)

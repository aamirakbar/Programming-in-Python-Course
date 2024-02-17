import random

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.reciever = receiver
        self.amount = amount

    def __str__(self):
        return f"Transaction from {self.sender} to {self.receiver} of {self.amount}"
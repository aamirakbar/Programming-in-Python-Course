from blockchain import Blockchain
from transaction import Transaction

# Create blockchain
my_blockchain = Blockchain()

# Adding blocks with transactions
transactions1 = Transaction("Babar", "Virat", 5000)
my_blockchain.add_block(transactions1)

transactions2 = Transaction("Shami", "Shaheen", 10000)
my_blockchain.add_block(transactions2)

transactions3 = Transaction("Ronaldo", "Messi", 500)
my_blockchain.add_block(transactions3)

# Displaying the original blockchain
print("Original Blockchain:")
my_blockchain.display_chain()

# Attempting to alter a block
block_to_alter = my_blockchain.get_block(2)
if block_to_alter:
    print("\nAttempting to alter the third block...\n")
    trans_to_alter = block_to_alter.get_transaction()
    trans_to_alter.sender = "Alter Sender"
    trans_to_alter.reciever = "Alter Reciever"
    trans_to_alter.amount = 999

# Displaying the altered blockchain
print("\nAltered Blockchain:")
my_blockchain.verify_blockchain()
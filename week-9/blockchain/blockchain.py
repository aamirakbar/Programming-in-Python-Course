from block import Block

class Blockchain:
    def __init__(self):
        self.__chain = [
                Block(transaction="Genesis Block")
            ]

    def add_block(self, transactions):
        previous_block = self.__chain[-1]
        new_block = Block(transactions, previous_block.get_hash())
        self.__chain.append(new_block)
        
    def get_block(self, index):
        return self.__chain[index]

    def display_chain(self):
        for block in self.__chain:
            print(block)
            print("----------")
            
    def verify_blockchain(self):
        for index, block in enumerate(self.__chain):
            if block.get_hash() == block.calculate_block_hash():
                print(f"Block at index {index} is not tempered")
            else:
                print(f"Block at index {index} is tempered")

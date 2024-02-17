import hashlib
import datetime

class Block:
    def __init__(self, transaction, previous_hash=None):
        self.__timestamp = datetime.datetime.now()
        self.__transaction = transaction
        self.__previous_hash = previous_hash
        self.__hash = self.calculate_block_hash()

    def calculate_block_hash(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.__timestamp).encode('utf-8') +
            str(self.__transaction).encode('utf-8') +
            (str(self.__previous_hash) if self.__previous_hash else '').encode('utf-8')
        )
        return sha.hexdigest()
    
    def get_hash(self):
        return self.__hash
    
    def get_transaction(self):
        return self.__transaction

    def __str__(self):
        return f"Block Hash: {self.__hash}\n" +\
                f"Timestamp: {self.__timestamp}\n" +\
                f"Transaction: {self.__transaction}\n" +\
                f"Previous Hash: {self.__previous_hash}\n"
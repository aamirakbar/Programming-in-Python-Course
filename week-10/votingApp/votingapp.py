from blockchain.blockchain import Blockchain
import json

class VotingApp:
    def __init__(self):
        self.blockchain = Blockchain()
        
        with open("voters_list.json", "r") as file:
            self.voters_list = json.load(file)
            
    def cast_vote(self, candidate):
        self.blockchain.add_block(candidate)
        
    def result_count(self, cadidate_result):
        for i in range(1, self.blockchain.get_length()):
            block = self.blockchain.get_block(i)
            cadidate_result[block.get_transaction()] += 1
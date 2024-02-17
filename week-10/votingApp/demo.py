from votingapp import VotingApp
import random
from termcolor import colored

voting_app = VotingApp()

VOTERS = ["11111-22222-3", "66667-77778-3", "11111-22222-0", "43534-345345-7", "12345-67890-9"]

CANDIDATES = ["candidate-a", "candidate-b", "candidate-c"]

for cnic in VOTERS:
    if cnic in voting_app.voters_list:
        candidate = random.choice(CANDIDATES)
        voting_app.cast_vote(candidate)
        print(colored("vote casted successfully", "green"))
    else:
        print(colored("voter is not registered", "red"))
        
print("\n Election Result:")

cadidate_result = {"candidate-a":0, "candidate-b":0, "candidate-c":0}

voting_app.result_count(cadidate_result)

print(colored(cadidate_result, "yellow"))
from  hidden_markov_model import HiddenMarkovModel
from hmm_trainer import HMMTrainer

start_probs = {
        "rock_loving" : 0.5,
        "paper_loving" : 0.25,
        "scissor_loving" : 0.25,
        }

transition_probs = {
    "rock_loving" : {
        "rock_loving" : 0.6,
        "paper_loving" : 0.3,
        "scissor_loving" : 0.1
        },
    "paper_loving" : {
        "rock_loving" : 0.1,
        "paper_loving" : 0.6,
        "scissor_loving" : 0.3
        },
    "scissor_loving" : {
        "rock_loving" : 0.3,
        "paper_loving" : 0.1,
        "scissor_loving" : 0.6
        }
    }

emission_probs = {
    "rock_loving" : {
        "rock": 0.6,
        "paper": 0.2,
        "scissor": 0.2
        },
    "paper_loving" : {
        "rock" : 0.2,
        "paper" : 0.7,
        "scissor" : 0.1
        },
    "scissor_loving" : {
        "rock": 0.1,
        "paper": 0.1,
        "scissor": 0.8
        }
    }

player = HiddenMarkovModel(start_probs,transition_probs,emission_probs)

trainer = HMMTrainer(3)
alphabet = ["rock","paper","scissor"]
random_player = trainer.random_hmm(alphabet)

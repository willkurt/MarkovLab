"""

HMMTrainer

Uses EM to train a hmm for a given set of training data

"""
from tools import gen_dist
from hidden_markov_model import HiddenMarkovModel

class HMMTrainer:

    # must pass in the cardinality (number of hidden states) of the HMM
    # your expecting to train.
    # There are ways around that, but our basic training makes the
    # assumption that the cardinality is known in advance
    # we wont' assume an alphabet since this could be infered from the training data
    def __init__(self,card):
        self.card = card
        self.states = map(lambda x: str(x),xrange(0,card))

    # here we do actually need an alphabet so that we can generate
    # a random set of emission probabilities
    def random_hmm(self,alphabet):
        alpha_size = len(alphabet)
        Pi = dict(zip(self.states,gen_dist(self.card)))
        A = dict(zip(self.states,map(lambda x: dict(zip(self.states,gen_dist(self.card))),xrange(0,self.card))))
        B = dict(zip(self.states,map(lambda x: dict(zip(alphabet,gen_dist(alpha_size))),xrange(0,self.card))))
        hmm = HiddenMarkovModel(Pi,A,B)
        return(hmm)
                 

    
    # the meat of this class
    # uses EM to train an optimal HMM
    # given a corpus of training 
    # examples
    def train(self,corpus):
        pass

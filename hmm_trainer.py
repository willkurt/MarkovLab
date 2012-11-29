"""

HMMTrainer

Uses EM to train a hmm for a given set of training data

"""


from hidden_markov_model import HiddenMarkovModel

class HMMTrainer:

    # must pass in the cardinality (number of hidden states) of the HMM
    # your expecting to train.
    # There are ways around that, but our basic training makes the
    # assumption that the cardinality is known in advance
    # we wont' assume an alphabet since this could be infered from the training data
    def __init__(self,card):
        self.card = card

    # here we do actually need an alphabet so that we can generate
    # a random 
    def random_hmm(self,alphabet):
        pass
    
    # the meat of this class
    # uses EM to train an optimal HMM
    # given a corpus of training 
    # examples
    def train(self,corpus):
        pass

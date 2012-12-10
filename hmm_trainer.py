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
    # does only one pass over the corpus
    # rather than traning to convergence
    def train(self,model,corpus):
        states = model.A.keys()
        symbols = model.B.values()
        for obs in corpus:
            #re-estimate the initial probs
            Pi = {}
            A = {}
            B = {}
            for state in states:
                A[state] = {}
                B[state] = {}
            for state in states:
                #update starting prob
                Pi[state] = model.gamma(obs,1,state)
                #update transisition probs
                for j in states:
                    #get to use this twice
                    #as the num in the transition prob
                    #and the dom in the emission prob
                    expected_i_to_j = 0 
                    expected_transitions = 0
                    for t in xrange(1,len(obs)+1):
                        expected_i_to_j += model.rho(obs,t,state,j)
                        expected_transitions += model.gamma(obs,t,state)
                    A[state][j] = expected_i_to_j/expected_transitions
                    #NOTE STILL NEED TO TRAIN SYMBOL EMISSONS
        return HiddenMarkovModel(Pi,A,model.B) #model B is just a place holder
                    
                
            

            

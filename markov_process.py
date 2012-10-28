"""
MarkovProcess

Create and simulate running through a MarkovProcess with known parameters

The output can then be used to inspect the performance of training and HMM


"""
from tools import prs

class MarkovProcess:
    
    """
    Using Variables from 'Foundations of Statistical NLP' pp. 324
    S = set of states 
    K = output alphabet
    Pi = initial state probabilities
    A = transition probabilities
    B = emission probabilities
    """
    def __init__(self,Pi,A,B):
        self.Pi = Pi #simpy dict of start valid start states and their probability
        self.A = A # dict of dicts 
        # still need to do 'B' but might actaully be
        self.B = B

    """ generates a sequence of characters based on the input """
    def run(self,n,debug=False):
        chain = []
        current_state = prs(self.Pi)
        for i in xrange(0,n):
            if debug:
                print(current_state)
            #emit
            emitted = prs(self.B[current_state])
            chain.append(emitted)
            #move
            current_state = prs(self.A[current_state])
        return " ".join(chain)
        
            
            
    

"""
HiddenMarkovModel

Creates a basic hidden markov model
can run a simulation
should eventually predict likely hood of Os
and predict likely S to Os

"""
from tools import prs

class HiddenMarkovModel:
    
    """
    NOTE: refactor these so that they are sensible
          rather than technical
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
        return chain
        
            
            
    
    """
    Given a set O of outcomes 
    how likely is it that it was
    generated by this model?
    """
    def likelihood_alpha(self, outputs):
        t = len(outcomes)+1
        return self.alpha(outputs,t)

    def likelihood_beta(self, outputs):
        t = len(outcomes)+1
        total = 0
        for s in self.A.keys():
            total += self.Pi[s]*self.beta(outpus,1,s)
        return total

    # the forward procedure which uses
    # dynamic programming to calculate 
    # the probability of seeing a sequence
    # of observences
    def alpha(self,outputs,t,state=False):
        trellis = {}
        # initialize with starting probs
        for s in self.A.keys():
            if self.Pi.has_key(s):
                trellis[s] = [self.Pi[s]]
            else:
                trellis[s] = [0]
        #now update all rows up to n
        for i in xrange(1,t):
            for x in self.A.keys():
                total = 0
                for s in self.A.keys():
                    previous_alpha = trellis[s][i-1]
                    prob_of_transition = self.A[s][x]
                    prob_of_emission = self.B[s][outputs[i-1]]
                    total += previous_alpha*prob_of_transition*prob_of_emission
                trellis[x].append(total)
        total_prob = 0
        if not state:
            for x in self.A.keys():
                total_prob += trellis[x][t-1]
        else:
            total_prob = trellis[state][t-1]
        return total_prob

    # the backwards proceedure which uses
    # memoization to compute the probability
    # of observing a sequence of outputs
    # the meaning of t is not as intuitive here
    # as beta(obs,1) will give the total probability
    def beta(self,outputs,t,state):
        if(t >= len(outputs)+1):
            return 1
        else:
            total = 0
            for s in self.A.keys():
                prob_of_transition = self.A[state][s]
                prob_of_emission = self.B[state][outputs[t-1]]
                total += prob_of_transition*prob_of_emission*self.beta(outputs,t+1,s)
            return total


    """
    Given a set O of outputs
    predict a set of states that
    is most likely to have generated this
    """
    def predict_states(self,outputs):
        pass


 

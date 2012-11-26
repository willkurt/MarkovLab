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
          rather than technical (or maybe not...)
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
    
    #method combining forward and backward computation
    def likelihood(self,outputs,t=1):
        total = 0
        for s in self.A.keys():
            total += self.alpha(outputs,t,s)*self.beta(outputs,t,s)
        return total

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
 

    # used to select maximum of all individual states
    # also i get mathematically what this is doing
    # but it seems more sensible from an implementation
    # standpoint to just select the bigest alpha(t)*beta(t)
    def gamma(self,outputs,t,state):
        # as mentioned earlier this gives you the exact
        # probability at time t
        top = self.alpha(outputs,t,state)*self.beta(outputs,t,state)
        bottom = 0
        for j in self.A.keys():
            bottom += self.alpha(outputs,t,j)*self.beta(outputs,t,j)
        return top/bottom

    def most_likely_state(self, outputs,t):
        state = ""
        max_gamma = 0
        for s in self.A.keys():
            s_gamma = self.gamma(outputs,t,s)
            if(s_gamma > max_gamma):
                max_gamma = s_gamma
                state = s
        return state


    # chooses maximum individual state
    def predict_states_individual(self,outputs):
        states = []
        # plus 1 is the way it is in the Manning et. al.
        # note to self, just double check how to do inclusive range
        for t in xrange(1,len(outputs)+2):
            states.append(self.most_likely_state(outputs,t))
        return states
    
    #assumes a Psi is initlized
    # should add a check to see if prob and state are already computed
    #  (maybe) make private as only the viterbi algorithm should be called directly
    # since it handles the resetting the hash for the objs
    def delta(self,outputs,t,state):
        if  self.deltaProbs[state].has_key(t):
            return self.deltaProbs[state][t]
        elif t == 1:
            if self.Pi.has_key(state):
                return self.Pi[state]
            else:
                return 0
        else:
            #can rewrite this in a more functional way later
            max_prob = 0
            max_state = ''
            for k in self.A.keys():
                val = self.delta(outputs,t-1,k)*self.A[k][state]*self.B[k][outputs[t-2]]
                if val > max_prob:
                    max_prob = val
                    max_state = k
            #store the backtrace
                self.Psi[state][t] = max_state
                self.deltaProbs[state][t] = max_prob
            return max_prob


    #calculate deltas and psi
    #note: i could pull the self.Psi into a ht that's passed around
    def viterbi(self,obs):
        #initialize Psi
        self.Psi = {}
        self.deltaProbs = {}
        for k in self.A.keys():
            self.Psi[k] = {}
            self.deltaProbs[k] = {}
        #now populate psi
        t = len(obs)+1
        for k in self.A.keys():
            self.delta(obs,t,k)
        return self.Psi
            
        
    # chooses maximum combined sequence
    def predict_states_sequence(self,obs):
        # will store all the necessary computations
        self.viterbi(obs)
        t = len(obs)+1
        predicted_states = []
        last_state = ""
        max_prob = 0 
        for k in self.A.keys():
            p = self.delta(obs,t,k)
            if p > max_prob:
                max_prob = p
                last_state = k
        predicted_states.append(last_state)
        while(t > 1):
            last_state = self.Psi[last_state][t]
            predicted_states.append(last_state)
            t -= 1
        predicted_states.reverse()
        return predicted_states

 

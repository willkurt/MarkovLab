#just some useful tools
from random import random


"""
given a dictionary of keys
and probabilities will return
a key at random based on it's probability

note: assuming all sum to 1, eventually will
add scaling/normalization
"""
#proportional random select
def prs(prob_dict):
    keys = prob_dict.keys()
    base_value = 0.0
    target_value = random()
    for k in keys:
        base_value = prob_dict[k] + base_value
        if target_value <= base_value:
            return k
    #in case theres an issue return last
    return keys[-1]

"""
pull this out into more formal tests later
"""

def test_prop_rs(n):
    ex = {'cat':0.2,'dog':0.4,'mouse':0.1,'rabbit':0.30}
    counts = {'cat':0,'dog':0,'mouse':0,'rabbit':0}
    total = n
    for x in xrange(0,total):
        counts[prs(ex)] += 1
        counts_prop = {}
        for k in counts.keys():
            counts_prop[k] = float(counts[k])/total
    print(counts_prop)
    print("original")
    print(ex)
    


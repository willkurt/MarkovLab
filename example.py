from  markov_process import MarkovProcess
#crazy coke machine example

Pi = {"cola_pref":1}

A = {}
A["cola_pref"] = {"cola_pref":0.7,"ice_t_pref":0.3}
A["ice_t_pref"] = {"cola_pref":0.5,"ice_t_pref":0.5}

emission_probs = {}
emission_probs["cola_pref"] = {"cola": 0.6,"ice_t": 0.1,"lem":0.3}
emission_probs["ice_t_pref"] = {"cola":0.1,"ice_t":0.7,"lem":0.2}


example_mp = MarkovProcess(Pi,A,emission_probs)

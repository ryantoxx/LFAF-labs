from grammar import Grammar

class finiteAutomata:
    def __init__(self, Q, Sigma, q0, delta, F):
        self.Q = Q
        self.Sigma = Sigma
        self.q0 = q0
        self.delta = delta
        self.F = F
    
    def if_valid(self,string):
        if string[0] not in self.q0:
            return False

        if string[-1] not in self.F:
            return  False

        for letter in string:
            if letter not in self.sigma:
                return False

        transitions = []
        for letter in string:
            transitions.append(['',letter,''])

        transitions[0][0] = 'S'
        transitions[-1].pop(-1)

        for i in range(len(transitions)-1):
            for state in self.delta:
                if transitions[i][0]==state[0] and transitions[i][1]==state[1]:
                    transitions[i][2]=state[2]
                    transitions[i+1][0]=state[2]
                    break
            if transitions[i][-1]=='':
                return False
        print(f'transitions tried by the automaton{transitions}')

        return True
    
    
    def fa_to_rg(self):
        VN = self.Q
        VT = self.Sigma
        P = {}
        S = self.q0
        
        for i, sigma , j in self.delta:
            if i not in P:
                P[i] = []
            P[i].append(sigma + j)
            
        for state in self.F:
            if state not in P:
                P[state] = []
                
        return Grammar(S, VN, VT, P, self.F)
    
    def fa_det(n):
        delta = {}

        for Q1, S1, Q2 in n.delta:
            if (Q1, S1) not in delta:
                delta[(Q1, S1)] = set()
            delta[(Q1, S1)].add(Q2)

        for (Q1, S) in delta:
            if len(delta[(Q1, S)]) > 1:
                return True

        return False
   
'''   
    def dfa_to_nfa(dfa):
    # Create a new NFA represented as a dictionary of sets
        nfa = {
            'states': dfa.Q,
            'alphabet': dfa.Sigma,
            'start_state': dfa.q0,
            'accept_states': dfa.F,
            'Delta': set()
        }

    # Convert each DFA transition to an NFA transition
        for (q, s), q2 in dfa.delta.items():
            nfa['Delta'].add((q, s, q2))

    # Add epsilon transitions from each state to itself
        for q in nfa['states']:
            nfa['Delta'].add((q, '', q))

        return nfa
'''


     




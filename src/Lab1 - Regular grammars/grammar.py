class Grammar:
    def __init__(self, S, VN, VT, P, F):
        self.S = S
        self.VN = VN
        self.VT = VT
        self.P = P
        self.F = F
        
    def chomsky_hierarchy(self):
        for left, right in self.P.items():
            for production in right:
                if not all((sym in self.VN or sym in self.VT) for sym in production):
                    return "Type 0 - Unrestricted Grammar"
        
        for left, right in self.P.items():
            for production in right:
                if len(production) > len(left):
                    return "Type 2 - Context-Free Grammar"
        
        if all(len(left) == 1 for left in self.P) and all(all(sym in self.VN or sym in self.VT for sym in right) for right in self.P.values()):
            return "Type 1 - Context-Sensitive Grammar"
        
        if all(len(left) == 1 for left in self.P) and all(len(right) <= 2 and all(sym in self.VT for sym in right) for right in self.P.values()):
            return "Type 3 - Regular Grammar"
        
        return "Invalid Grammar"
'''
    def convert_to_fa(self):
            current_state =[]
            for state in self.P['S']:
                current_state.append(state[0])

            symbols = []
            for i in self.P:
                for state in self.P[i]:
                    if state.islower():
                        symbols.append(state)

            func = []
            for i in self.P:
                for state in self.P[i]:
                    j = []
                    j.append(i)
                    j = j + list(state)
                    func.append(j)

            print(f'Transitions: {func}')
            automaton = finiteAutomata(current_state, symbols, self.alf, func)
            return automaton
'''
        


        


class finiteAutomata:
    def __init__(self, delta, F, sigma, q0):
        self.delta = delta
        self.F = F
        self.q0 = q0
        self.sigma = sigma
        

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



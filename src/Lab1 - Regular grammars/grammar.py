import random

from finiteAutomaton import finiteAutomata

class Grammar:
    def __init__(self, V_n, V_t, P, E):
        self.V_n = V_n
        self.V_t = V_t
        self.P = P
        self.alf = E

    def generate_string(self):
        self.list = []
        self.begin='S'
        self.list.append(self.begin)
        while self.begin[-1].isupper():
            j = []
            j.append(self.begin[-1])
            self.begin = self.begin[:-1]+random.choice(self.P[self.begin[-1]])
            if self.begin[-1].isupper():
                j.append(self.begin[-2])
                j.append(self.begin[-1])
            else:
                j.append(self.begin[-1])
            self.list.append(j)
        self.list=self.list[1:]
        print(f'The generated string is: {self.begin}')
        print(f'Transitions that were used: {self.list}')
        return self.begin


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
        

        


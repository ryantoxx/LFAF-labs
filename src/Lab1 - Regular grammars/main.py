from grammar import Grammar
from finiteAutomaton import finiteAutomata

'''
LAB - 1
v_n = ['S','B','L']
v_t = ['a','b', 'c']
p = {
    'S':['aB'],
    'B':['bB','cL'],
    'L':['cL','aS', 'b'],
}
E = v_t

new_grammar = Grammar(v_n ,v_t, p, E)
new_automaton = new_grammar.convert_to_fa()

for i in range(5):
    string = new_grammar.generate_string()
    if new_automaton.if_valid(string):
        print('Successul')
    print()

test_string = 'abcccb'
if new_automaton.if_valid(test_string):
    print('Correct')
else:
    print('Incorrect')
'''

# LAB - 2
Regular_Grammar = Grammar('S', ['S', 'B', 'L'], ['a', 'b', 'c'],
                        { 
                            'S': ['aB'],
                            'B': ['bB', 'cL'],
                            'L': ['cL', 'aS', 'b']
                        }, {'a'})

gr_type = Regular_Grammar.chomsky_hierarchy()
print('---------------------------')
print(gr_type)
print('---------------------------')
'''
Q = {'q0', 'q1', 'q2', 'q3'}
Sigma = {'a', 'b', 'c'}
F = {'q3'}
delta = {
    ('q0', 'a'): {'q1'},
    ('q1', 'b'): {'q2'},
    ('q2', 'c'): {'q3'},
    ('q3', 'a'): {'q1'},
    ('q1', 'b'): {'q1'},
    ('q0', 'b'): {'q2'}
}
'''
Finite_Automaton = finiteAutomata(['q0', 'q1', 'q2', 'q3'], ['a', 'b', 'c'], 'q0',
                                  [ ('q0', 'a', 'q1'),
                                    ('q1', 'b', 'q2'),
                                    ('q2', 'c', 'q3'),
                                    ('q3', 'a', 'q1'),
                                    ('q1', 'b', 'q1'),
                                    ('q0', 'b', 'q2')                                    
                                  ],
                                   {'q3'})

gr = Finite_Automaton.fa_to_rg()
print('q0 ->' , gr.S)
print('VN ->', gr.VN)
print('VT ->', gr.VT)
print('P ->', gr.P)

print('---------------------------')

print("The fa is Deterministic" if Finite_Automaton.fa_det() else "The fa is Non Deterministic")

print('---------------------------')



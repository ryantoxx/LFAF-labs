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

VN = {'S', 'B', 'L'}
VT = {'a', 'b', 'c'}
P = {
    'S': {'aB'},
    'B': {'bB', 'cL'},
    'L': {'cL', 'aS', 'b'}
}

grammar = Grammar(VN, VT, P)
grammar_classification = grammar.chomsky_hierarchy()
print(grammar_classification)

Q = {'q0', 'q1', 'q2', 'q3'}
Sigma = {'a', 'b', 'c'}
F = {'q3'}
delta = {
    ('q0', 'a'): {'q1'},
    ('q1', 'b'): {'q2', 'q1'},
    ('q2', 'c'): {'q3'},
    ('q3', 'a'): {'q1'},
    ('q0', 'b'): {'q2'}
}

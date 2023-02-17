from grammar import Grammar
from finiteAutomaton import finiteAutomata

# V-10
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
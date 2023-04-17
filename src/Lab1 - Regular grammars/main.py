import lexer
from grammar import Grammar
from finiteAutomaton import finiteAutomata
from CNF import CNF


VN = ['S', 'A', 'B', 'D']
VT = ['a', 'b', 'd']
P = {'S': ['dB', 'AB'],
     'A': ['d', 'dS', 'aAaAb', ''],
     'B': ['a', 'aS', 'A'],
     'D': ['Aba']
}
S = 'S'

grammar = CNF(VN, VT, P, S)

print('\nCFG productions:\n')
print('P =', P)

print('\n1st Step: Eliminate null productions:')
grammar.null_production()

print('\n2nd Step: Eliminate unit productions:')
grammar.unit_production()

print('\n3rd Step: Eliminate useless symbols:')
grammar.eliminate_useless_symbols()

print('\nFinal form:')
grammar.toNormalForm()

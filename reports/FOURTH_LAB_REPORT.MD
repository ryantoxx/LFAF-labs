# Topic: Chomsky Normal Form

### Course: Formal Languages & Finite Automata
### Author: Chihai Nichita

----

## Theory

Chomsky Normal Form is a context-free grammar in which the right hand side of any production rule consists of either one terminal symbol or two non-terminal symbols.

Steps to convert a given CFG TO CNF:

1. If the start symbol S occurs on some right side, create a new start symbol S and new productions S' -> S.
2. Remove null productions.
3. Remove unit productions.
4. Replace each production A -> B1 ... Bn where n > 2, with A -> B1C where C -> B2 ... Bn. Repeat this step for all productions having two or more symbols on the right side.
5. If the right side of any production is in the from A -> aB where 'a' is a terminal and A and B are non-terminals, then the production is replaced by A -> XB and X -> a. Repeat this step for every production which is in the form A ->aB.

## Objectives:
1. Learn about Chomsky Normal Form (CNF).
2. Get familiar with the approaches of normalizing a grammar.
Implement a method for normalizing an input grammar by the rules of CNF.
3. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
The implemented functionality needs executed and tested.

## Implementation description
I created a separate class that will hold the implementation of the Chomsky Normal Form. It will be initialized with several attributes such as: non terminal symbols, terminal symbols, productions and starting symbol.
```py
class CNF:
    def __init__(self, VN, VT, P, S):
        self.VN = VN
        self.VT = VT
        self.P = P
        self.S = S
```
I implemented the first rule which is the removing of all null productions.It basically eliminates all productions that derive from the empty string.

```py
def null_production(self):
        P = self.P.copy()
        eps = []
        for production in P:
            if '' in P[production]:
                eps.append(production)
                P[production].remove('')

        eliminate = []
        for i in P.keys():
            if not P[i]:
                eliminate.append(i)
        for item in eliminate:
            P.pop(item)
            self.VN.remove(item)

        for item in eps:
            for production in P:
                for i in range(len(P[production])):
                    P[production][i] = P[production][i].replace(item, '')
        self.P = P
```
In the second rule i removed the unit productions, productinos of the form A -> B from the CFG. It checks if the production contains a non-terminal symbol. If it does, it replaces that non-terminal symbol with the productions that it generates until it only has productions that derive only terminal symbols.

```py
def unit_production(self):
        for production in self.P:
            for symbol in self.P[production]:
                if symbol in self.VN:
                    self.P[production].remove(symbol)
                    self.P[production].extend(self.P[symbol])
```
The third tule is a method that eliminates all inaccessible symbols (non-terminal symbols that cannot be derived from the starting symbol) and all unreachable symbols (non-terminal symbols that cannot derive any terminal string) from the CFG. 

```py
def eliminate_useless_symbols(self):
        reached = set()
        for vt in self.VN:
            for production in self.P:
                for symbol in self.P[production]:
                    if vt in symbol:
                        reached.add(vt)

        useless = []
        for item in list(self.P.keys()):
            if item not in reached:
                useless.append(item)

        for item in useless:
            del self.P[item]
            self.VN.remove(item)
```
The last method converts the resulting CFG after applying the first three methods to Chomsky Normal Form. It first adds a new starting symbol to the CFG and adds a new production that derives the old starting symbol to this new starting symbol.

```py
    self.VN.append('S0')
        dict = {'S0': ['S']}
        self.P = {**dict, **self.P}
```

It creates a dictionary **final** to keep track of all new non-terminal symbols and their corresponding productions. Then it iterates over all the productions and for each production that contains more than two symbols
```py
final = {}
        dict = {}
        flag = 0
        for production in self.P:
            for symbol in self.P[production]:
                if len(symbol) > 1:
                    for char in symbol:
                        if char in self.VT and char not in final.values():
                            final[chr(70 + flag)] = char
                            dict[char] = chr(70 + flag)
                            flag += 1

        for item in dict.keys():
            for production in self.P:
                for i in range(len(self.P[production])):
                    if len(self.P[production][i]) > 1:
                        self.P[production][i] = self.P[production][i].replace(item, dict[item])
```

## Screenshots / Results
This is the CNF for my CFG. Variant 10.
```
CFG productions:

P = {'S': ['dB', 'AB'], 'A': ['d', 'dS', 'aAaAb', ''], 'B': ['a', 'aS', 'A'], 'D': ['Aba']}

1st Step: Eliminate null productions:

P =  {'S': ['dB', 'B'], 'A': ['d', 'dS', 'aab'], 'B': ['a', 'aS', ''], 'D': ['ba']}

2nd Step: Eliminate unit productions:

P =  {'S': ['dB', 'a', 'aS'], 'A': ['d', 'dS', 'aab'], 'B': ['a', 'aS'], 'D': ['ba']}

3rd Step: Eliminate useless symbols:

P =  {'S': ['dB', 'a', 'aS'], 'B': ['a', 'aS']}

Final form:

P = {'S0': ['S'], 'S': ['FB', 'a', 'GS'], 'B': ['a', 'GS'], 'F': 'd', 'G': 'a'}
```

## Conclusions 

In this laboratory work I managed to convert my context free grammar to its chomsky normal form. I analyzed the steps and rules that it takes to convert the certain CFG to its CNF form. Implementing CNF in python allowed me to  transform grammar into a form that is easy to work with.

To sum up, this technique was useful for my experience and it allowed me to understand more complex concepts.

## References

1. [Algorithm to convert into Chomsky Normal From](https://www.tutorialspoint.com/automata_theory/chomsky_normal_form.htm)
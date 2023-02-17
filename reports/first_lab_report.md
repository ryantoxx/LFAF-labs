# The title of the work

### Course: Formal Languages & Finite Automata
### Author: Chihai Nichita

----

## Theory
* A language is: A set of strings from some alphabet (finite or 
infinite), in other words…
* A grammar G is an ordered quadruple G=(VN, VT, P, S) where:
    - VN is a finite set of non-terminal symbols
    - VT - is a finite set of terminal symbols
    - S belongs N is a start symbol
    - P – is a finite set of productions of rules

* An automaton is an abstract model of a digital computer. It is  is a 5-tuple (Q, Σ, δ,q0, F) 
where:
    - Q is a finite set of states.
    - Σ is an input alphabet.
    - δ: Q × Σ → Q is a transition function.
    - q0 belongs Q is the initial state.
    - F subset Q is a set of accepting states (or final states)

## Objectives:
1. General knowledge about language and what it needs to be cosidered to be a formal one.
2. Create a local repository for storing the laboratory works
3. Implement a type/class for your grammar
4. Add one function that would generate 5 valid strings from the language expressed by your given grammar
5. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton
6. For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;


## Implementation description

* Function that generates strings:
    - It randomly generates a string choosing transition rules from a set of rules associated with each symbol in the grammar, and keeps track of the trasitions used to geberate the string.The resulting string and the transitions used to generate it are printed and returned by the method.
```
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
```

* Function that converts a grammar object to a finite automaton.
    - this method converts a grammar into a finite automaton by creating a set of states based on the productions associated with the starting symbol 'S', defining the input symbols based on the lowercase symbols used in the productions, and defining the transition function based on the productions in the grammar. The resulting finite automaton is returned by the method.

```
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
```

* Function that checks whether the string is a finite automaton
    - this method checks whether a given string is accepted by a finite automaton by constructing the list of transitions made by the automaton while processing the string and comparing these transitions to the transition function of the automaton. If the transitions are valid and lead to a final state, the string is accepted by the automaton. Otherwise, the method returns False.

```
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
```
## Screenshots / Results
* My variant was number 10:

![image](https://user-images.githubusercontent.com/114425150/219773236-a827fb16-e065-4233-b80c-c49013adbfd4.png)


* The genrating strings + checking whether belongs to FA

![image](https://user-images.githubusercontent.com/114425150/219773409-20b80ff5-6ae3-4394-8530-5b785e0e5e23.png)



## Conclusions 
In this laboratory work I developed the basic logic in understandint the purpose of a language, regular grammar and it's applications.To my mind the trickiest part of the undestadint of the Finite Automaton and it's purpose, it was quite challenging for me to understand this concept, which I'm satiesfied that I managed to implement it here.
To sum up this laboratory work a great introduction to the theme and to further projects.

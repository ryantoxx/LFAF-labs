# Topic: Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.

### Course: Formal Languages & Finite Automata
### Author: Chihai Nichita

----

## Theory

#### Finite Automata:
* Deterministic Finite Automata (DFA) -
A deterministic finite automaton is a 5-tuple (Q, Σ, δ, q0, F) 
where:
    - Q is a finite set of states.
    - Σ is an input alphabet.
    - δ: Q × Σ → Q is a transition function.
    - q0 belongs Q is the initial state.
    - F is a subset Q is a set of accepting states (or final states).

* Nondeterministic Finite Automata (NFA) -
A nondeterministic finite automaton is a 5-tuple (Q, Σ, δ, q0, F) 
where:
    - Q is a finite set of states;
    - Σ is an input alphabet;
    - δ: Q × (Σ ∪ {lambda}) → subsets of Q is a transition function;
    - q0 belongs Q is the initial state;
    - F is a subset Q is a set of accepting states (or final states).

* Differences from DFA:

1. transition function δ can go into several states;
2. it is allowed the epsilon-transitions

#### Chomsky Classification:

Type 0. Unristricted Grammar

Type 1. Context-Sensitive Grammar

Type 2. Context-Free Grammar

Type 3. Regular Grammar

## Objectives:

1. Understand the concepts of NFA and DFA, along with the classificaton of Chomsky Hierarchy
2. Implement conversion of a finite automaton to a regular grammar.
3. Determine whether your FA is deterministic or non-deterministic.
4. Implement some functionality that would convert an NDFA to a DFA.
5. Represent the finite automaton graphically (optionally)

## Implementation description

* Function that determines the Chomsky type:
    - The function takes a grammar represented by a set of variables (VN), a set of terminals (VT), and a set of production rules (P), and checks each production rule to see if it meets the criteria for each type of grammar.

```
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

```

* Functions that converts Finite Automaton to a Regular Grammar:
    - It first initializes the sets VN, VT, and S to the set of states Q, the input alphabet Sigma, and the initial state q0, respectively. It then initializes an empty dictionary P to hold the production rules of the.The function iterates over each transition (i, sigma, j) in the transition function delta and adds a production rule i -> sigma j to the dictionary P. If i is not already a key in P, it adds an empty list to P[i] before appending the new production rule.
```
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
```

* Functions that cheks whether my FA is deterministic or not:
    - This function takes in a Finite Automaton n as input and returns a Boolean value indicating whether the FA is deterministic or not.The function first creates an empty dictionary delta to store the transitions of the FA.It returns true whether any state 'Q1' has more than one possible transition for  a given input symbol 'S'.It return true, indicating that it is non-deterministic, otherwise it is deterministic

```
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
```
My finite automaton is deterministic.

## Screenshots / Results

* Variant:

![Variant Number 10:](/img/variant.png)

* Results:

![Result for Lab 2:](/img/results.png)

* DFA using graphviz:

![DFA graph:](/img/dfa.png)

* NFA using graphviz:

![NFA graph:](/img/NFA.png)

## Conclusions 
In conclusion, the Chomsky hierarchy is a system for categorizing grammars according to the kinds of rules they employ to produce languages. It consists of four types, starting from Type 0 to Type 3, each with unique constraints on the structure of its rules.

Deterministic Finite Automata and Nondeterministic Finite Automata are types of automata that can identify formal languages. DFAs, a subset of NFAs, are simpler to build and analyze than NFAs since they only contain one transition from each state on each input symbol. Yet, NFAs are more effective in some situations than DFAs because they can recognize some languages that DFAs cannot.

Overall, the Chomsky hierarchy and the distinctions between NFA and DFA are important concepts in formal language theory that help us understand the capabilities and limitations of different types of grammars and automata.
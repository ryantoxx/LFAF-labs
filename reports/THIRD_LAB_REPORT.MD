# Topic: Lexer & Scanner

### Course: Formal Languages & Finite Automata
### Author: Chihai Nichita

----

## Theory

Lexical Analysis:

Lexical analysis is the process of analyzing the structure of a sequence of characters in a source code file or other text input in order to produce a stream of tokens, which are the basic building blocks of programming languages.

During lexical analysis, a lexer (also known as a scanner or tokenizer) which is a component of a compiler or interpreter that takes the source code of a programa as input and  converts it into a sequence of tokens, examines the input text character by character, identifying and grouping together sequences of characters that represent meaningful units, such as keywords, identifiers, literals, operators, and punctuation symbols.

The purpose of lexical analysis is to simplify the process of parsing a programming language by breaking down the input text into smaller, more manageable units that can be processed more efficiently. This makes it easier for the compiler or interpreter to analyze the input code and detect any syntactical or semantic errors.

## Objectives:

1. Understand what lexical analysis is.
2. Get familiar with the inner working of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.

## Implementation description

* First I defined a set of constants that will be used as token types for the lexer.

```
INT		    = 'INT'
FLOAT    = 'FLOAT'
PLUS     = 'PLUS'
MINUS    = 'MINUS'
MUL      = 'MUL'
DIV      = 'DIV'
EQUAL    = 'EQUAL'
LPAREN   = 'LPAREN'
RPAREN   = 'RPAREN'
```
* I created a class __Lexer__ that has several methods such as __advance()__, __make_tokens()__ and __make_number()__.

Advance method updates the current character and the position of the lexer in the input code.

```python
 def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None
```
* The __make tokens()__ method updates the current character and the position of the lexer in the input code and generates a list of tokens from the input code.It then iterates over the input code and checks the current character against a set of rules.If the current character is a digit, the __make_number()__ is called to generate an INT or FLOAT. If the current character is a special character __('+', '-', '*', '/','(', ')', '=')__ a corresponding token is generated.If the current character does not match any rules, an error is raised.

```python
def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(PLUS))
                self.advance()
            ...

            ...
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        return tokens, None
```
* The __make_number()__ method generates a token for a __integer__ or a __float__ number.It reads characters from the input code until it finds a non-digit character or a second period for __floats__. Then, it converts the number string to an __integer__ or __float__ and return the coresponding token.

```python
def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(INT, int(num_str))
        else:
            return Token(FLOAT, float(num_str))
```
* The __Token__ class represents a single token and has two attributes: __type__ (string representing the token type) and __value__ (the value of the token).The class has a  method __repr()__ which is basically used to return a string representation of the token.

```python
def __repr__(self):
        if self.value: return f'{self.type}: \'{self.symbol}{self.value}\''
        return f'{self.type}: \'{self.symbol}\''
```

* The __Position__ class represents the current position of the lexer in the input code.It has two mehotds for __advacing__ the position and creating a __copy__ of the current position.

```python
def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self
```

```python
def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)
```

* The __Error__ class represents a lexer error and has several attributes.It was created with the purpose of one method __as_string()__ which returs a string representation of the error. The __IllegalCharError__ class is a subclass of __Error__ and represents an illegal character error.It was basically implemented to set the error name to "Illegal Character".

```python
 def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result
```
* At the end, the __run()__ function is defined, which creates an instance of a __Lexer__ class and generates a list of tokens from the input code. The function returns the list of tokens and any errors that were raised during the lexing process.

```python
def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error
```

* I call the __run()__ function in a separate file __main.py__ where it loops till an error is raised or when a new expression is typed and the tokenization output ocurrs.

```python
while True:
    text = input('lexer > ')
    tokens, error = lexer.run('example.txt',text)

    if error: 
        print(error.as_string())
    else: 
        print(tokens)
```

## Screenshots / Results
1. Succesful sample example:
    - Input: 20 + (2.5 * 15) - 40 / 5 = 64.33
```
[INT: '20', PLUS: '+', LPAREN: '(', FLOAT: '2.5', MUL: '*', INT: '15', RPAREN: ')', MINUS: '-', INT: '40', DIV: '/', INT: '5', EQUAL: '=', FLOAT: '64.33']
```

2. Failed sample example:
    - Input 12 * 32 = a / 4
```
Illegal Character: 'a'
File <example.txt, line 1
```

## Conclusions 

In this laboratory work, I managed to implement a simple lexer that is responsible for  breaking down the input code into a stream of tokens, which represent the basic units of meaning in the language.
I was able to get a deeper understanding in the process of creating a compiler or interpreter for a programming language since lexer is the first step in creating one.

Overall, I consider this laboratory work a solid beginning for implementing more sophisticated projects in the future.

## References

1. [How to write a programming language, the lexer.](https://accu.org/journals/overload/26/145/balaam_2510/)
2. [What is a lexer?](https://dev.to/cad97/what-is-a-lexer-anyway-4kdo)
3. [Make your own programming language. The lexer.](https://www.youtube.com/watch?v=Eythq9848Fg)
4. [Lexical Analysis and Syntax Analysis](https://www.geeksforgeeks.org/lexical-analysis-and-syntax-analysis/)

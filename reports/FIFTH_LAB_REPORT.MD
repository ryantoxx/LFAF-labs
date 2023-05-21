# Parser & Building an Abstract Syntax Tree

### Course: Formal Languages & Finite Automata
### Author: Chihai Nichita

----

## Theory
A parser is a program that is part of the compiler, and parsing is part of the compiling process. Parsing happens during the analysis stage of compilation.

In parsing, code is taken from the preprocessor, broken into smaller pieces and analyzed so other software can understand it. The parser does this by building a data structure out of the pieces of input.

More specifically, a person writes code in a human-readable language like C++ or Java and saves it as a series of text files. The parser takes those text files as input and breaks them down so they can be translated on the target platform.

Abstract Syntax Tree is a kind of tree representation of the abstract syntactic structure of source code written in a programming language. Each node of the tree denotes a construct occurring in the source code.

There is numerous importance of AST with application in compilers as abstract syntax trees are data structures widely used in compilers to represent the structure of program code. An AST is usually the result of the syntax analysis phase of a compiler. It often serves as an intermediate representation of the program through several stages that the compiler requires, and has a strong impact on the final output of the compiler.


## Objectives:

1. Get familiar with parsing, what it is and how it can be programmed.
2. Get familiar with the concept of AST.
In addition to what has been done in the 3rd lab work do the following:
3. In case you didn't have a type that denotes the possible types of tokens you need to:
    - Have a type TokenType (like an enum) that can be used in the lexical analysis to categorize the tokens.
    - Please use regular expressions to identify the type of the token.
    - Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
    - Implement a simple parser program that could extract the syntactic information from the input text.

## Implementation description

* I used regular expression and made a TokenType class as I did not implement it when I did the logic of the Lexer

```py
class TokenType:
    INT = 'INT'
    FLOAT = 'FLOAT'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MUL = 'MUL'
    DIV = 'DIV'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    EOF = 'EOF'
```
* I've implemented two new classes that basically are meant to parse the input provided by the user. It takes a list of __tokens__ as input and initializes the parser by setting the tokens attribute and calling the __advance__ method to set the __current_tok__ attribute to the first token.
```py
def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def parse(self):
        res = self.expr()
        if not res.error and self.current_tok.type != TokenType.EOF:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected '+', '-', '*' or '/'"
            ))
```
* The methods that provide the parsing of the input are __factor__, __term__ and __expr__.
```py
def factor(self):
        res = ParseResult()
        tok = self.current_tok

        if tok.type in (TokenType.PLUS, TokenType.MINUS):
            res.register(self.advance())
            factor = res.register(self.factor())
            if res.error:
                return res
            return res.success(UnaryOpNode(tok, factor))

        elif tok.type in (TokenType.INT, TokenType.FLOAT):
            res.register(self.advance())
            return res.success(NrNodee(tok))

        elif tok.type == TokenType.LPAREN:
            res.register(self.advance())
            expr = res.register(self.expr())
            if res.error:
                return res
            if self.current_tok.type == TokenType.RPAREN:
                res.register(self.advance())
                return res.success(expr)
            else:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected ')'"
                ))

        return res.failure(InvalidSyntaxError(
            tok.pos_start, tok.pos_end,
            "Expected int or float"
        ))

    def term(self):
        return self.bin_op(self.factor, (TokenType.MUL, TokenType.DIV))

    def expr(self):
        return self.bin_op(self.term, (TokenType.PLUS, TokenType.MINUS))

```
* The factor method handles parsing of factors, which can be unary operations, numbers (integers or floats), or parentheses enclosing expressions. It uses the ParseResult class to handle the parsing results. If the current token is a unary operation (+ or -), it creates a __UnaryOpNode__ with the operator and the result of recursively parsing the factor. If the current token is a number, it creates an NrNode with the token value. If the current token is a left parenthesis, it advances the token and recursively parses an expression. After parsing the expression, it checks if the next token is a right parenthesis. If it is, the expression is considered valid; otherwise, an error is returned.

* The term method handles parsing of terms, which involve multiplication and division operations. It uses the __bin_op__ method to handle the binary operations. It calls __bin_op__ with self.factor as the parsing function and the set of operators __(TokenType.MUL, TokenType.DIV)__.

* The expr method handles parsing of expressions, which involve addition and subtraction operations. It also uses the __bin_op__ method with self.term as the parsing function and the set of operators __(TokenType.PLUS, TokenType.MINUS)__.

## Screenshots / Results
The AST of the project.
1. Basic input:
    - Input: 6 + 5 * 2
```
(INT:6, PLUS, (INT:5, MUL, INT:2))
```

2. Adding parentheses
    - Input: (6 + 5) * 2
```
((INT:6, PLUS, INT:5), MUL, INT:2)
```
3. Unary Operation
    - Input: -6
```
(MINUS, INT:6)
```
4. Complex example
    - Input: (34.3 - 23) * 4 + 12.5 / 43 * (34 - 4) +  321 
```
((((FLOAT:34.3, MINUS, INT:23), MUL, INT:4), PLUS, ((FLOAT:12.5, DIV, INT:43), MUL, (INT:34, MINUS, INT:4))), PLUS, INT:321)
```
5. Error handling (Invalid Syntax)
    - Input: 543 - 12342 14214 
```
Invalid Syntax: Expected '+', '-', '*' or '/'
File <example.txt, line 1

543 - 12342 14214
```
6. Error handling (Illegal Character)
    - Input: 32 + 53 / (4 + d)
```
Illegal Character: 'd'
File <example.txt, line 1

32 + 53 / (4 + d)
               ^
```
## Conclusions 
In conclusion, the implementation of a parser is an important step in building a language processing system or interpreter. The parser is responsible for analyzing the structure of input code and creating a parse tree or an Abstract Syntax Tree (AST). This tree-like structure represents the hierarchical relationship between the different components of the code.

The provided code is a simple parser that handles expressions involving numbers and basic arithmetic operations. It uses a ParseResult class to track the parsing results and potential errors. The Parser class defines methods for parsing factors, terms, and expressions, as well as a general method for parsing binary operations. The code employs recursive descent parsing, where each parsing method corresponds to a particular grammar rule.

Overall, the implementation of a parser in Python provides a solid foundation for developing language processing systems and enables you to perform analysis and manipulation of code structures.

## References
1. [Parsing In Python: Tools And Libraries](https://tomassetti.me/parsing-in-python/)
2. [Make your own programming language. The parser.](https://www.youtube.com/watch?v=RriZ4q4z9gU&t=381s)
3. [Guide to the Parser. Python](https://devguide.python.org/internals/parser/index.html)

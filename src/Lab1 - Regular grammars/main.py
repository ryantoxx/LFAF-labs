import Lexer_Parser.parse as parse

while True:
    text = input('input > ')
    tokens, error = parse.run('<example.txt', text)

    if error: 
        print(error.as_string())
    else: 
        print(tokens)

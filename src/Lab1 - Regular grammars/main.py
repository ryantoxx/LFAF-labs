import lexer

while True:
    text = input('lexer > ')
    tokens, error = lexer.run('<example.txt',text)

    if error: 
        print(error.as_string())
    else: 
        print(tokens)

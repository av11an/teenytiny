from lex import *

def main():
    source = "testVar = \"My string\""
    lexer = Lexer(source)

    token = lexer.getToken()        
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()


main()

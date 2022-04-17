from lib2to3.pgen2.token import EQUAL
from sly import Lexer

class BasicLexer(Lexer):
    tokens = {NAME, NUMBER, STRING, IF, PRINT, THEN, ELSE, FOR, FUN, TO, ARROW, EQUAL,  }
    ignore = '\t '
    ignore_comment = r'\#.*'


    #definisi token
    IF      = r'if'
    PRINT   = r'print'
    THEN    = r'then'
    ELSE    = r'else'
    FOR     = r'for'
    FUN     = r'fun'
    TO      = r'to'
    ARROW   = r'->'
    NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING  = r'\".*?\"'
    EQUAL    = r'=='


    #token bilangan
    @_(r'\d+')
    def NUMBER(self, t):

        #konvert ke integer
        t.value = int(t.value)
        return t
    
    #token komen
    @_(r'//.*')
    def COMMENT(self, t):
        pass 

    #token newline
    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    #token error
    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1
    
if __name__ == '__main__':
    lexer = BasicLexer()
    env = {}
    while True:
        try:
            text = input('pm > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)

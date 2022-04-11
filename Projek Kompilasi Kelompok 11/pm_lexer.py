from sly import Lexer

class BasicLexer(Lexer):
    tokens = {NAME, NUMBER, STRING, IF, PRINT, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ, PLUS, MINUS, TIMES, DIVIDE, LT, LE, GT, GE, NE}
    ignore = '\t '
    ignore_comment = r'\#.*'

    literals = {'=', '(', ')', '{', '}' ',', ';'}


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

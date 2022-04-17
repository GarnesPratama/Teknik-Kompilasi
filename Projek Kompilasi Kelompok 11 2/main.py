import kelompok11_lexer
import kelompok11_parser
import kelompok11_interpreter

from sys import *


lexer = kelompok11_lexer.BasicLexer()
parser = kelompok11_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    kelompok11_interpreter.BasicExecute(tree, env)

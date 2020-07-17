from lexer import lexer
from transpiler import transpiler

code = lexer(open('testing.rg'))

code.lexing()

codeeee = transpiler(code.return_tokens())

#for debug purposes only
for i in code.return_tokens():
    print(i)

codeeee.transpile()

codeeee.write_file()

#import transpiled_file
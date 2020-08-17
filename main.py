from lexer import lexer
from transpiler import transpiler
from sys import argv

try:
	file = argv[1]
except:
	file = "testing.rg"
#print(file)
code = lexer(open(file))

code.lexing()

DebugLevel = 2
# Lvl 1 = Basic Logging
# Lvl 2 = Intermediate Logging
# Lvl 3 = Full logging
codeeee = transpiler(code.return_tokens())

#for debug purposes only
if DebugLevel > 1:
    for i in code.return_tokens():
       print(i)

codeeee.transpile()

codeeee.write_file()

#import transpiled_file
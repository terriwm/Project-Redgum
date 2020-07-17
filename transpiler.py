import os

class transpiler ():
    def __init__(self, tokens):
        self.tokens = tuple(tokens)
        self.raw_transpiled_file = open('transpiled_file.py', 'r+')
        self.raw_transpiled_file.seek(0)
        self.raw_transpiled_file.truncate()
        self.readlines_transpiled_file = self.raw_transpiled_file.readlines()
        self.transpiled_file = []

        for line in self.readlines_transpiled_file:
            self.transpiled_file.append(line)



    def transpile(self):
        self.indentation_level = 0
        for token in self.tokens:

            self.curr_indentation = ''

            for i in range(0, self.indentation_level):
                self.curr_indentation += ('  ')

            #evaling the vars
            if token.find('VAL:') != -1:
                variable = str(token[token.find('ID:') + 4 : token.find('VAL:')] +'='+ token[token.find('VAL:') + 4: len(token)])
                self.transpiled_file.append(self.curr_indentation + variable)
                

            #printing
            if token.find('print') != -1:
                printing = str(token[token.find('OP:') + 4 : len(token)])
                self.transpiled_file.append(self.curr_indentation + 'print('+ printing +')')

            #maths
            if token.find('+') != -1:
                addition = str(token[token.find('ID:') + 4 : token.find('OP:')] +'+= '+ str(token[token.find('+') + 2 : len(token)]))
                self.transpiled_file.append(self.curr_indentation + addition)
            if token.find('-') != -1:
                subtraction = str(token[token.find('ID:') + 4 : token.find('OP:')] +'-= '+ str(token[token.find('-') + 2 : len(token)]))
                self.transpiled_file.append(self.curr_indentation + subtraction)
            if token.find('*') != -1:
                multiplication = str(token[token.find('ID:') + 4 : token.find('OP:')] +'*= '+ str(token[token.find('*') + 2 : len(token)]))
                self.transpiled_file.append(self.curr_indentation + multiplication)
            if token.find('/') != -1:
                division = str(token[token.find('ID:') + 4 : token.find('OP:')] +'/= '+ str(token[token.find('/') + 2 : len(token)]))
                self.transpiled_file.append(self.curr_indentation + division)

            #if, for & while
            if token.find('if') != -1:
                if_statement = 'if ' + str(token[token.find('OP:') + 4 : len(token)]) + ':'
                self.transpiled_file.append(self.curr_indentation + if_statement)
            if token.find('while') != -1:
                while_op = token[token.find('OP:') + 4 : len(token)]
                while_statement = 'while ' + while_op +':'
                self.transpiled_file.append(self.curr_indentation  + while_statement)
            if token.find('for') != -1:
                for_statement = 'for ' + str(token[token.find('VAR:') + 5 : token.find('OP:')]) + 'in ' + str(token[token.find('OP:') + 4 : len(token)]) + ':'
                self.transpiled_file.append(self.curr_indentation + for_statement)

            #Indents
            if token.find('ID: {') != -1:
                self.indentation_level += 1
            if token.find('ID: }') != -1:
                self.indentation_level -= 1

            #functions
            if token.find('FN:') != -1:
                function_dec = 'def' + str(token[token.find('FN:') + 3 : token.find('VAR:')]) + '(' + str(token[token.find('VAR:') + 5 : len(token)]) + '):'
                self.transpiled_file.append(self.curr_indentation + function_dec)

    def write_file(self):
        self.raw_transpiled_file.writelines('#!/usr/bin/env python3\n')
        for line in self.transpiled_file:
            self.raw_transpiled_file.writelines(line + '\n')

        self.raw_transpiled_file.close()



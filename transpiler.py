# Code Written by William
# Comments Written By Evan

class transpiler (): # Creates a class called "transpiler"
	def __init__(self, tokens: tuple): # On instantiation, pass tokens
		self.tokens = tuple(tokens) # local tokens is a tuple of what is passed
		self.raw_transpiled_file = open('transpiled_file.py', 'r+') # open the file
		self.raw_transpiled_file.seek(0)
		self.raw_transpiled_file.truncate()
		self.readlines_transpiled_file = self.raw_transpiled_file.readlines() # Reads the lines into the variable
		self.transpiled_file = [] # set the finished file to an empty list

		for line in self.readlines_transpiled_file: # for every line in the file
			self.transpiled_file.append(line) # append it to the transpiled file list



	def transpile(self): # function called transpile, passed nothing
		self.indentation_level = 0 # indentation level 0 to start with
		for token in self.tokens:

			self.curr_indentation = ''

			for i in range(0, self.indentation_level):
				self.curr_indentation += ('  ')

			#vars
			if token.find('VAR:') != -1:
				if token.find('VAL:') != -1:
					variable = str(token[token.find('ID:') + 4 : token.find('VAL:')] +'='+ token[token.find('VAL:') + 4: len(token)])
					self.transpiled_file.append(self.curr_indentation + variable)
				

			#built in functions
			#if token.find('print') != -1 and token.find('println') == -1:
			#	printing = str(token[token.find('OP:') + 4 : len(token)])
			#	self.transpiled_file.append(self.curr_indentation + 'print('+ printing +', end="")')
			#if token.find('println') != -1:
			#	println = str(token[token.find('OP:') + 4 : len(token)])
			#	self.transpiled_file.append(self.curr_indentation + 'print('+ println +')')
			if token.find('BUILTIN:') != -1:
				if token.find('print') != -1:
					if token.find('println') != -1: temp = ',end=\"\"'
					else: temp = ""
					printer = str(token[token.find('OP:') + 4 : len(token)])
					self.transpiled_file.append(self.curr_indentation + 'print('+ printer +'%s)' % temp)
				if token.find('say') != -1:
					say = 'say = gTTS('+ str(token[token.find('OP:') + 4: len(token)]) +')'
					self.transpiled_file.append(self.curr_indentation + say)
					self.transpiled_file.append(self.curr_indentation + 'say.save("speak.mp3")')
					self.transpiled_file.append(self.curr_indentation + 'playsound.playsound("speak.mp3")')
					self.transpiled_file.append(self.curr_indentation + 'os.remove("speak.mp3")')
				if token.find('return') != -1:
					return_func = 'return('+ str(token[token.find('OP:') + 4 : len(token)]) + ')'
					self.transpiled_file.append(self.curr_indentation + return_func)

			
			#maths
			if token.find('MATH:') != -1:
				if token.find('+') != -1:
					addition = str(token[token.find('ID:') + 4 : token.find('OP:')] +'+= '+ str(token[token.find('+') + 2 : len(token)]))
					self.transpiled_file.append(self.curr_indentation + addition)
				if token.find('-') != -1:
					subtraction = str(token[token.find('ID:') + 4 : token.find('OP:')] +'-= '+ str(token[token.find('-') + 2 : len(token)]))
					self.transpiled_file.append(self.curr_indentation + subtraction)
				if token.find('*') != -1:
					multiplication = str(token[token.find('ID:') + 4 : token.find('OP:')] +'*= '+ str(token[token.find('*') + 2 : len(token)]))
					self.transpiled_file.append(self.curr_indentation + multiplication)
				if token.find('/') != -1 and token.find('_/') == -1 and token.find('//') == -1:
					division = str(token[token.find('ID:') + 4 : token.find('OP:')] +'/= '+ str(token[token.find('/') + 2 : len(token)]))
					self.transpiled_file.append(self.curr_indentation + division)
				if token.find('_/') != -1:
					floor_div = str(token[token.find('ID:') + 4 : token.find('OP:')]) + '= ' + str(token[token.find('OP:') + 4 : len(token)])
					self.transpiled_file.append(self.curr_indentation + floor_div)
				if token.find('floor') != -1:
					floor = str(token[token.find('ID:') + 4 : token.find('OP:')] + '= math.floor(' + str(token[token.find('floor') + 6 : len(token)]) +')')
					self.transpiled_file.append(self.curr_indentation + floor)
				if token.find('%') != -1:
					modulo = str(token[token.find('ID:') + 4: token.find('OP:')]) +'%='+ str(token[token.find('%') + 1 : len(token)])
					self.transpiled_file.append(self.curr_indentation + modulo)

			#if, for & while
			if token.find('BASE:') != -1:
				if token.find('if') != -1 and token.find('elif') == -1:
					if_statement = 'if ' + str(token[token.find('OP:') + 4 : len(token)]) + ':'
					self.transpiled_file.append(self.curr_indentation + if_statement)
				if token.find('elif') != -1:
					elif_statement = 'elif '+ str(token[token.find('OP:') + 4 : len(token)]) + ':'
					self.transpiled_file.append(self.curr_indentation + elif_statement)
				if token.find('else') != -1:
					else_statement = 'else:'
					self.transpiled_file.append(self.curr_indentation + else_statement)
				if token.find('while') != -1:
					while_op = token[token.find('OP:') + 4 : len(token)]
					while_statement = 'while ' + while_op +':'
					self.transpiled_file.append(self.curr_indentation  + while_statement)
				if token.find('for') != -1:
					for_statement = 'for ' + str(token[token.find('VAR:') + 5 : token.find('OP:')]) + 'in ' + str(token[token.find('OP:') + 4 : len(token)]) + ':'
					self.transpiled_file.append(self.curr_indentation + for_statement)

			#Indents
			if token.find('BRACE:') != -1:
				if token.find('ID: {') != -1:
					self.indentation_level += 1
				if token.find('ID: }') != -1:
					self.indentation_level -= 1

			#functions
			if token.find('FUNCTION:') != -1:
				if token.find('FN:') != -1 and token.find('VAR') != -1:
					function_dec = 'def' + str(token[token.find('FN:') + 3 : token.find('VAR:')]) + '(' + str(token[token.find('VAR:') + 5 : len(token)]) + '):'
					self.transpiled_file.append(self.curr_indentation + function_dec)
				if token.find('FN:') != -1 and token.find('VAR') == -1:
					function_op = str(token[token.find('FN:') + 4 : token.find('OP:') - 1]) + '(' + str(token[token.find('OP:') + 4 : len(token)]) + ')'
					self.transpiled_file.append(self.curr_indentation + function_op)


	def write_file(self):
		self.raw_transpiled_file.writelines('#!/usr/bin/env python3\n')
		self.raw_transpiled_file.writelines('import math\n')
		self.raw_transpiled_file.writelines('import gTTS\n')
		self.raw_transpiled_file.writelines('import os\n')
		self.raw_transpiled_file.writelines('import playsound\n')
		for line in self.transpiled_file:
			self.raw_transpiled_file.writelines(line + '\n')

		self.raw_transpiled_file.close()



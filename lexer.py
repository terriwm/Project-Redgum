

class lexer ():
    def __init__(self, source_code):
        self.psc = source_code
        self.isc = self.psc.readlines()
        self.sc = []
        self.tokens = []
        self.strings = []

        for i in range(len(self.isc)):
            quote_locs = []
            for j in range(len(self.isc[i])):
                if self.isc[i][j] == "'":
                    quote_locs.append(j)

            for k in range(len(quote_locs)):
                if k % 2 == 0:
                    self.strings.append(self.isc[i][quote_locs[k] + 1 : quote_locs[k + 1]])


        for line in self.isc:
            line = line.replace(' ', '')
            line = line.replace('\n', '')
            line = line.replace('true', 'True')
            line = line.replace('false', 'False')
            line = line.replace('&&', ' and ')
            line = line.replace('||', ' or ')
            if line.find("'") != -1:
                for i in range(len(self.strings)):
                    stripped_string = self.strings[i].replace(' ', '')
                    x = line.find("'")
                    y = line.find("'", x + 1)
                    if line[x + 1 : y] == stripped_string:
                        line = line.replace(line[x + 1 : y], self.strings[i])
            self.sc.append(line)


    def lexing (self):
        for i in range(0, len(self.sc)):

            #braces
            if self.sc[i].find('}') != -1:
                self.tokens.append('ID: }')

            #var def
            if self.sc[i][0:3] == 'var':
                self.tokens.append('ID: '+ str(self.sc[i][self.sc[i].find('var') + 3 : self.sc[i].find('=')]) + ' VAL: '+ str(self.sc[i][self.sc[i].find('=') + 1 : len(self.sc[i])]))

            #while, for and if statements
            if self.sc[i].find('if') != -1 and self.sc[i].find('elseif') == -1:
                self.tokens.append('ID: if OP: '+ str(self.sc[i][self.sc[i].find('(') + 1 : self.sc[i].find(')')]))
                self.tokens.append('ID: {')
            if self.sc[i].find('elseif') != -1:
                self.tokens.append('ID: elif OP: '+ str(self.sc[i][self.sc[i].find('(') + 1 : self.sc[i].find(')')]))
                self.tokens.append('ID: {')
            if self.sc[i].find('else') != -1 and self.sc[i].find('elseif') == -1:
                self.tokens.append('ID: else')
                self.tokens.append('ID: {')
            if self.sc[i][0:5] == 'while':
                self.tokens.append('ID: while OP: '+ str(self.sc[i][self.sc[i].find('(') + 1 : self.sc[i].find(')')]))
                self.tokens.append('ID: {')
            if self.sc[i][0:3] == 'for':
                self.tokens.append('ID: for VAR: '+ str(self.sc[i][self.sc[i].find('(') + 1 : self.sc[i].find('=>')]) + ' OP: ' + str(self.sc[i][self.sc[i].find('=>') + 2: self.sc[i].find(')') + 1]))
                self.tokens.append('ID: {')

            #basic printing and other statements
            if self.sc[i][0:5] == 'print':
                self.tokens.append('ID: print OP: '+ str(self.sc[i][self.sc[i].find('(') + 1 : self.sc[i].find(')')]))

            #maths
            if self.sc[i].find('+=') != -1:
                self.tokens.append('ID: '+ str(self.sc[i][0 : self.sc[i].find('+')]) +' OP: + '+ str(self.sc[i][self.sc[i].find('=') + 1 : len(self.sc[i])]))
            if self.sc[i].find('-=') != -1:
                self.tokens.append('ID: '+ str(self.sc[i][0 : self.sc[i].find('-')]) +' OP: - '+ str(self.sc[i][self.sc[i].find('=') + 1 : len(self.sc[i])]))
            if self.sc[i].find('*=') != -1:
                self.tokens.append('ID: '+ str(self.sc[i][0 : self.sc[i].find('*')]) +' OP: * '+ str(self.sc[i][self.sc[i].find('=') + 1 : len(self.sc[i])]))
            if self.sc[i].find('/=') != -1:
                self.tokens.append('ID: '+ str(self.sc[i][0 : self.sc[i].find('/')]) +' OP: / '+ str(self.sc[i][self.sc[i].find('=') + 1 : len(self.sc[i])]))
            if self.sc[i].find('++') != -1:
                self.tokens.append('ID: '+ str(self.sc[i][0 : self.sc[i].find('++')]) +' OP: + 1')
            if self.sc[i].find('--') != -1:
                self.tokens.append('ID: '+ str(self.sc[i][0 : self.sc[i].find('--')]) +' OP: - 1')

            #functions
            if self.sc[i].find('fn') != -1 and self.sc[i].find('{') != -1:
                self.tokens.append('FN: '+ str(self.sc[i][self.sc[i].find('fn') + 2 : self.sc[i].find('(')]) +' VAR: '+ str(self.sc[i][self.sc[i].find('(') + 1 : self.sc[i].find(')')]))
                self.tokens.append('ID: {')
            if self.sc[i].find('fn') != -1 and self.sc[i].find('{') == -1:
                self.tokens.append('FN: '+ str(self.sc[i][self.sc[i].find('fn') + 2 : self.sc[i].find('(')]) + ' OP: '+ str(self.sc[i][self.sc[i].find('(') + 1 : self.sc[i].find(')')]))


            #built in functions
            if self.sc[i].find('return') != -1:
                self.tokens.append('ID: return OP: ' + str(self.sc[i][self.sc[i].find('(') + 1 : self.sc[i].find(')')]))
   



    def return_tokens(self):
        return(self.tokens)


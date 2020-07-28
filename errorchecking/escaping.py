
text = ""
rg_file = None
paired_chars = ('\"\"', "\'\'", "()", "{}", "[]")
quote_chars = ("\"", "\'")
string_regions = []

def greatest(liste:list):
    high = 0
    for i in liste:
        if i > high:
            high = i
    return high

def tests(fp: str):
    rg_file = open(fp, "r")
    text = rg_file.read()
    stripped_text = text.strip()

def strip_comments(text: str): # strip the comments out for better checking
    
    regions = find_string_regions(text.strip()) # all of the regions encased in strings
    print(str(regions) + " PrintCodeA - String Regions") # for debug purposes
    print(str(text.count("//")) + " PrintCodeB - Amount of //") # for debug purposes
    excluded = [] # a list of the things that should not be comments because theyr'e in strings
    for i in range(text.count("//")):  # for every double-slash
        start = text.index("//", greatest(excluded) + 1) # it starts at the first found that hasn't already been processed
        valid = True # if the comment is still a comment
        for reg in regions: # for every string region
            if reg[0] < start < reg[1]: # if it's inside the region
                valid = False # it isn't valid, its in the string
        if valid: # after that, if its valid still
            text = text[:text.index("//", greatest(excluded) + 1)] + text[text.index("\n", text.index("//", greatest(excluded) + 1)):]
            # remove it from the text to fix
        else:
            excluded.append(text.index("//", greatest(excluded) + 1))
            # otherwise, it is excluded from future searches
    print(str(excluded) + " PrintCodeC - Excluded Regions")
    return text
        
def find_string_regions(stripped_text: str):
    if stripped_text.count("\"") % 2 == 1 or stripped_text.count("\'") % 2 == 1:
        exit("wrong num quotes")
    removedchars = 0
    string_regions = [] 
    temptext = stripped_text
    for char in quote_chars:
        for _ in range(stripped_text.count(char) // 2):
            string_regions.append((temptext.index(char) + removedchars, temptext.index(char,temptext.index(char) + 1) + removedchars))
            temptext = temptext[:temptext.index(char)] + temptext[temptext.index(char) + 1:]
            temptext = temptext[:temptext.index(char)] + temptext[temptext.index(char) + 1:]
            removedchars += 2
        temptext = stripped_text
        removedchars = 0
    return string_regions

def escaped_parentheses(stripped_text: str):
    for i in paired_chars:
        if stripped_text.count(i[0]) == stripped_text.count(i[1]):
            pass
#"hello\"mo\"yeet\'me\'"
#"hello // hi \n hello"

b = open("errorunescaped.rg", "r")
print(str(strip_comments(b.read())) + " PrintCodeD - Custom Debug")
#print("hello // hi \nhello\n\"hi // \"\n")
#print(find_string_regions("hello // hi \nhello\n\"hi // \"\n".strip()))
#print(strip_comments("hello // hi \nhello\n\"hi // \"\n"))


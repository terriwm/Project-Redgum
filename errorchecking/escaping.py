
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

def strip_comments(text: str):
    
    regions = find_string_regions(text.strip())
    print(regions)
    print(text.count("//"))
    excluded = []
    for i in range(text.count("//")): 
        start = text.index("//", greatest(excluded) + 1)
        valid = True
        for reg in regions:
            if reg[0] < start < reg[1]:
                valid = False
        if valid:
            text = text[:text.index("//", greatest(excluded) + 1)] + text[text.index("\n", text.index("//", greatest(excluded) + 1)):]
        else:
            excluded.append(text.index("//"))
    print(excluded)
    return text
        
def find_string_regions(stripped_text: str):
    if stripped_text.count("\"") % 2 == 1 or stripped_text.count("\'") % 2 == 1:
        exit("wrong num quotes")
    removedchars = 0
    string_regions = [] 
    temptext = stripped_text
    for char in quote_chars:
        for i in range(stripped_text.count(char) // 2):
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
print(strip_comments(b.read()))
#print("hello // hi \nhello\n\"hi // \"\n")
#print(find_string_regions("hello // hi \nhello\n\"hi // \"\n".strip()))
#print(strip_comments("hello // hi \nhello\n\"hi // \"\n"))


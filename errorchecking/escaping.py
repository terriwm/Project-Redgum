
text = ""
rg_file = None
paired_chars = ('\"\"', "\'\'", "()", "{}", "[]")
quote_chars = ("\"", "\'")
def tests(fp: str):
    rg_file = open(fp, "r")
    text = rg_file.read()
    stripped_text = text.strip()

def strip_comments(rg_file):
    lines = rg_file.readlines()
    for i in lines:
        if i.count("\\") == 1 and i.index("\\") not in reg

def find_string_regions(stripped_text: str):
    if stripped_text.count("\"") % 2 == 1 or stripped_text.count("\'") % 2 == 1:
        exit("wrong num quotes")
    removedchars = 0
    regions = []
    temptext = stripped_text
    for char in quote_chars:
        for i in range(stripped_text.count(char)):
            regions.append((temptext.index(char), temptext.index(char, start=temptext.index(char) + 1)))
            temptext = temptext[:temptext.index(char)] + temptext.index[temptext.index(char) + 1:]
            temptext = temptext[:temptext.index(char)] + temptext.index[temptext.index(char) + 1:]
            removedchars += 2
        temptext = stripped_text
        removedchars = 0
    return regions


def escaped_parentheses(stripped_text: str):
    for i in paired_chars:
        if stripped_text.count(i[0]) == stripped_text.count(i[1]):
            pass

print(find_string_regions("hello\"mo\""))
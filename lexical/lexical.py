keyword = ['break', 'case', 'char', 'const', 'countinue', 'deafult', 'do', 'int', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
           'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
built_in_functions = ['clrscr()', 'printf(', 'scanf(', 'getch()', 'main()']
operators = ['+', '-', '', '/', '%', '==', '!=', '>', '<', '>=', '<=',
             '&&', '||', '!', '&', '|', '^', '~', '>>', '<<', '=', '+=', '-=', '=']
specialsymbol = ['@', '#', '$', '_', '!']
separator = [',', ':', ';', '\n', '\t', '{', '}', '(', ')', '[', ']']

file = open("input.txt", "r+")
filecontent = file.read()
split = filecontent.split()
length = len(split)

for i in range(0, length):
    if split[i] in keyword:
        print(split[i], "=keyword")
        continue
    if split[i] in operators:
        print(split[i], "=operator")
        continue
    if split[i] in separator:
        print(split[i], "=seperator")
        continue
    if split[i] in built_in_functions:
        print(split[i], "=built in function")
        continue
    if split[i] in specialsymbol:
        print(split[i], "=Special Symbol")
        continue
    if type(split[i]) == int or type(split[i]) == float or type(split[i]) == complex:
        print(split[i], "=numeral")
        continue
    if split[i].isidentifier():
        print(split[i], "=identifier")

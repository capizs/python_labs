d = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}
print(list(d.keys())[list(d.values()).index(x)] if ((x := input()) in list(d.values())) else -1)
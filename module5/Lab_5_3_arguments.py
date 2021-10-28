# String variable
word = 'Found name:'
# Dict with user data
ids = {'name':"Alice", 'age':27}

def intersection(word,name,*args,age=None):
    # word and name neccessary arguments
    print(word, name)
    # age argument at the end of function arguments set
    print('Age:',age)
    # collecting any arguments into one tuple
    print(args)

# call function with word and ids data unpack
intersection(word, **ids)
# call function with word and ids data and some list unpack
intersection(word, ids['name'], *list(range(10)))

def concatenate(*args):
    word = ''
    for i in args:
        word = word + i + '-'
    return word[:-1]
    

print(concatenate("I", "love", "Python", "!"))

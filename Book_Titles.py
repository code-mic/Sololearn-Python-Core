file = open("books.txt", "r")

#your code goes here
book_list = file.readlines()
for book in book_list:
    if book[-1] == '\n':
        print("{0}{1}".format(book[0], len(book) - 1))
    else:
        print("{0}{1}".format(book[0], len(book)))
file.close()

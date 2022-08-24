poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'r') as poem_file:  => change r (read) to w (write)
    poem_file.write(poem)

FileNotFoundError: [Errno 2] No such file or directory: 'poem.txt'

ANSWER:
create a text file with filename poem.txt
poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w') as poem_file:
    poem_file.write(poem)

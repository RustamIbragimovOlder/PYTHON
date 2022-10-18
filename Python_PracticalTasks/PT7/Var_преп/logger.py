def write_new(contact):
    with open('book.txt', 'a', encoding = 'utf8') as f:
        f.write(contact)

def get_book():
    book = []
    with open('book.txt', 'r', encoding = 'utf8') as f:
        for line in f:
            book.append(line)
    return book
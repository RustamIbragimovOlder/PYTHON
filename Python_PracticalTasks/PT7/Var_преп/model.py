from re import I
from unicodedata import name


def get_contact():
    name = input('NAME: ')
    phone = input('PHONE: ')
    return f'{name} || {phone} \n'

def find_contact(book: list, req: str) -> str:  # list, str - просто анотация!
    a = ''
    for i in book:
        if i.find(req) != -1:
            a += f'{i}'
    if a == '':
        return "Empty"
    else:
        return a

def get_request():
    return input("Contact to find: ")

def choose_mode():
    return int(input("MODE WRITNG - 1; MODE FIND - 2: "))

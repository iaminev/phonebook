from docutils.parsers.rst.directives import path
import random

phone_book = {}
path='phonebook.txt'

path_dummies = ['names.txt','surnames.txt','comments.txt']

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        uid, name, phone, comment = contact.strip().split(';')
        phone_book[int(uid)] = [name, phone, comment]


def save_file():
    with open(path, 'w', encoding = 'UTF-8') as file:
        all_contacts = []
        for uid, contact in phone_book.items():
            all_contacts.append(';'.join([str(uid), contact[0], contact[1], contact[2]]))
        all_contacts = '\n'.join(all_contacts)
        file.write(all_contacts)

def add_contact(new: list[str]) -> str:
    uid = max(phone_book) + 1
    phone_book[uid] = new
    return new[0]


def delete_contact(uid: int) -> str:
    return phone_book.pop(uid)[0]

def change_contact(uid: int, rename: list[str]) -> str:
    contact = phone_book.get(uid)
    for i in range(3):
        if rename[i]:
            contact[i] = rename[i]
    phone_book[uid] = contact
    return contact[0]

def search(word):
    result = {}
    for uid, contact in phone_book.items():
        for field in contact:
            if word.lower() in field.lower():
                result[uid] = contact
                break
    return result


def generate_phone_number()->str:
    phone_codes = ['901', '903', '905', '926', '905']
    digits = '0123456789'
    return f'+7({random.choice(phone_codes)}){random.choice(digits)}{random.choice(digits)}{random.choice(digits)}-{random.choice(digits)}{random.choice(digits)}-{random.choice(digits)}{random.choice(digits)}'
def add_bunch_of_records(num_records: int):
    dummies_dict = {}
    for i in range(3):
        with open(path_dummies[i], 'r', encoding='UTF-8') as file:
            dummies_dict[i] = file.read().splitlines()
    for i in range(num_records):
        contact = [random.choice(dummies_dict[0]) + ' ' + random.choice(dummies_dict[1]), generate_phone_number(), random.choice(dummies_dict[2])]
        add_contact(contact)


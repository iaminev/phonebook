import text

def show_menu() -> int:
    for i,item in enumerate(text.main_menu):
        if i:
            print('\t' + f'{i}. {item}')
        else:
            print(item)
    select_option = input('Выберите пункт меню: ')
    while True:
        if select_option.isdigit() and 0 < int(select_option) < len(text.main_menu):
            return int(select_option)
        select_option = input(text.main_menu_input_error)

def show_contact(book: dict[int, list[str]], msg: str):
    if book:
        max_n, max_p, max_c = 0,0,0
        for contact in book.values():
            if max_n < len(contact[0]):
                max_n = len(contact[0])
            if max_p < len(contact[1]):
                max_p = len(contact[1])
            if max_c < len(contact[2]):
                max_c = len(contact[2])

        print('\n' + '='*(8+6+max_n+max_p+max_c))
        for uid, contact in book.items():
            print(f'{uid: >4}. {contact[0]: <{max_n+2}} {contact[1]: <{max_p+2}} {contact[2]: <{max_c+2}}' )
        print('='*(8+6+max_n+max_p+max_c)+'\n' )
    else:
        print(msg)


def print_msg(msg: str):
    print('\n' + '='*len(msg))
    print(msg)
    print('='*len(msg))

def input_new_contact(input_list: list[str]):
    new_contact = []
    for item in input_list:
        new_contact.append(input(item))
    return new_contact

def input_data(msg: str) -> str:
    return input(msg)

def input_number(msg: str) -> int:
    while True:
        number = input(msg)
        if number.isdigit():
            return int(number)
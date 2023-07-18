main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать контакты',
             'Добавить контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Добавить много записей(1..50)',
             'Выход']

main_menu_input_error = f'Ошибка ввода! Введите число от 1 до {len(main_menu)}: '
too_many_records      = f'Ошибка ввода! Значение должно быть от 1 до {50}'


empty_book = 'Нет записей'

load_successful = 'Телефонная книга успешно загружена.'
save_successful = 'Телефонная книга успешно сохранена.'
fields_new_contact = ['Введите имя: ','Введите телефон: ','Введите комментарий: ']
fields_rename_contact = ['Введите новое имя: ','Введите новый телефон: ','Введите новый комментарий: ']

def new_contact_successful(name: str)->str:
    return f'Контакт {name} успешно добавлен.'

def contact_deleted(name: str)->str:
    return f'Контакт {name} успешно удален.'

def rename_contact_successful(name: str)->str:
    return f'Контакт {name} успешно отредактирован.'

def new_records_added(num: int)->str:
    return f'Успешно создано {num} контактов.'


input_search_word = 'Введите строку для поиска: '
input_del_uid = 'Введите id контакта для удаления: '
input_rename_uid = 'Введите id контакта для редактирования: '
input_number_of_records = 'Введите количество новых записей: '


def empty_search(word: str) -> str:
    return f'Ничего не найдено. Искали: ""{word}"".'
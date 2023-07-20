import view
import model
import text

def search_module():
    word = view.input_data(text.input_search_word)
    result = model.search(word)
    view.show_contact(result, text.empty_search)


def start():
    main_phone_book = model.PhoneBook()
    while True:
        user_select = view.show_menu()
        match user_select:
            case 1:
                main_phone_book.open_file()
                view.print_msg(text.load_successful)
            case 2:
                main_phone_book.save_file()
                view.print_msg(text.save_successful)
            case 3:
                pb = main_phone_book.phone_book
                view.show_contact(pb, text.empty_book)
            case 4:
                contact = view.input_new_contact(text.fields_new_contact)
                main_phone_book.add_contact(contact)
                view.print_msg(text.new_contact_successful(contact[0]))
            case 5:
                search_module()
            case 6:
                search_module()
                uid = view.input_number(text.input_rename_uid)
                rename = view.input_new_contact(text.fields_rename_contact)
                name = main_phone_book.change_contact(uid,rename)
                view.print_msg(text.rename_contact_successful(name))
            case 7:
                search_module()
                uid = view.input_number(text.input_del_uid)
                name = main_phone_book.delete_contact(uid)
                view.print_msg(text.contact_deleted(name))
            case 8:
                num_records = view.input_number(text.input_number_of_records)
                if 0 < int(num_records) <= 50:
                    main_phone_book.add_bunch_of_records(num_records)
                    view.print_msg(text.new_records_added(num_records))
                    pb = main_phone_book.phone_book
                    view.show_contact(pb, text.empty_book)
                else:
                    view.print_msg(text.too_many_records)
            case 9:
                if main_phone_book.phone_book != main_phone_book.original_phone_book:
                    answer = view.input_data(text.save_changes)
                    if answer.lower() =='y':
                        main_phone_book.save_file()
                        view.print_msg(text.save_successful)
                view.print_msg(text.good_day)
                break

import text
import view
import model


def open_file():
    model.read_file()
    view.message(text.open_file_successful)


def save_file():
    model.save_file()
    view.message(text.save_file_successful)


def show_all_contacts():
    view.show_contacts(
        model.phone_book,
        text.empty_phone_book,
    )


def create_contact():
    new_contact = view.input_data(text.create_new_user)
    model.create_contact(new_contact)
    view.message(text.contact_create_successful.format(name=new_contact[0]))


def find_contact():
    key_word = view.input_data(text.input_key_word_to_find, single=True)
    search_result = model.find_contact(key_word)
    view.show_contacts(search_result, text.null_search_result.format(key_word=key_word))


def edit_contact():
    id_to_edit = view.input_data(text.input_id_to_edit, single=True)
    new_contact = view.input_data(text.edit_user)
    name_edit_contact = model.edit_contact(id_to_edit, new_contact)
    view.message(text.edit_contact_successful.format(name=name_edit_contact))


def delete_contact():
    id_to_delete = view.input_data(text.input_id_to_delete, single=True)
    contact = model.delete_contact(int(id_to_delete))
    view.message(text.contact_delete_successful.format(name=contact[0]))


def say_hello():
    print('Hello, ёпта')


def end_work():
    exit()


def start_app():
    while True:
        view.show_main_menu()
        user_choice = view.main_menu_user_choice()

        main_menu_controller = [
            open_file,
            save_file,
            show_all_contacts,
            create_contact,
            find_contact,
            edit_contact,
            delete_contact,
            end_work,
        ]
        main_menu_controller[user_choice - 1]()

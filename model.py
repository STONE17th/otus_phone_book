phone_book = {}

SEPARATOR = ';'


def read_file():
    global phone_book
    with open('phone_book.txt', 'r', encoding='UTF-8') as file:
        phone_book = {i: row.strip().split(SEPARATOR) for i, row in enumerate(file.readlines(), 1)}


def save_file():
    data = '\n'.join([SEPARATOR.join(contact) for contact in phone_book.values()])
    with open('phone_book.txt', 'w', encoding='UTF-8') as file:
        file.write(data)


def _next_id():
    if phone_book:
        return max(phone_book) + 1
    return 1


def create_contact(new_contact: list[str]):
    cur_id = _next_id()
    phone_book[cur_id] = new_contact


def find_contact(key_word: str):
    global phone_book
    search_result = {}
    for i, contact in phone_book.items():
        for field in contact:
            if key_word.lower() in field.lower():
                search_result[i] = contact
                break
    return search_result


def edit_contact(id_to_edit: str, new_contact: list[str]) -> str:
    current_contact = phone_book[int(id_to_edit)]
    for i in range(len(current_contact)):
        current_contact[i] = new_contact[i] if new_contact[i] else current_contact[i]
    phone_book[int(id_to_edit)] = current_contact
    return current_contact[0]


def delete_contact(id_to_delete: int):
    global phone_book
    contact = phone_book.pop(id_to_delete)
    return contact

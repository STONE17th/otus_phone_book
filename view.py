import text


def show_main_menu():
    for i, row in enumerate(text.main_menu):
        print(f'\t{i}. {row}' if i else row)


def message(msg: str):
    print('\n' + '╔' + '═' * (len(msg) + 2) + '╗')
    print('║ ' + msg + ' ║')
    print('╚' + '═' * (len(msg) + 2) + '╝' + '\n')


def main_menu_user_choice():
    while True:
        user_choice = input(text.main_menu_user_choice)
        if user_choice.isdigit() and 0 < int(user_choice) < len(text.main_menu):
            return int(user_choice)
        else:
            message(text.main_menu_user_choice_error)


def show_contacts(data: dict[int, list], msg_error: str):
    if data:
        print('\n' + '╔' + '═' * 67 + '╗')
        for i, contact in data.items():
            print(f'║ {i:>3}. {contact[0]:<20}{contact[1]:<20}{contact[2]:<20} ║')
        print('╚' + '═' * 67 + '╝' + '\n')
    else:
        message(msg_error)


def input_data(msg_list: list[str] | str, single: bool = False) -> list[str] | str:
    # data = []
    # for row in msg_list:
    #     data.append(input(row))
    # return data
    in_data = input(msg_list) if single else [input(row) for row in msg_list]
    return in_data


if __name__ == '__main__':
    # show_main_menu()
    num = main_menu_user_choice()
    print(num)

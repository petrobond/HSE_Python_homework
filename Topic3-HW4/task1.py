documents = [
    {'type': 'passport',  'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice',   'number': '11-2',        'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006',       'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_owner_by_number(number: str) -> str | None:
    """Вернуть имя владельца по номеру документа или None, если не найден."""
    for doc in documents:
        if doc.get('number') == number:
            return doc.get('name')
    return None

def handle_command_p():
    number = input('Введите номер документа:\n').strip()
    owner = get_owner_by_number(number)
    if owner:
        print(f'Владелец документа: {owner}')
    else:
        print('Документ с таким номером не найден.')

def main_loop():
    while True:
        cmd = input('Введите команду:\n').strip().lower()
        if cmd == 'q':
            print('Выход.')
            break
        elif cmd == 'p':
            handle_command_p()
        else:
            print('Неизвестная команда. Доступные: p — владелец по номеру, q — выход.')

main_loop()
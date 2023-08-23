import json

phonebook = {"Дядя Петя": {"phone_numbers": ["12345", "12346"], "birthday": "01.03/1996", "e-mail": "petya@mail.ru"} }

with open("phonebook.json", "w", encoding = "utf-8") as phonebookjson:
    phonebookjson.write(json.dumps(phonebook, ensure_ascii = False))



def new_contact (list_names, list_phone_numbers):
    new_info_name = input('Введите ФИО: ')
    new_info_phone = int(input('Введите номер телефона: '))
    print('Контакт успешно добавлен')
    list_names.append(new_info_name)
    list_phone_numbers.append(new_info_phone)
    with open('phone_book.txt', 'a', encoding = "utf-8") as phonebook:
        phonebook.write(f'{new_info_name}, ')
        phonebook.write(f'{new_info_phone}\n')
def find_contact():
    contact_to_find = input('Введите имя, фамилию или телефонный номер для поиска: ')
    phonebook = open('phone_book.txt', encoding = 'utf-8').readlines()
    contact_found = False
    for i in iter(phonebook):
        if contact_to_find in i:
            contact_found = True
            print(f'Найден абонент {i}')
    if contact_found == False:
        print('Абонент не найден')
def all_contact():
    print('Вот текущий список контактов')
    print(phone_book_names)
    print(phone_book_numbers)
def delete_contact(list_names, list_phone_numbers):
    print(phone_book_names)
    i = int(input('выберите индекс абонента(первый элемент 0)'))
    list_names.pop(i)
    list_phone_numbers.pop(i)
    print('контакт успешно удален')
def edit_contact_name(list_names):
    print(phone_book_names)
    i = int(input('выберите индекс абонента(первый элемент 0)'))
    list_names.pop(i)
    new_info_name = input('Введите новое ФИО: ')
    list_names.append(new_info_name)
    with open('phone_book.txt', 'a', encoding = "utf-8") as phonebook:
        phonebook.write(f'{new_info_name},\n')
    print('имя контакт успешно изменен')
def edit_contact_number(list_phone_numbers):
    print(phone_book_names)
    i = int(input('выберите индекс абонента(первый элемент 0)'))
    list_phone_numbers.pop(i)
    new_info_phone = int(input('Введите номер телефона: '))
    list_phone_numbers.append(new_info_phone)
    with open('phone_book.txt', 'a', encoding = "utf-8") as phonebook:
        phonebook.write(f'{new_info_phone}\n')
    print('номер контакта успешно изменен')
def save():
    with open("phonebook.json", "w", encoding = "utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii = False))
    print('контакты были сохранены')

def load():
    with open("phonebook.json", "w", encoding = "utf-8") as fh:
        phonebook = json.load(fh)
    print('контакты были контакты были загружены')


phone_book_names = ['Иванов Иван Иванович', 'Петров Пётр Петрович', 'Сергеев Сергей Сергеевич']
phone_book_numbers = [88005553535, 89999999, 89220010103]
print('1 - Добавить контакт, 2 - найти контакт, 3 - Показать список контактов, 4 - изменить имя контакта, 5 - изменить номер контакта')
print('6 - сохранить данные, 7 - загрузить данные, 8 - удалить контакт')
choice = int(input('Введите номер своего выбора: '))
while True:
    if choice == 1:
        new_contact(phone_book_names, phone_book_numbers)
    elif choice == 2:
        find_contact()
    elif choice == 3:
        all_contact()
    elif choice == 4:
        edit_contact_name(phone_book_names)
    elif choice == 5:
        edit_contact_number(phone_book_numbers)
    elif choice == 8:
        delete_contact(phone_book_names, phone_book_numbers)
    elif choice == 6:
        save()
    elif choice == 7:
        load()
    else:
        print('Ошибка ввода')


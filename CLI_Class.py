from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record
    #потом добавим логику поиска по записям в этот класс.


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        print(f'A new contact has been created for the subscriber {self.name}')
        if phone == None:
            self.phone_list = []
        else:
            self.phone_list = [phone]
            print(f'A phone number {self.phone_list} has been added to the contact {self.name}')


    def add_phone(self, phone_number):
        if phone_number not in self.phone_list:
            self.phone_list.append(phone_number)
            print(f'A new phone number {phone_number} has been added to the contact {self.name}')
        else:
            print(f'Entered number {phone_number} already exists')


    def delete_phone(self, phone_number):
        for ph in self.phone_list:
            if ph == phone_number:
                self.phone_list.remove(ph)
                print(f'Number {ph} has been deleted')
            else:
                print(f'Entered number {phone_number} not found')


    def edit_phone(self, phone_number, new_phone_number):
        for ph in self.phone_list:
            if ph == phone_number:
                self.phone_list.remove(ph)
                self.phone_list.append(new_phone_number)
                print(f'The number {ph} has been changed to {new_phone_number}')
            else:
                print(f'Entered number {phone_number} not found')
    #реализует методы для добавления/удаления/редактирования объектов Phone


class Field:
    def __init__(self, value):
        self.value = value
    #будет родительским для всех полей, в нем потом реализуем логику общую для всех полей.


class Name(Field):
    def __init__(self, name):
        pass
        #обязательное поле с именем.


class Phone(Field):
    def __init__(self, phone = None):
        pass
    #необязательное поле с телефоном и таких одна запись (Record) может содержать несколько.
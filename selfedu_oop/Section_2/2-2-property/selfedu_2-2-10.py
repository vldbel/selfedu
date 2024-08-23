class PhoneBook:
    def __init__(self):
        self.__contacts = []
    
    def add_phone(self, phone):
        self.__contacts.append(phone)
    
    def remove_phone(self, indx):
        self.__contacts.pop(indx)

    def get_phone_list(self):
        return self.__contacts
    
class PhoneNumber:
    def __init__(self, number: int, fio: str): 
        self.__fio = fio
        self.__number = number   


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
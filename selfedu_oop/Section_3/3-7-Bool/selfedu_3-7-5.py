"""Подвиг 5. """
import sys 

class MailBox:
    def __init__(self):
        self.inbox_list = []
    
    def receive(self):
        # lst_in = list(map(str.strip, sys.stdin.readlines()))
        lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
                'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
                'Python ООП; Балакирев С.М.; 2022',
                'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']
        for line in lst_in:
            mail_from, title, content = line.split("; ")
            self.inbox_list.append(MailItem(mail_from, title, content))


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False
    
    def set_read(self, fl_read):
        self.is_read = fl_read
    
    def __len__(self):
        return 1 if self.is_read else 0

    def __str__(self):
        return f"From: {self.mail_from}, Title: {self.title}, Content: {self.content}, Readed: {self.is_read}"

    def __repr__(self):
        return self.__str__()
    

mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
print(mail.inbox_list)
inbox_list_filtered = list(filter(bool, mail.inbox_list))
print(inbox_list_filtered)
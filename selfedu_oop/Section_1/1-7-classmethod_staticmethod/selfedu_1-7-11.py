class Viber:
    messages = []
        
    @classmethod
    def add_message(cls, msg):  # добавление нового сообщения в список сообщений;
        cls.messages.append(msg)
    
    @classmethod 
    def remove_message(cls, msg): # удаление сообщения из списка;
        cls.messages.remove(msg)
    
    @classmethod
    def set_like(cls, msg):  # поставить/убрать лайк для сообщения msg, если лайка нет то он ставится, если уже есть, то убирается);
        idx = cls.messages.index(msg)
        cls.messages[idx].fl_like = not cls.messages[idx].fl_like
        # print(f"Message: {cls.messages[idx].text}; Like: {cls.messages[idx].fl_like}")
    
    @classmethod
    def show_last_message(cls, tail=1):  # отображение последних сообщений;
        # for message in cls.messages[:-tail-1:-1]:
        #     #print(message.text)
        return cls.messages[:tail]
    
    @classmethod
    def total_messages(cls):  # возвращает общее число сообщений.
        # print(len(cls.messages))
        return len(cls.messages)
        
class Message:
    def __init__(self, text, fl_like=False) -> None:
        self.text = text  # текст сообщения (строка);
        self.fl_like = fl_like  # поставлен или не поставлен лайк у сообщения, изначально False);

    
msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.total_messages()
Viber.show_last_message(5)
Viber.set_like(msg)
Viber.set_like(msg)
Viber.remove_message(msg)
Viber.total_messages()
from string import ascii_uppercase, digits
from re import fullmatch as re_fullmatch


class CardCheck:
    CHARS_FOR_NAME = ascii_uppercase + digits
    
    @staticmethod
    def check_card_number_format(card_number):
        pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
        return True if re_fullmatch(pattern, card_number) else False
    
    @classmethod
    def check_card_number(cls, number):
        return cls.check_card_number_format(number)
        
    @classmethod
    def check_name(cls, name:str):
        if not len(name.split()) == 2:
            return False
        name = set(name)
        name.remove(" ")
        if not name.issubset(set(cls.CHARS_FOR_NAME)):
            return False
        return True
                

print(CardCheck.check_card_number("1234-5678-9012-0000"))
print(CardCheck.check_name("SERGEI BALAKIREV"))
"""Подвиг 8. В программе необходимо объявить классы для работы с кошельками в разных валютах:"""
DELTA = 0.1
class MoneyR:
    """для рублевых кошельков"""
    def __init__(self, balance=0):
        self.__volume  = balance
        self.__cb = None

    def __str__(self):
        return str(self.__volume)

    @property
    def volume(self):
        return self.__volume

    @property
    def cb(self):
        return self.__cb

    @volume.setter
    def volume(self, val):
        self.__volume = val

    @cb.setter
    def cb(self, val):
        self.__cb = val

    def check_exchange_rates(self):
        if not self.__cb:
            raise ValueError("Неизвестен курс валют.")

    def get_price_in_rub(self):
        if isinstance(self, MoneyD):
            conv_rate = self.cb.rates["rub"]
        elif isinstance(self, MoneyE):
            conv_rate = self.cb.rates["euro"] * self.cb.rates["rub"]
        else:
            conv_rate = 1
        return conv_rate * self.volume

    def __eq__(self, other):
        self.check_exchange_rates()
        return (self.get_price_in_rub() - other.get_price_in_rub()) <= DELTA
    
    def __gt__(self, other):
        self.check_exchange_rates()
        return (self.get_price_in_rub() - other.get_price_in_rub()) > DELTA
    
    def __ge__(self, other):
        self.check_exchange_rates()
        return self.get_price_in_rub() > other.get_price_in_rub()
    

class MoneyD:
    """для долларовых кошельков"""
    def __init__(self, balance=0):
        self.__volume  = balance
        self.__cb = None

    def __str__(self):
        return str(self.__volume)
    
    @property
    def volume(self):
        return self.__volume

    @property
    def cb(self):
        return self.__cb

    @volume.setter
    def volume(self, val):
        self.__volume = val

    @cb.setter
    def cb(self, val):
        self.__cb = val

    def check_exchange_rates(self):
        if not self.__cb:
            raise ValueError("Неизвестен курс валют.")
    
    def get_price_in_rub(self):
        if isinstance(self, MoneyD):
            conv_rate = self.cb.rates["rub"]
        elif isinstance(self, MoneyE):
            conv_rate = self.cb.rates["euro"] * self.cb.rates["rub"]
        else:
            conv_rate = 1
        return conv_rate * self.volume

    def __eq__(self, other):
        self.check_exchange_rates()
        return (self.get_price_in_rub() - other.get_price_in_rub()) <= DELTA
    
    def __gt__(self, other):
        self.check_exchange_rates()
        return (self.get_price_in_rub() - other.get_price_in_rub()) > DELTA
    
    def __ge__(self, other):
        self.check_exchange_rates()
        return self.get_price_in_rub() > other.get_price_in_rub()

class MoneyE:
    """для евро-кошельков"""
    def __init__(self, balance=0):
        self.__volume  = balance
        self.__cb = None

    def __str__(self):
        return str(self.__volume)
    
    @property
    def volume(self):
        return self.__volume

    @property
    def cb(self):
        return self.__cb

    @volume.setter
    def volume(self, val):
        self.__volume = val

    @cb.setter
    def cb(self, val):
        self.__cb = val

    def check_exchange_rates(self):
        if not self.__cb:
            raise ValueError("Неизвестен курс валют.")
    
    def get_price_in_rub(self):
        if isinstance(self, MoneyD):
            conv_rate = self.cb.rates["rub"]
        elif isinstance(self, MoneyE):
            conv_rate = self.cb.rates["euro"] * self.cb.rates["rub"]
        else:
            conv_rate = 1
        return conv_rate * self.volume

    def __eq__(self, other):
        self.check_exchange_rates()
        return (self.get_price_in_rub() - other.get_price_in_rub()) <= DELTA
    
    def __gt__(self, other):
        self.check_exchange_rates()
        return (self.get_price_in_rub() - other.get_price_in_rub()) > DELTA
    
    def __ge__(self, other):
        self.check_exchange_rates()
        return self.get_price_in_rub() > other.get_price_in_rub()
        

class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls):
        return
    
    @classmethod
    def register(cls, money):
        """для регистрации объектов классов MoneyR, MoneyD и MoneyE."""
        money.cb = cls


# rub = MoneyR()   # с нулевым балансом
# dl = MoneyD(1501.25) # с балансом в 1501.25 долларов
# euro = MoneyE(100)  # с балансом в 100 евро

# print(rub)
# print(dl)
# print(euro)

# CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)
e = MoneyE(300)

CentralBank.register(r)
CentralBank.register(d)
CentralBank.register(e)

print(r == d)
print(r > d)
print(d > e)
print(r < e)

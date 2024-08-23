class DataBase:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
        
    def __del__(self):
            DataBase.__instance = None
    
    def __init__(self, host, user, password, port):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
    
    def connect(self):
        print("Connecting to DB " + self.user)
        
    def close(self):
        print("Closing DB connection")
        
    def read(self):
        return "data read from DB"
    
    def write(self, data):
        print("Data recorded to DB")
        

def test():
    db1 = DataBase(host='localhost', user='testdbuser', password='temppass', port='5432')
    db2 = DataBase(host='localhost', user='testdbuser2', password='temppass2', port='5432')
    print(id(db1), id(db2))
    db1.connect()

if __name__ == "__main__":
    test()
class Data:
    def __init__(self, data, ip_addr) -> None:
        self.ip_addr = ip_addr
        self.data = data
        

class Server:
    __server_no = 1
    
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.ip_addr = cls.__server_no
        cls.__server_no += 1
        return obj
    
    def __init__(self):
        self.routers:set[Router] = set()
        self.buffer = []
    
    def add_router(self, router):
            self.routers.add(router)
        
    def remove_router(self, router):
            self.routers.remove(router)
    
    def send_data(self, data: Data):
        """ для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя 
            (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);"""
        for router in self.routers:
            router.receive_data(data)
    
    def receive_data(self, data):
        self.buffer.append(data)
        # print(f"server {self} has received the data: {data}")
        
    def get_data(self):
        """ возвращает список принятых пакетов 
            (если ничего принято не было, то возвращается пустой список) и очищает входной буфер;"""
        res = self.buffer.copy()
        self.buffer = []
        return res
        
    def get_ip(self):
        """ возвращает свой IP-адрес. """
        return self.ip_addr


class Router: 
    def __init__(self):
        """ для описания работы роутеров в сети (в данной задаче полагается один роутер);"""
        self.connected_servers = set()
        """ список для хранения принятых от серверов пакетов (объектов класса Data). """
        self.buffer:list[Data] = []
        
    def link(self, server:Server):
        """ для присоединения сервера server (объекта класса Server) к роутеру 
            (для простоты, каждый сервер соединен только с одним роутером);"""
        self.connected_servers.add(server)
        server.add_router(self)
            
    def unlink(self, server:Server):
        """ для отсоединения сервера server (объекта класса Server) от роутера;"""
        self.connected_servers.remove(server)
        server.remove_router(self)
    
    def receive_data(self, data):
        self.buffer.append(data)
       
    def send_data(self):
        """" для отправки всех пакетов (объектов класса Data)
             из буфера роутера соответствующим серверам (после отправки буфер должен очищаться)."""
        for data in self.buffer:
            # print(f"sending data: {data}")
            # getting target server by ip
            target_server:Server = None
            for server in self.connected_servers: # looking for server by IP
                if server.ip_addr == data.ip_addr:
                    target_server = server # server with matching ip has found
                    break
            if not target_server: # server not found case, dropping this data
                continue
            # print(f"target server: {target_server}")
            target_server.receive_data(data)
        self.buffer.clear()
                                

# sv = Server()
# router = Router()
# data = Data(строка с данными, IP-адрес назначения)

router = Router()
sv_from = Server()
sv_from2 = Server()

router.link(sv_from)  #1
router.link(sv_from2) # 2
router.link(Server()) # 3
router.link(Server()) # 4
router.unlink(sv_from2)

sv_to = Server()
router.link(sv_to)

sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
# print(router.buffer)

router.send_data()
# print(sv_to.buffer)
msg_lst_from = sv_from.get_data()
# print(msg_lst_from)
msg_lst_to = sv_to.get_data()
# print(msg_lst_to)
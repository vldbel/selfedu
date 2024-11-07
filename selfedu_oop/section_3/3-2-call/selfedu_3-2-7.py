class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, request):
        return self.get(self.__fn, request)
    
    def get(self, func, request:dict):
        method = request.get("method", "GET")
        if method != "GET":
            return None
        return f"{method}: {func(request)}"

    
@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})
print(res)
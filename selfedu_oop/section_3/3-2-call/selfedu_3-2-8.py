class Handler:
    def __init__(self, methods):
        # здесь нужные строчки
        self.methods = methods
        # print("init")
        # print(methods)

    def __call__(self, func):
        def wrapper(request:dict, *args, **kwargs):
            # здесь нужные строчки
            # print("call/wrapper")
            method = request.get("method", "GET")
            if method not in self.methods:
                return None
            elif method == "GET":
                return self.get(func, request, *args, **kwargs)
            elif method == "POST":
                return self.post(func, request, *args, **kwargs)
        return wrapper

    def get(self, func, request, *args, **kwargs):
        """для имитации обработки GET-запроса"""
        # print("get")
        return f"GET: {func(request, *args, **kwargs)}"
        
    def post(self, func, request, *args, **kwargs):
        """для имитации обработки POST-запроса"""
        # print("post")
        return f"POST: {func(request, *args, **kwargs)}"


@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})
print("res =", res) # "POST: Сергей Балакирев"
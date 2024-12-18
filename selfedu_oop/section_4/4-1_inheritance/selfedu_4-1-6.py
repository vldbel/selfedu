"""Подвиг 6. Еще один пример, когда в базовом классе прописывается необходимый начальный функционал для дочерних классов."""

class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    # def __init__(self, methods = ('GET',)):
    #     super().__init__(methods)

    def render_request(self, request, method):
        if method.upper() not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        meth = getattr(self, method.lower())
        return meth(request)
    
    def get(self, request:dict):
        if not isinstance(request, dict):
            raise TypeError('request не является словарем')
        if not "url" in request:
            raise TypeError('request не содержит обязательного ключа url')
        return f"url: '{request['url']}"
    

dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')   # url: https://site.ru/home
print(html)

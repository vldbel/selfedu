class RenderList:
    def __init__(self, type_list):
        # type_list - тип списка (принимает значения: "ul" - для списка с тегом <ul> и "ol" - для списка с тегом <ol>).
        # Если значение параметра type_list другое (не "ul" и не "ol"), то формируется список с тегом <ul>.
        self.type_list = type_list if type_list == "ol" else "ul"
    
    def __call__(self, lst):
        """<ul>
            <li>Пункт меню 1</li>
            <li>Пункт меню 2</li>
            <li>Пункт меню 3</li>
        </ul>"""
        res = f"<{self.type_list}>\n"
        for item in lst:
            res += f"<li>{item}</li>\n"
        res += f"</{self.type_list}>"
        return res        

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)
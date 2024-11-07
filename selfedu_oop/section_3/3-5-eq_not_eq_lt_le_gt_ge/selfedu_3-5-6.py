"""""Подвиг 6. 
Ваша задача написать программу поиска слова в строке."""""

class Morph:
    def __init__(self, *words):
        self.words = []
        self.words.extend(words)

    def add_word(self, word):
        """добавление нового слова (если его нет в списке слов объекта класса Morph);"""
        if word not in self.words:
            self.words.append(word)

    def get_words(self):
        """получение кортежа форм слов."""
        return tuple(self.words)

    def __eq__(self, other):
        return other.lower() in self.words

dict_words = [  Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
                Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
                Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
                Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'), 
                Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')
            ]

text = "Мы, будем устанавливать. связь завтра днем."
text_split = [word.strip(",.;-") for word in text.lower().split()]

res = sum(dict_words.count(word) for word in text_split)
print(res)
        
    # print(list(map(lambda x: x == word, dict_words)))
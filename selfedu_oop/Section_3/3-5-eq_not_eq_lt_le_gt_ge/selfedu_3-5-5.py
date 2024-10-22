"""Подвиг 5. Имеется стихотворение, представленное следующим списком строк:"""

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

sym_to_remove = list("–?!,.;")


class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words.copy()

    def __len__(self):
        return len(self.lst_words)

    def __eq__(self, other):
        return len(self) == len(other)
    
    def __gt__(self, other):
        return len(self) > len(other)
    
    def __ge__(self, other):
        return len(self) >= len(other)
    
    def __str__(self):
        return f"{self.lst_words}"
    
    def __repr__(self):
        return self.__str__()
        

def cleanup(stich, sym_to_remove):
    clean_stich = []
    for line in stich:
        words = line.split()
        clean_line = []
        for word in words:
            if word[0] in sym_to_remove:
                word = word[1:]
            if word and word[-1] in sym_to_remove:
                word = word[:-1]
            if word:
                clean_line.append(word)
        if clean_line:
            clean_stich.append(clean_line)
    return clean_stich

cleaned_text = cleanup(stich, sym_to_remove)
# print(clean_stich)
lst_text = [StringText(line)for line in cleaned_text]

lst_text_sorted = sorted(lst_text, reverse=True)
# print(lst_text_sorted)

lst_text_sorted = [" ".join(line.lst_words) for line in lst_text_sorted]
print(lst_text_sorted)

# print(st1 > st2)   # True, если число слов в st1 больше, чем в st2
# print(st1 >= st2)  # True, если число слов в st1 больше или равно st2
# print(st1 < st2)   # True, если число слов в st1 меньше, чем в st2
# print(st1 <= st2)  # True, если число слов в st1 меньше или равно st2

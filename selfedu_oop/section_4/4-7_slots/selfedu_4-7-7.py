"""Подвиг 7. Объявите класс Note (нота), объекты которого создаются командой:"""

class Note:
    _allowed_notes = 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'
    _allowed_tones = -1, 0, 1
    
    def __init__(self, name:str, ton:int=0):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name':
            self._verify_note(value)
            super().__setattr__(key, value)

        if key == '_ton':
            self._verify_ton(value)
            super().__setattr__(key, value)

    @classmethod
    def _verify_note(cls, note:str):
        if note not in cls._allowed_notes:
            raise ValueError('недопустимое значение аргумента')
    
    @classmethod
    def _verify_ton(cls, ton:int):
        if ton not in cls._allowed_tones:
            raise ValueError('недопустимое значение аргумента')
    
class Notes:
    _instance = None

    _notes = "_do", "_re", "_mi", "_fa", "_solt", "_la", "_si"
    _notes_names = 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'

    __slots__ = _notes

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __del__(self):
        Notes._instance = None
    
    def __init__(self):
        for note, note_name in zip(self._notes, self._notes_names):
            setattr(self, note, Note(note_name))

    def __getitem__(self, key):
        return getattr(self, self.__slots__[self._check_idx(key)])
    
    def __setitem__(self, key, val):
        setattr(self, self.__slots__[self._check_idx(key)], val)

    def _check_idx(self, idx):
        if idx not in range(-len(self.__slots__), len(self.__slots__)):
            raise IndexError('недопустимый индекс')
        return idx


notes = Notes()

nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -1
"""Подвиг 7 (на повторение). Перед вами стоит задача выделения файлов с определенными расширениями из списка файлов,"""

class FileAcceptor:
    def __init__(self, *ext):
        self.ext = [*ext]

    def __call__(self, name):
        return name.split(".")[-1] in self.ext
    
    def __add__(self, other):
        return FileAcceptor(*set(self.ext + other.ext))

acceptor1 = FileAcceptor("fname.ext1", "fname.asd.ext2", "ext3")
acceptor2 = FileAcceptor("ext3", "ext4")

acceptor12 = acceptor1 + acceptor2
print(acceptor12.ext)

filenames = ["ext0", "ext1", "ext2", "ext3", "ext4", "ext5"]
filenames = list(filter(acceptor12, filenames))
print(filenames)
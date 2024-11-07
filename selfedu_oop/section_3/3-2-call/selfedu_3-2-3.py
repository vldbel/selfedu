class ImageFileAcceptor:
    def __init__(self, filter:list[str]):
        self.filter = filter

    def __call__(self, filename:str):
        ext = filename.split('.')[-1]
        return filename if ext in self.filter else None
        
filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]

image_filenames = filter(acceptor, filenames)
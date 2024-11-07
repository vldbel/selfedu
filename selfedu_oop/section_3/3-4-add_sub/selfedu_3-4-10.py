"""Подвиг 10 (на повторение). 
В нейронных сетях использую операцию под названием Max Pooling. 
Суть ее состоит в сканировании прямоугольной таблицы чисел (матрицы) 
окном определенного размера (обычно, 2x2 элемента) и 
выбора наибольшего значения в пределах этого окна"""

class MaxPooling:
    def __init__(self, step=(2, 2), size=(2,2)):
        self.step = step
        self.size = size

    @staticmethod
    def get_max_from_window(mtx):
        return max([max(line) for line in mtx])

    @staticmethod
    def get_mtx_window(mtx, start_x, start_y, size_x=2, size_y=2):
        return [line[start_x:start_x+size_x] for line in mtx[start_y:start_y+size_y]]

    def __call__(self, mtx):
        self.check_matrix(mtx)
        if not mtx:
            return
        mtx_size_x, mtx_size_y = len(mtx[0]), len(mtx)
        wnd_size_x, wnd_size_y = self.size
        wnd_step_x, wnd_step_y = self.step

        out_mtx = []
        cur_x = cur_y = 0
        while (cur_y + wnd_size_y) <= mtx_size_y:
            out_mtx_line = []
            while (cur_x + wnd_size_x) <= mtx_size_x:
                wnd = self.get_mtx_window(mtx, cur_x, cur_y, wnd_size_x, wnd_size_y)
                out_mtx_line.append(self.get_max_from_window(wnd))
                cur_x += wnd_step_x
            cur_x = 0
            cur_y += wnd_step_y
            out_mtx.append(out_mtx_line)
        return out_mtx

    @staticmethod
    def check_matrix(mtx):
        # check that matrix is rectangular 
        ln_sz = [len(line) for line in mtx]
        if ln_sz.count(ln_sz[0]) != len(ln_sz):
            raise ValueError("Неверный формат для первого параметра matrix.")
        
        # check types of all values in the matrix 
        if not all([all(map(lambda x: isinstance(x, (int, float)), line)) for line in mtx]):
            raise ValueError("Неверный формат для первого параметра matrix.")
    
    @staticmethod
    def show_mtx(mtx):
        for line in mtx:
            print(line)
        

mp = MaxPooling(step=(2, 2), size=(2,2))
matrix = ([ [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 8, 7, 6], 
            [5, 4, 3, 2]
            ])
res = mp(matrix)  # [[6, 8], [9, 7]]

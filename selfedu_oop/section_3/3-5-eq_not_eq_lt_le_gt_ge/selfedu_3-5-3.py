class Track:
    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.tracklist = []

    def add_track(self, tr):
        """добавление линейного сегмента маршрута (следующей точки);"""
        self.tracklist.append(tr)

    def get_tracks(self):
        """получение кортежа из объектов класса TrackLine."""
        return tuple(self.tracklist)

    def __len__(self):
        """возвращает целочисленную длину маршрута (привести к типу int) для объекта track"""
        start_x, start_y = self.start_x, self.start_y
        track_len = 0
        for item in self.tracklist:
            track_len += int(((item.to_x - start_x)**2 + (item.to_y - start_y)**2) ** 0.5)
            start_x, start_y = item.to_x, item.to_y
        return track_len

    def __eq__(self, other):
        return len(self) == len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed

track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track1 == track2
print(res_eq)
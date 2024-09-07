class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        """возвращает текущее время в секундах"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

class DeltaClock:
    def __init__(self, clock2:Clock, clock1:Clock):
        self.clock1 = clock1
        self.clock2 = clock2
        diff = self.clock2.get_time() - self.clock1.get_time()    
        self.delta_sec = diff if diff >= 0 else 0 
        self.delta_hours = self.delta_sec // 3600
        self.delta_minutes = self.delta_sec % 3600 // 60
        self.delta_seconds = self.delta_sec % 3600 % 60
        
    def __str__(self):
        return f"{self.delta_hours:02}:{self.delta_minutes:02}:{self.delta_seconds:02}"
    
    def __len__(self):
        return self.delta_sec

# clock1 = Clock(2, 2, 2)
# clock2 = Clock(1, 1, 1)
# dt = DeltaClock(clock1, clock2)

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)
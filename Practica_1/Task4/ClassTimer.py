class MyTimer:
    Day = 0
    Hours = 0
    Min = 0
    Seconds = 0
    Timeout = 0
    Work = True

    def __init__(self, seconds):
        self.Timeout = seconds
        self.Seconds = seconds
        self.correct()

    def correct(self):
        if self.Timeout < 0: self.Work = False
        self.Seconds = self.Timeout
        self.Min = (int)(self.Seconds / 60)
        self.Seconds = self.Seconds % 60
        self.Hours = (int)(self.Min / 60)
        self.Min = self.Min % 60
        self.Day = (int)(self.Hours / 24)
        self.Hours = self.Hours % 24

    def decTimeout(self):
        self.Timeout -= 1

    def timeout(self):
        return self.Work

    def out(self):
        print('Осталось времени: ', end=' ')
        if self.Day != 0:
            print('Day:', self.Day, end=' ')
        if self.Hours != 0:
            print('Hour:', self.Hours, end=' ')
        if self.Min != 0:
            print('Minute:', self.Min, end=' ')
        print('Second:', self.Seconds)

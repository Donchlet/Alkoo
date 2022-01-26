class TimeDesk:
    def __init__(self, seconds):
        self.seconds = seconds
        self.secons = seconds % 60
        self.minutes = seconds % 3600 // 60
        self.hours = seconds % 86400 // 3600
        self.days = seconds // 86400

    def __str__(self):
        return f'Days: {self.days}, hours: {self.hours}, minutes: {self.minutes}, seconds: {self.secons}'

promezhutok = TimeDesk(99000)
print(promezhutok)



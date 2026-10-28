class NegativTimeError(Exception):
    pass
class Time:
    def __init__(self,hours,minutes,seconds):
        if hours < 0 or minutes < 0 or seconds < 0:
            raise NegativTimeError(f"число не может быть отрицательным")
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600 )// 60
        self.seconds = total_seconds % 60
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    def __add__(self, other):
        if not isinstance(other,Time):
            return NotImplemented
        return Time(
            self.hours + other.hours,
            self.minutes + other.minutes,
            self.seconds + other.seconds
        )



try:
    t_1 = Time(2,40,25)
    print(t_1)
    t_2 = Time(10,20,15)
    print(t_2)
    t_3 = t_1 + t_2
    print(t_3)

except NegativTimeError as e:
    print(f"ошибка значения: {e}")


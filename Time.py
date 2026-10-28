class NegativTimeError(Exception):
    pass
class Time:
    def __init__(self,hours,minutes,seconds):
        if hours < 0 or minutes < 0 or seconds < 0:
            raise NegativTimeError(f"число не может быть отрицательным")
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600 )// 3600
        self.seconds = total_seconds % 60

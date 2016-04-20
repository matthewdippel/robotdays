from robotdays.src.App.DataStructures.TimeSlot import TimeSlot

class ScheduledTask():
    def __init__(self, name, timeslot):
        self._name = name
        if not isinstance(timeslot, TimeSlot):
            raise ValueError("arg timeslot must be a TimeSlot object")
        self._timeslot = timeslot
        return

    @property
    def name(self):
        return self._name

    @property
    def timeslot(self):
        return self._timeslot

    def __lt__(self, other):
        return self.timeslot.end < other.timeslot.start

    def __gt__(self, other):
        return self.timeslot.start > other.timeslot.end

    def __le__(self, other):
        return self.timeslot.end <= other.timeslot.start

    def __ge__(self, other):
        return self.timeslot.start >= other.timeslot.end

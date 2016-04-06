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
__author__ = 'mdippel'

from robotdays.src.App.Scheduling.Rules.Rule import Rule
from robotdays.src.App.DataStructures.TimeSlot import TimeSlot

class NoOverlapRule(Rule):
    """
    Rule that the task holding it cannot overlap with a defined set of intervals
    """
    def __init__(self):
        self._timeslots_to_avoid = []

    def add_timeslot_to_avoid(self, timeslot):
        if not isinstance(timeslot, TimeSlot):
            raise ValueError("param timeslot must be of type TimeSlot")
        self._timeslots_to_avoid.append(timeslot)
        return

    def timeslot_count(self):
        return len(self._timeslots_to_avoid)

    def satisfied_by(self, scheduled_task):
        """
        Check if the scheduled task overlaps with any of the intervals in
        class variable _timeslots_to_avoid

        Return False if any of them do
        Return True otherwise
        :param scheduled_task:
        :return:
        """
        for timeslot in self._timeslots_to_avoid:
            if scheduled_task.timeslot.intersects_internally_with(timeslot):
                return False
        return True
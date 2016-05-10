__author__ = 'mdippel'

from robotdays.src.App.Scheduling.Rules.Rule import Rule

class NoOverlapRule(Rule):
    """
    Rule that the task holding it cannot overlap with a defined set of intervals
    """
    def __init__(self):
        self._timeslots_to_avoid = []

    def satisfied_by(self, scheduled_task):
        """
        Check if the scheduled task overlaps with any of the intervals in
        class variable _timeslots_to_avoid

        Return False if any of them do
        Return True otherwise
        :param scheduled_task:
        :return:
        """
        pass
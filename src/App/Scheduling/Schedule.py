from robotdays.src.App.DataStructures.ScheduledTask import ScheduledTask

class Schedule():
    def __init__(self):
        self._tasks = []

    def insert_task(self, task):
        """
        Insert parameter task into the current schedule
        raise a value error if it conflicts with the current schedule
        :param task:
        :type task: ScheduledTask
        :return: does not return any value
        :rtype: None
        """
        pass

    def can_hold_task(self, task):
        """
        Checks if the parameter task can fit into the current schedule
        returns a boolean value
        :param task:
        :type task: ScheduledTask
        :return: whether or not task fits into the schedule
        :rtype: bool
        """
        pass


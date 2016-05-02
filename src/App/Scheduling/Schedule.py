from ScheduledTask import ScheduledTask

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

        if isinstance(task, ScheduledTask):
            if self.can_hold_task(task):
                self._tasks.append(task)
            else:
                raise ValueError('schedule conflict!')
        else:
            raise ValueError('inserted should be a ScheduledTask')

    def can_hold_task(self, task):
        """
        Checks if the parameter task can fit into the current schedule
        returns a boolean value
        :param task:
        :type task: ScheduledTask
        :return: whether or not task fits into the schedule
        :rtype: bool
        """
        for existing_task in self._tasks:

   #         if (task.timeslot.start> existing_task.timeslot.start
    #                and task.timeslot.start< existing_task.timeslot.start)\
     #               or (task.timeslot.end> existing_task.timeslot.start
      #              and task.timeslot.end< existing_task.timeslot.end)\
       #             or (task.timeslot.end> existing_task.timeslot.end
        #            and task.timeslot.start< existing_task.timeslot.start):
            if existing_task.timeslot.intersects_internally_with(task.timeslot) or existing_task.timeslot.intersects_boundary_with(task.timeslot):
                return False
        return True



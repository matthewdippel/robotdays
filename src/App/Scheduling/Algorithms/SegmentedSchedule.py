__author__ = 'mdippel'

from datetime import datetime
class SegmentedSchedule():
    """
    represents a segmented schedule

    here the schedule is split into discrete time slots for easier algorithmic
    manipulation

    also stores the start and end time so that it can be converted
    back into a regular schedule, and also so that it can check
    standard rules without having to convert them to a special format
    """
    def __init__(self, length, start, end):
        if not isinstance(start, datetime.datetime):
            raise ValueError("arg start must be a datetime.datetime object")
        if not isinstance(end, datetime.datetime):
            raise ValueError("arg end must be a datetime.datetime object")
        self._length = length
        self._schedule = [None] * length
        self._start, self._end = start, end
        self._segment_length = (end - start) / length
        self._stored_tasks = {}
        return



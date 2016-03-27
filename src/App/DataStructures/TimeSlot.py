import datetime

class TimeSlot():
    def __init__(self, start, end):
        self._start = start
        self._end   = end
        return

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @start.deleter
    def start(self):
        del self._start

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value

    @end.deleter
    def end(self):
        del self._end

    def intersects_internally_with(self, other):
        """
        checks if self intersects with other
        intersection must be beyond endpoints touching
        :param other: time slot to compare with self
        :type other: TimeSlot
        :return: whether or not they intersect
        :rtype: bool
        """
        pass

    def intersects_boundary_with(self, other):
        """
        checks if self intersects with other
        intersection can include endpoints touching
        :param other: time slot to compare with self
        :type other: TimeSlot
        :return: whether or not they intersect
        :rtype: bool
        """
        pass

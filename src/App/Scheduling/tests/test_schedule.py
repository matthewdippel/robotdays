from nose.tools import assert_equal
from nose.tools import assert_is
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import assert_true
from nose.tools import assert_false

from datetime import datetime as DT

from robotdays.src.App.DataStructures.TimeSlot import TimeSlot
from robotdays.src.App.Scheduling.ScheduledTask import ScheduledTask
from robotdays.src.App.Scheduling.Schedule import Schedule

class test_Schedule(object):
    """
    tests for the Schedule class
    """
    def test_empty_insert(self):
        """
        correct insert task to empty Schedule raises no errors
        """
        Myschedule = Schedule()

        a = DT.today()
        b = DT.today()
        ts = TimeSlot(a,b)
        s = ScheduledTask("eat food", ts)
        Myschedule.insert_task(s)
        return

    def test_non_conflict_insert(self):
        """
        insert task to Schedule without conflict raises no errors
        """
        Myschedule = Schedule()

        a = DT.today()
        b = DT.today()
        ts = TimeSlot(a,b)
        s = ScheduledTask("eat food", ts)
        Myschedule.insert_task(s)

        a2 = DT.today()
        b2 = DT.today()
        ts2 = TimeSlot(a2,b2)
        s2 = ScheduledTask("eat desert", ts2)
        Myschedule.insert_task(s2)

        return

    def test_conflict_insert(self):
        """
        insert task to Schedule with conflict, raises conflict errors
        """
        Myschedule = Schedule()

        a = DT.today()
        b = DT.today()
        ts = TimeSlot(a,b)
        s = ScheduledTask("eat food", ts)
        Myschedule.insert_task(s)

        b2 = DT.today()

        ts3 = TimeSlot(a,b2)
        s3 = ScheduledTask("eat desert", ts3)

        assert_raises(ValueError, Myschedule.insert_task, s3)

        return
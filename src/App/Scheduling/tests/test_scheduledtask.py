from nose.tools import assert_equal
from nose.tools import assert_is
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import assert_true
from nose.tools import assert_false

from datetime import datetime as DT

from robotdays.src.App.DataStructures.TimeSlot import TimeSlot
from robotdays.src.App.Scheduling.ScheduledTask import ScheduledTask

class test_ScheduledTask(object):
    """
    tests for the ScheduledTask class
    """
    def test_simple_init(self):
        """
        correct init of ScheduledTask raises no errors
        """
        a = DT.today()
        b = DT.today()
        ts = TimeSlot(a,b)
        s = ScheduledTask("eat food", ts)
        return

    def test_bad_params_raise_errors(self):
        """
        bad params to ScheduledTask raises ValueError
        """
        assert_raises(ValueError, ScheduledTask, None, None)
        a = DT.today()
        b = DT.today()
        ts = TimeSlot(a,b)
        assert_raises(ValueError, ScheduledTask, "eat food", "eat food")
        assert_raises(ValueError, ScheduledTask, ts, "eat food")
        return
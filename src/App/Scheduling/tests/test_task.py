__author__ = 'mdippel'
from nose.tools import assert_equal
from nose.tools import assert_is
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import assert_true
from nose.tools import assert_false

from datetime import datetime as DT

from robotdays.src.App.DataStructures.TimeSlot import TimeSlot
from robotdays.src.App.Scheduling.ScheduledTask import ScheduledTask
from robotdays.src.App.Scheduling.Task import Task

class test_Task(object):
    """
    tests for the ScheduledTask class
    """
    def test_simple_init(self):
        """
        correct init of Task raises no errors
        """
        assert_true(False, "implement this test!")
        return

    def test_bad_params_raise_errors(self):
        """
        bad params to Task raises ValueError
        """
        assert_true(False, "implement this test!")
        return
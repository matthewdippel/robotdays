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
from robotdays.src.App.Scheduling.Schedule import Schedule
from robotdays.src.App.Scheduling.Rules.NoOverlapRule import NoOverlapRule
from robotdays.src.App.Scheduling.Algorithms.SegmentedSchedule import SegmentedSchedule

class test_SegmentedSchedule(object):

    def test_bad_params_to_init_raises_errors(self):
        """
        bad params to SegmentedSchedule init raises ValueErrors
        """
        assert_raises(ValueError, SegmentedSchedule, None, None, None)
        a = DT.today()
        b = DT.today()
        l = 10
        assert_raises(ValueError, SegmentedSchedule, None, a, b)
        assert_raises(ValueError, SegmentedSchedule, l, None, b)
        assert_raises(ValueError, SegmentedSchedule, l, a, None)
        assert_raises(ValueError, SegmentedSchedule, l, b, a)
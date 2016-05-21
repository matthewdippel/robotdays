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
        assert_raises(ValueError, SegmentedSchedule, 0, a, b)

    def test_good_params_to_init_raise_no_errors(self):
        a = DT.today()
        b = DT.today()
        l = 10

        S = SegmentedSchedule(l, a, b)
        return

    def test_length_is_properly_returned(self):
        a = DT.today()
        b = DT.today()
        l = 1234

        S = SegmentedSchedule(l, a, b)
        assert_equal(S.length, 1234, "length should be equal to the param given to init")
        return

    def test_slots_start_empty(self):
        a = DT.today()
        b = DT.today()
        l = 100
        S = SegmentedSchedule(l, a, b)
        for i in range(l):
            assert_equal(S.task_at_ith_slot(i), None)
        return

    def test_bad_params_to_taskatithslot_raises_errors(self):
        a = DT.today()
        b = DT.today()
        l = 100
        S = SegmentedSchedule(l, a, b)
        assert_raises(ValueError, S.task_at_ith_slot, -1)
        assert_raises(ValueError, S.task_at_ith_slot, 100)


    def task_bad_params_to_startofithslot_raises_errors(self):
        a = DT.today()
        b = DT.today()
        l = 100
        S = SegmentedSchedule(l, a, b)
        assert_raises(ValueError, S.start_of_ith_slot, -1)
        assert_raises(ValueError, S.start_of_ith_slot, 100)

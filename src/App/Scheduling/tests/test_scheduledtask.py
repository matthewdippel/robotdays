from nose.tools import assert_equal
from nose.tools import assert_is
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import assert_true
from nose.tools import assert_false

from robotdays.src.tests.HelperClasses import UniqueDT as UniqueDT
DT = UniqueDT.UniqueDT()

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
        st_raises_no_errors = ScheduledTask("eat food", ts)
        return

    def test_gt_lt(self):
        a = DT.today()
        b = DT.today()
        c = DT.today()
        d = DT.today()

        ts_ab = TimeSlot(a, b)
        ts_cd = TimeSlot(c, d)
        st_ab = ScheduledTask("ab", ts_ab)
        st_cd = ScheduledTask("cd", ts_cd)
        assert_true(st_ab < st_cd)
        assert_true(st_ab <= st_cd)
        assert_false(st_ab > st_cd)
        assert_false(st_ab >= st_cd)

        assert_true(st_cd > st_ab)
        assert_true(st_cd >= st_ab)
        assert_false(st_cd < st_ab)
        assert_false(st_cd <= st_ab)

        ts_bc = TimeSlot(b, c)
        st_bc = ScheduledTask("bc", ts_bc)

        assert_true(st_ab <= st_bc)
        assert_false(st_ab < st_bc)
        assert_false(st_ab > st_bc)
        assert_false(st_ab >= st_bc)

        assert_true(st_bc >= st_ab)
        assert_false(st_bc > st_ab)
        assert_false(st_bc < st_ab)
        assert_false(st_bc <= st_ab)
        return
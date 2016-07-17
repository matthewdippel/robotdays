import sys
print sys.path

from nose.tools import assert_equal
from nose.tools import assert_is
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import assert_true
from nose.tools import assert_false

#from datetime import datetime as DT
from robotdays.src.tests.HelperClasses import UniqueDT as UniqueDT
DT = UniqueDT.UniqueDT()

from robotdays.src.App.DataStructures.TimeSlot import TimeSlot


class test_TimeSlot(object):
    """
    Tests for simple initilization of TimeSlot objects
    """

    def test_bad_params_raise_errors(self):

        # inputs must be datetime objects
        a = DT.today()
        assert_raises(ValueError, TimeSlot, None, None)
        assert_raises(ValueError, TimeSlot, a, None)
        assert_raises(ValueError, TimeSlot, None, a)
        return

    def test_good_params_raise_no_errors(self):
        a = DT.today()
        b = DT.today()
        t = TimeSlot(a, b)
        return

    def test_out_of_order_params_raise_errors(self):
        a = DT.today()
        b = DT.today()
        assert_raises(ValueError, TimeSlot, a, a)
        assert_raises(ValueError, TimeSlot, b, b)
        assert_raises(ValueError, TimeSlot, b, a)
        return

    def test_basic_intersection(self):
        a = DT.today()
        b = DT.today()
        c = DT.today()
        d = DT.today()
        t1 = TimeSlot(a, b)
        t2 = TimeSlot(b, c)
        assert_true(t2.intersects_boundary_with(t1))
        assert_true(t1.intersects_boundary_with(t2))
        assert_false(t2.intersects_internally_with(t1))
        assert_false(t1.intersects_internally_with(t2))

        t3 = TimeSlot(a, c)
        t4 = TimeSlot(b, d)
        assert_true(t3.intersects_internally_with(t4))
        assert_true(t4.intersects_internally_with(t3))
        assert_true(t3.intersects_boundary_with(t4))
        assert_true(t4.intersects_boundary_with(t3))

        assert_true(t1.intersects_boundary_with(t1))
        assert_true(t1.intersects_internally_with(t1))

        t5 = TimeSlot(c, d)
        assert_false(t1.intersects_boundary_with(t5))
        assert_false(t1.intersects_internally_with(t5))
        assert_false(t5.intersects_boundary_with(t1))
        assert_false(t5.intersects_internally_with(t1))

        t6 = TimeSlot(a,d)
        t7 = TimeSlot(b,c)
        assert_true(t6.intersects_internally_with(t7))
        assert_true(t6.intersects_boundary_with(t7))
        assert_true(t7.intersects_internally_with(t6))
        assert_true(t7.intersects_boundary_with(t6))

    def test_intersection_symmetry(self):
        """
        assert that a.intersects(b) = b.intersects(a) for any intervals a, b
        """
        a = DT.today()
        b = DT.today()
        c = DT.today()
        d = DT.today()
        time_slots = [a, b, c, d]
        for w in time_slots:
            for x in time_slots:
                if w >= x:
                    continue
                T1 = TimeSlot(w, x)
                for y in time_slots:
                    for z in time_slots:
                        if y >= z:
                            continue
                        T2 = TimeSlot(y, z)
                        assert_equal(T1.intersects_boundary_with(T2), T2.intersects_boundary_with(T1))
                        assert_equal(T1.intersects_internally_with(T2), T2.intersects_internally_with(T1))

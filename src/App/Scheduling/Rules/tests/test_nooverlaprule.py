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

class test_NoOverlapRule(object):

    def test_init_raises_no_errors(self):
        r = NoOverlapRule()
        assert_equal(r.timeslot_count(), 0, "init rule should have no timeslots")
        return

    def test_add_bad_timeslot_raises_error(self):
        r = NoOverlapRule()
        assert_raises(ValueError, r.add_timeslot_to_avoid, None)
        assert_equal(r.timeslot_count(), 0, "rule should have no timeslots after adding bad ones")
        assert_raises(ValueError, r.add_timeslot_to_avoid, 123)
        assert_equal(r.timeslot_count(), 0, "rule should have no timeslots after adding bad ones")
        assert_raises(ValueError, r.add_timeslot_to_avoid, DT.today())
        assert_equal(r.timeslot_count(), 0, "rule should have no timeslots after adding bad ones")
        return

    def test_can_add_timeslots(self):
        r = NoOverlapRule()
        assert_equal(r.timeslot_count(), 0, "init rule should have no timeslots")
        r.add_timeslot_to_avoid(TimeSlot(DT.today(), DT.today()))
        assert_equal(r.timeslot_count(), 1, "added 1 rule")
        r.add_timeslot_to_avoid(TimeSlot(DT.today(), DT.today()))
        assert_equal(r.timeslot_count(), 2, "added 2 rules")
        return

    def test_trivial_satisfaction(self):
        r = NoOverlapRule()
        for _ in range(100):
            r.add_timeslot_to_avoid(TimeSlot(DT.today(), DT.today()))
            ST = ScheduledTask("stuff", TimeSlot(DT.today(), DT.today()))
            assert_true(r.satisfied_by(ST), "all rules are scheduled before the dummy task")
        return

    def test_trivial_overlap(self):
        r = NoOverlapRule()
        for i in range(100):
            a = DT.today()
            b = DT.today()
            c = DT.today()
            d = DT.today()
            if i % 2 == 0:
                r.add_timeslot_to_avoid(TimeSlot(a, d))
                ST = ScheduledTask("stuff", TimeSlot(b,c))
                assert_false(r.satisfied_by(ST), "there is overlap")
            else:
                r.add_timeslot_to_avoid(TimeSlot(a, c))
                ST = ScheduledTask("stuff", TimeSlot(b,d))
                assert_false(r.satisfied_by(ST), "there is overlap")
            return

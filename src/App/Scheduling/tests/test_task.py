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
from robotdays.src.App.Scheduling.Rules.Rule import Rule

class test_Task(object):
    """
    tests for the ScheduledTask class
    """

    def test_simple_init(self):
        """
        correct init of Task raises no errors
        """
        a = DT.today()
        b = DT.today()
        length = b - a
        T = Task("stuff", length)
        return

    def test_init_bad_params_raise_errors(self):
        """
        bad params to Task raises ValueError
        """
        assert_raises(ValueError, Task, None, None)
        a = DT.today()
        b = DT.today()
        length = b - a
        assert_raises(ValueError, Task, length, None)
        assert_raises(ValueError, Task, "stuff", a)
        assert_raises(ValueError, Task, "stuff", b)
        return

    def test_add_rule_bad_params_raise_errors(self):
        a = DT.today()
        b = DT.today()
        length = b - a
        T = Task("stuff", length)
        assert_raises(ValueError, T.add_rule, None)
        assert_raises(ValueError, T.add_rule, a)
        assert_raises(ValueError, T.add_rule, length)
        assert_raises(ValueError, T.add_rule, 10)
        assert_raises(ValueError, T.add_rule, 10)

    def test_add_rule(self):
        a = DT.today()
        b = DT.today()
        length = b - a
        T = Task("stuff", length)
        R = Rule()
        T.add_rule(R)

    def test_can_always_start_when_no_rules(self):
        A = []
        B = []
        for _ in range(20):
            A.append(DT.today())
        for _ in range(20):
            B.append(DT.today())
        for a in A:
            for b in B:
                T = Task("stuff", b - a)
                assert_true(T.can_start_at(a), "a task with no rules should always be able to start")
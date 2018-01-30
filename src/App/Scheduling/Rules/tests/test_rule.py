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
from robotdays.src.App.Scheduling.Schedule import Schedule
from robotdays.src.App.Scheduling.Rules.Rule import Rule

class test_Rule(object):

    def test_basic_rule_throws_error(self):
        r = Rule()
        assert_raises(NotImplementedError, r.satisfied_by, None)


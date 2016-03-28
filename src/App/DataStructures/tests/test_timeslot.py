from nose.tools import assert_equal
from nose.tools import assert_is
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import assert_true
from nose.tools import raises


import robotdays
from robotdays.src.App.DataStructures.TimeSlot import TimeSlot

class test_TimeSlot_init(object):
    """
    Tests for simple initilization of TimeSlot objects
    """

    def test_bad_params_raise_errors(self):
        assert_raises(ValueError, TimeSlot, None, None)

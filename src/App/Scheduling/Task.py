__author__ = 'mdippel'

from Rules.Rule import Rule
from robotdays.src.App.DataStructures.TimeSlot import TimeSlot
from robotdays.src.App.Scheduling.ScheduledTask import ScheduledTask

import datetime

class Task():
    def __init__(self, name, length):
        if not isinstance(length, datetime.timedelta:
            raise ValueError("arg length must be a datetime.timedelta object")
        self._name = name
        self._rules = {}
        self._length = length

    def add_rule(self, rule):
        """
        Add a rule to the rules dictionary
        raises a ValueError if param rule does not inherit from the Rule class
        :param rule: the rule to be added
        :type rule: Rule
        :return:
        """
        if not isinstance(rule, Rule):
            raise ValueError("parameter rule must be of type Rule")
        rule_type = rule.__class__.__name__
        if rule_type not in self._rules:
            self._rules[rule_type] = []
        self._rules[rule_type].append(rule)
        return

    def can_start_at(self, start):
        """
        determine whether or not the current set of rules allow
        this task to start at the specified time
        :param start: the proposed start time
        :type start: datetime.datetime
        :return: answer to whether or not this Task can begin at time start
        :rtype : bool
        """
        if not isinstance(start, datetime.datetime):
            raise ValueError("arg start must be a datetime.datetime object")

        proposed_timeslot = TimeSlot(start, start + self._length)
        proposed_scheduled_task = ScheduledTask(self._name, proposed_timeslot)

        for rule_type in self._rules:
            for rule in self._rules[keys]:
                if not rule.satisfied_by(proposed_scheduled_task):
                    return False
        return True
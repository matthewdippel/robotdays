__author__ = 'mdippel'

from Rules.Rule import Rule

class Task():
    def __init__(self, name):
        self._name = name
        self._rules = {}

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
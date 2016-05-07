__author__ = 'mdippel'

class Rule():
    """
    Empty base class for rules
    Used only so that we can check isinstance(x, Rule) later on
    """
    def __init__(self):
        return

    def satisfied_by(self, scheduled_task):
        raise NotImplementedError
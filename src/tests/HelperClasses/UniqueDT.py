from datetime import datetime as datetime
from datetime import timedelta as timedelta
class UniqueDT:
    """
    Test class for creating unique date times
    Only meant to be used for testing purposes
    and to refactor calls to datetime.today which are not unique in succession
    on windows machines
    """
    def __init__(self):
        self.most_recent_dt = datetime.today()

    def today(self):
        # type: () -> datetime.datetime
        new_datetime = datetime.today()
        return_value = None
        if new_datetime <= self.most_recent_dt:
            return_value =  self.most_recent_dt + timedelta(microseconds=1)
            self.most_recent_dt = return_value

        else:
            self.most_recent_dt = new_datetime
            return_value = new_datetime
        print return_value
        return return_value

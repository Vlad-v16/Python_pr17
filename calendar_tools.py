import datetime

class UkrainianCalendar:
    def get_holiday_list(self):
        return ["01-01", "01-07", "03-08", "05-01", "05-09", "06-28", "08-24", "10-14", "12-25"]

    def is_working_day(self, date):
        holidays = self.get_holiday_list()
        weekday = date.weekday()
        date_str = date.strftime("%m-%d")
        return weekday < 5 and date_str not in holidays

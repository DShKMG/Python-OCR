import datetime as dt;

class Date(object):
    def __init__(self):
       CurrentDate = dt.date.today();
       self.Day = CurrentDate.day;
       self.Month = CurrentDate.month;
       self.Year = CurrentDate.year;
       return;

    def retTodayDay(self):
       return self.Day;
    def retTodayMonth(self):
       return self.Month;
    def retTodayYear(self):
       return self.Year;
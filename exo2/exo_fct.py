import datetime
class journal:

    def __init__(self, journalData):
        self.weekDay = {
            'Monday':0,
            'Tuesday':1,
            'Wednesday':2,
            'Thursday':3,
            'Friday':4,
            'Saturday':5,
            'Sunday':6}
        self.data = journalData
        self.it = 0

    def hasNextCount(self):
        if self.it+1 < len(self.data):
            return True
        else:
            return False
        
    def getNextCount(self):
        data = self.data[self.it]
        self.it = self.it+1
        return data

    def getWeekDayFromDate(self, date):
        day, month, year = (int(x) for x in date.split('/'))    
        ans = datetime.date(year, month, day)
        res = ans.strftime("%A")
        return self.weekDay[res]
        
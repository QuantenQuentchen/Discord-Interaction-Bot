from Imports import *

DayBegStruc = 520


class HClass:
    addIn = {
        # Hour : Addin
        3: 15,
        10 : 10
    }

    def __init__(self, Lehrer, Raum, Fach, Day, Hor, Len):
        self.Lehrer = Lehrer
        self.Raum = Raum
        self.Fach = Fach
        self.Day = Day
        self.Hor = Hor
        self.Len = Len
        Starts = 0
        for hor, add in self.addIn.items():
            if self.Hor >= hor:
                Starts = + add

        self.Start = int(((self.Hor - 1) * self.Len + (self.Hor - 1) * 5) + DayBegStruc + Starts)
        self.Startmin = timedelta(minutes=self.Start)  # Start Time
        self.Endmin = timedelta(minutes=self.Start + self.Len)  # End Time
        print(self.Startmin)
        print(self.Endmin)


class Stundenplan:
    def __init__(self, MaxH, Days):
        self.DayDic = {
            "Montag": 0,
            "Dienstag": 1,
            "Mittwoch": 2,
            "Donnerstag": 3,
            "Freitag": 4,
            "Samstag": 5,
            "Sonntag": 6
        }
        self.DayRange = {}
        self.MaxH = MaxH
        self.Days = Days
        try:
            self.SWeek = pickle.load(open("Plan.p", "rb"))
        except FileNotFoundError:
            self.SWeek = self.Plan_Gen()

    def Plan_Gen(self):
        SWeek = []
        for Day in range(self.Days):
            temp = []
            for Hour in range(self.MaxH):
                if Hour is not 6:
                    temp.append(HClass("Test", "Test", "Testologie", Day, Hour, 45))
                else:
                    temp.append(HClass("Test", "Test", "Testologie", Day, Hour, 50))
            SWeek.append(temp)
        return SWeek

    def Import_Plan(self):
        self.save_Plan()
        pass

    def get_Hour(self, Day, Hour):
        return self.SWeek[self.DayDic[Day]][Hour - 1]

    def save_Plan(self):
        pickle.dump(self.SWeek, open("Plan.p", "wb"))


Main = Stundenplan(11, 5)

print(Main.get_Hour("Montag", 3).Fach)

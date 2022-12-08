#########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Homework 12
#########################################
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    """A user-defined data structure that stores and manipulates dates"""
    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        """The constructor for objects of type Date"""
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        """This method returns a string representation for the object of type Date that calls it (named self).
            ** Note that this _can_ be called explicitly, but it more often is used implicitly via the print
            statement or simply by expressing self's value."""
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        """This method also returns a string representation for the object"""
        return self.__str__()

    def isLeapYear(self):
        """Returns True if the calling object is in a leap year; False otherwise"""
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """Returns a new object with the same month, day, year as the calling object (self)"""
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """Decides if self and d2 represent the same calendar date, whether or not they are the in the same place in
        memory"""
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def tomorrow(self):
        """Finds the date tomorrow"""
        if self.month == 2 and self.isLeapYear():
            if self.day + 1 > 29:
                self.month += 1
                self.day = 1
            else:
                self.day += 1
        elif self.day + 1 > DAYS_IN_MONTH[self.month]:
            if self.month + 1 > 12:
                self.month = 1
                self.day = 1
                self.year += 1
            else:
                self.month += 1
                self.day = 1
        else:
            self.day += 1

    def yesterday(self):
        """Finds the date yesterday"""
        if self.month == 3 and self.isLeapYear():
            if self.day - 1 < 1:
                self.month = 2
                self.day = DAYS_IN_MONTH[2] + 1
            else:
                self.day -= 1
        elif self.day - 1 < 1:
            if self.month == 1:
                self.month = 12
                self.day = DAYS_IN_MONTH[12]
                self.year -= 1
            else:
                self.month -= 1
                self.day = DAYS_IN_MONTH[self.month]
        else:
            self.day -= 1

    def addNDays(self, N):
        """Adds n amount of days to current date"""
        print(self.__str__())
        for i in range(N):
            self.tomorrow()
            print(self.__str__())

    def subNDays(self, N):
        """Subtracts n amount of days to current date"""
        print(self.__str__())
        for i in range(N):
            self.yesterday()
            print(self.__str__())

    def isBefore(self, d2):
        """Returns True if self date is before parameter date. Else return False if after or same day"""
        if self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month < d2.month:
                return True
            elif self.month == d2.month:
                if self.day < d2.day:
                    return True
                return False
            return False
        return False

    def isAfter(self, d2):
        """Returns True if self date is after parameter date. Else return False if before or same day"""
        if self.equals(d2):
            return False
        return not self.isBefore(d2)

    def diff(self, d2):
        """Returns an integer showing the amount of days between self date and parameter date"""
        count = 0
        varself = self.copy()
        vard2 = d2.copy()
        if self.equals(d2):
            return count
        elif varself.isBefore(vard2):
            while not vard2.equals(varself):
                vard2.yesterday()
                count -= 1
            return count
        elif varself.isAfter(vard2):
            while not varself.equals(vard2):
                varself.yesterday()
                count += 1
            return count

    def dow(self):
        """Returns the day of the week of the date"""
        names = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
        x = 3
        daysBetween = self.diff(Date(11, 9, 2011))
        key = (x + (daysBetween % 7)) % 7
        return names[key]

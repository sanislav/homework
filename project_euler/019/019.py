'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

class Calendar:
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def traverse_dates(self, start_date, end_date):
        current_day, current_month, current_year = start_date
        first_of_month_sundays = 0
        num_days_passed = 0
        
        while not (current_day == end_date[0] and current_month == end_date[1] and current_year == end_date[2]):
            next_date = self.get_next_date(current_day, current_month, current_year)
            current_day, current_month, current_year = next_date
            num_days_passed += 1

            if current_day == 1 and 'Sunday' == self.week_days[num_days_passed - (num_days_passed / 7) * 7] and current_year > start_date[2]:
                first_of_month_sundays += 1

        return first_of_month_sundays


    # Based on a day, month and year get the date of the next day 
    def get_next_date(self, day, month, year):
        next_date = [day, month, year]
        current_month_num_days = self.get_month_num_days(month, year)
        if day < current_month_num_days:
            next_date[0] = day+1
            next_date[1] = month
            next_date[2] = year
        else:
            next_date[0] = 1
            # if current month is the last one we move on to next year
            if month == self.months[-1]:
                next_date[1] = self.months[0]
                next_date[2] = year+1
            else:
                # increment the month only
                next_date[1] = self.get_next_month(month)
                next_date[2] = year

        return next_date


    # Based on a month mane get the next month in the calendar
    def get_next_month(self, month):
        return self.months[self.months.index(month) + 1]


    # Get number of days in month
    def get_month_num_days(self, month, year):
        if 'February' == month and self.is_leap_year(year):
            return 29

        return self.days_in_month[self.months.index(month)]


    # Check if year is leap year
    def is_leap_year(self, year):
        if 0 == year%400 or (0 == year%4 and 0 != year%100):
            return True
        return False

cal = Calendar()

start_date = [1, 'January', 1900]
end_date = [31, 'December', 2000]
print cal.traverse_dates(start_date, end_date)
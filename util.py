months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = dict((m[:3].lower(), m) for m in months)


def valid_month(month):
    if month:
        if month.capitalize() in months:
            return month.capitalize()


def valid_month3(month):
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)


def valid_day(day):
    if day and day.isdigit():
        day_int = int(day)
        if 1 <= day_int <= 31:
            return day_int


def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if 1900 <= year <= 2020:
            return year


given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."


def sub_m(name, nickname):
    return given_string2 % {"nickname": nickname, "name": name}


def escape_html(s):
    return s.replace("&", "&amp;").replace(">", "&gt;").replace("<", "&lt;").replace('"', "&quot;")


def fizzbuzz(n):
    if n:
        n = int(n)
        for i in range(0, n):
            if i % 3 == 0 and i % 5 == 0:
                print "FizzBuzz"
            elif i % 5 == 0:
                print "Buzz"
            elif i % 3 == 0:
                print "Fizz"
            else:
                print i

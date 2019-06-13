import webapp2
from util import *

form = """
<form method="post">
    What is your birthday?
    <br>
    <label>Month
        <input type="text" name="month" value="%(month)s">
    </label>
    <label>Day
        <input type="text" name="day" value="%(day)s">
    </label>
    <label>Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br>

    <input type="submit">
<form>
"""


class MainPage(webapp2.RedirectHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error,
                                        "month": escape_html(month),
                                        "day": escape_html(day),
                                        "year": escape_html(year)
                                        })

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get("month")
        user_day = self.request.get("day")
        user_year = self.request.get("year")

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if month and day and year:
            self.redirect("/thanks")
        else:
            self.write_form("That doesnt look valid to me!", user_month, user_day, user_year)


class TestHandler(webapp2.RedirectHandler):
    def post(self):
        # q = self.request.get("q")
        # self.response.out.write(q)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(self.request)


class ThanksHandler(webapp2.RedirectHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day~")


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/testform', TestHandler),
                               ("/thanks", ThanksHandler)], debug=True)
import os
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

form = """
<form>
    <h2>Add a food</h2>
    <input type="text" name="food" value="">
    %s

    <button>Add</button>
<form>
"""

hidden_html = """
<input type="hidden" name="food" value="%s">
"""

item_html = "<li>%s</li>"

shopping_list_html = """
<br>
<br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""


class Handler(webapp2.RedirectHandler):
    def write(self, *a, **kwargs):
        self.response.out.write(*a, **kwargs)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        items = self.request.get_all("food")

        self.render("shopping_list.html", items=items)

        # output = form
        # output_hidden = ""
        #
        # items = self.request.get_all("food")
        # if items:
        #     output_items = ""
        #     output_shopping = ""
        #     for item in items:
        #         output_hidden += hidden_html % item
        #         output_items += item_html % item
        #
        #     output_shopping += shopping_list_html % output_items
        #     output += output_shopping
        #
        # output = output % output_hidden
        # self.write(output)


class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n', 0)
        n = n and int(n)
        self.render('fizzbuzz.html', n=n)


app = webapp2.WSGIApplication([('/', MainPage), ('/fizzbuzz', FizzBuzzHandler)], debug=True)

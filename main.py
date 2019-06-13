import os
import webapp2
import jinja2
import rot13

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


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
        self.render("rot13.html")

    def post(self):
        text = self.request.get("text")
        if text:
            text = text.strip().encode("utf-8")
            print text
            rot_ = rot13.doRot13(text)
            print rot_
            self.render("rot13.html", text=rot_)
        else:
            self.render("rot13.html")


class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n', 0)
        n = n and int(n)
        self.render('fizzbuzz.html', n=n)


app = webapp2.WSGIApplication([('/', MainPage), ('/fizzbuzz', FizzBuzzHandler)], debug=True)

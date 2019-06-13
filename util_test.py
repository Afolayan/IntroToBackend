from util import *
import rot13

print(month_abbvs)

print(valid_month("july"))
print(valid_month("november"))
print(valid_month("june"))
print(valid_month("april"))
print(valid_month(""))
print(valid_month("foo"))

print(valid_month3("jul"))
print(valid_month3("nov"))
print(valid_month3("jun"))
print(valid_month3("apr"))
print(valid_month3(""))
print(valid_month3("foo"))

print valid_day('0')
print valid_day('10')
print valid_day('15')
print valid_day('500')

print valid_year('0')
print valid_year('-11')
print valid_year('1950')
print valid_year('2000')

print sub_m("Mike", "Goose")

print escape_html('>')
print escape_html('<')
print escape_html('"')
print escape_html("&")
print escape_html("&=&amp;")

fizzbuzz(100)

print rot13.doRot13("hello world")
print rot13.doRot13("enter")

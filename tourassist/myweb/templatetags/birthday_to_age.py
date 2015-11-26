from django import template
import datetime

register = template.Library()

def birthday_to_age(value):
    current = datetime.date.today().year
    value = current - value 
    return str(value)
register.filter('birthday_to_age', birthday_to_age)
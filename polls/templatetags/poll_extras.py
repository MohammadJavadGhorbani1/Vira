from django import template
from jalali_date import date2jalali , datetime2jalali
from jdatetime import date

register = template.Library()

@register.filter('jdate')
def jalalidate(value):
    return date2jalali(value)

@register.filter('jtime')
def jalalidatetime(value):
    return datetime2jalali(value)

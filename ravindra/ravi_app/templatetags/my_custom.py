from django import template

register = template.Library()


def cut(value, arg):
    """
        This will multiply the given number by "n" times!!
    """
    return value.replace(arg,'value*arg')


register.filter('cut', cut)

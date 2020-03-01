from datetime import date


def firstrun():
    return "success"


def circleArea(r):
    pi = 3.14
    area = pi * (r ** 2)
    return area


def list(l):
    first = l[0]
    last = l[-1]
    return (first, last)


def days(date1, date2):
    return (date1-date2).days

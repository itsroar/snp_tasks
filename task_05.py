import datetime


def date_in_future(days=None):
    return (datetime.datetime.now() + datetime.timedelta(days=days if isinstance(days, int) else 0)).strftime("%d-%m-%Y %H:%M:%S")

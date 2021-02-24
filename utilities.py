"""
Module comprenant des fonctions utilitaires.
"""
import datetime


def timedelta_to_num(objtime):
    """
    Function converting datetime.timedelta objects to float numbers.
    """
    return (objtime.days*24*3600)+objtime.seconds


def time_to_timedelta(time_obj):
    """
    Function converting datetime.time objects to timedelta.
    """
    return datetime.datetime.combine(datetime.datetime.min, time_obj) - datetime.datetime.min


def timedelta_to_time(timedelta_obj):
    """
    Function converting datetime.timedelta objects to datetime.time ones.
    """
    return (datetime.datetime.min + timedelta_obj).time()


def check_xls_type(argument):
    """
    Vérifie si l'argument fourni a bien pour extension XLS ou xls.
    """
    type_xls = ["xls", "XLS"]

    return argument.split('.')[-1] in type_xls

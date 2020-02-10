"""
Module comprenant des fonctions utilitaires.
"""

def time_to_num(objtime):
    """
    Function converting datetime.time objects to float numbers.
    """
    return (objtime.hour*60+objtime.minute)*60+objtime.second

def check_xls_type(argument):
    """
    Vérifie si l'argument fourni a bien pour extension XLS ou xls.
    """
    type_xls = ["xls", "XLS"]

    return argument.split('.')[-1] in type_xls
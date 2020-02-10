#!/usr/bin/env python3
#coding: utf8
"""
Module principal permettant l'utilisation du traceur de graphique en CLI.

Dépendances externes : argparse, os, sys

"""
import argparse
import os
import sys


def check_xls_type(argument):
    """
    Vérifie si l'argument fourni a bien pour extension XLS ou xls.
    """
    type_xls = ["xls", "XLS"]

    return argument.split('.')[-1] in type_xls


def main_cli():
    """
    Fonction permettant de lancer le traceur de graphique en CLI.
    """
    # Parsage des arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("gares",
                        nargs=1,
                        help="Fichier xls contenant la liste des gares avec les points kilométriques associés.")
    parser.add_argument("sillons",
                        nargs=1,
                        help="Fichier de paramètres de traitement par lot au format JSON.")
    args = parser.parse_args()

    # Vérifications des paramètres
    if not check_xls_type(args.gares) or not check_xls_type(args.sillons):
        sys.stderr.write("Les fichiers de données ne sont pas au format XLS.\n")
        sys.exit(1)

    print("test")


# Si l'on exécute le fichier, on lance la fonction main_gui
if __name__ == '__main__':
    main_cli()

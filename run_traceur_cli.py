#!/usr/bin/env python3
#coding: utf8
"""
Module principal permettant l'utilisation du traceur de graphique en CLI.
"""
import argparse
import sys
from xls_reader import XlsReader
from draw_graph import DrawGraph

from utilities import check_xls_type


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
    if not check_xls_type(args.gares[0]) or not check_xls_type(args.sillons[0]):
        sys.stderr.write("Les fichiers de données ne sont pas au format XLS.\n")
        sys.exit(1)
    
    # Lecture des fichiers XLS
    gares_reader = XlsReader(args.gares[0])
    df_gares = gares_reader.give_df_representation(None)

    sillons_reader = XlsReader(args.sillons[0])
    df_sillons = sillons_reader.give_df_representation(0)

    graph = DrawGraph(df_gares, df_sillons)
    graph.draw_sillons()
    graph.draw_stations()
    graph.finalize_graph()
    graph.show()


# Si l'on exécute le fichier, on lance la fonction main_gui
if __name__ == '__main__':
    main_cli()

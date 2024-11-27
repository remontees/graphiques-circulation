"""
Module contenant le nécessaire pour tracer un graphique de circulation.
"""
import numpy as np
import pandas as pd
from math import sqrt
from matplotlib import pyplot as plt
from matplotlib import dates as plt_dates

from utilities import time_to_timedelta, timedelta_to_time, timedelta_to_num
from datetime import timedelta


class DrawGraph:
    """
    Classe assurant la construction d'un graphique de circulation voulu
    en utilisant les librairies matplotlib et pandas à partir de données déjà disponibles
    sous forme de dataframes Pandas.
    """

    def __init__(self, df_gares, df_sillons):
        """
        Constructeur de la classe permettant de dessiner et d'afficher le graphique final.
        Les listes de gares et de sillons doivent être des dataframes pandas.
        """
        if not isinstance(df_gares, pd.DataFrame) or not isinstance(df_sillons, pd.DataFrame):
            raise ValueError("Invalid argument.")

        self.df_gares = df_gares
        self.df_sillons = df_sillons

        # Paramètres de dessin (à personnaliser si besoin)
        self.default_color = '#000000'
        self.colors = {
            'TGV': '#9b2743',
            'TER': '#004494',
            'IC': '#00A550'
        }
        self.fig, self.ax = plt.subplots(figsize=(20, 20))

    def pick_color(self, name):
        """
        Pick the right color of the train according to its name.
        """
        for type_train in self.colors.keys():
            if name.startswith(type_train):
                return self.colors[type_train]

        return self.default_color

    def finalize_graph(self):
        """
        Finalise le rendu du graphique.
        """
        plt.grid(axis='y')
        self.ax.set_title('Graphique de circulation')
        self.ax.legend().set_visible(False)

    def draw_sillons(self):
        """
        Dessine les sillons sur le graphique.
        """
        iter_df = self.df_sillons.items()
        _, pk_col = next(iter_df)

        for label, x_col in iter_df:
            # Construction of a unit dataframe for each circulation
            data_train = {
                'Heure': x_col,
                'y': pk_col
            }
            df_train = pd.DataFrame(data=data_train)
            df_train['Heure'] = pd.to_datetime(
                df_train['Heure'], errors='coerce', format='%H:%M:%S'
            ).dt.time

            # Mask every NA value
            df_train = df_train.dropna()
            train_color = self.pick_color(label)
            _ = df_train.plot.line(
                x='Heure',
                y='y',
                label=label,
                ax=self.ax,
                color=train_color)

            self.add_train_label(label, df_train, train_color)

    def add_train_label(self, text_label, df_train, label_color):
        """
        Draws the name of the circulation along the line representing the circulation (+/-).
        """
        if len(df_train['Heure'].index) > 1 and len(df_train['y'].index) > 1:
            list_points = list(
                zip(df_train['Heure'].values, df_train['y'].values))

            self.ax.annotate(text_label, xy=list_points[0], xytext=(0, 0),
                             textcoords='offset points',
                             size=8,
                             ha='center',
                             va='bottom',
                             rotation=0,
                             color=label_color)

    def draw_stations(self):
        """
        Allows you to scale the ordinate axis according to the different stations.
        """
        self.ax.set_yticks(list(self.df_gares['PK']))
        self.ax.set_yticklabels(list(self.df_gares['Gare']))

    def show(self):
        """
        Affiche le graphique à l'écran à l'écran.
        """
        plt.show()

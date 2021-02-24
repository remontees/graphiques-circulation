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
        iter_df = self.df_sillons.iteritems()
        _, pk_col = next(iter_df)

        for label, x_col in iter_df:
            # Construction of a unit dataframe for each circulation
            data_train = {
                'Heure': x_col,
                'y': pk_col
            }
            df_train = pd.DataFrame(data=data_train)
            df_train['Heure'] = pd.to_datetime(
                df_train['Heure'], errors='coerce', format='%H:%M:%S').dt.time

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
        def y_distance(points):
            """
            Retourne |dy| = |y2-y1| d'un couple de deux points.
            """
            (_, y1), (_, y2) = points

            return abs(y2-y1)

        if len(df_train['Heure'].index) > 1 and len(df_train['y'].index) > 1:
            iter_points = zip(df_train['Heure'].values, df_train['y'].values)
            # list_points = list(map(map_points, iter_points))
            list_points = list(iter_points)
            # list_segments = list(zip(list_points[1:], list_points[:-1]))
            # iter_euclidian_distances = map(y_distance, list_segments)
            # plus_long_segment = max(
            #     zip(iter_euclidian_distances, list_segments))
            # print(plus_long_segment)
            # # x1 = df_train['Heure'].iloc[1]
            # # x2 = df_train['Heure'].iloc[2]
            # # y1 = df_train['y'].iloc[1]
            # # y2 = df_train['y'].iloc[2]

            # (x1, y1), (x2, y2) = plus_long_segment[1]
            # x1, x2 = time_to_timedelta(x1), time_to_timedelta(x2)

            # x_mean = (x1+x2)/2+timedelta(seconds=60)
            # y_mean = (y1+y2)/2
            # xylabel = (timedelta_to_time(x_mean), y_mean)

            # sp1 = self.ax.transData.transform_point(
            #     (timedelta_to_num(x1), y1))
            # sp2 = self.ax.transData.transform_point(
            #     (timedelta_to_num(x2), y2))
            # # sp1, sp2 = (timedelta_to_num(x1), y1), (timedelta_to_num(x2), y2)

            # rise = (sp2[1] - sp1[1])
            # run = (sp2[0] - sp1[0])

            # # dx, dy = self.ax.transData.transform_point((run, rise))
            # # print(rise)
            # # print(run)

            # slope_degrees = np.degrees(np.arctan2(rise, run))

            # if (slope_degrees > 90):
            #     slope_degrees -= 180
            # elif (slope_degrees < -90):
            #     slope_degrees += 180

            # print(slope_degrees)

            self.ax.annotate(text_label, xy=list_points[0], xytext=(0, 0),
                             textcoords='offset points',
                             size=8,
                             ha='center',
                             va='bottom',
                             rotation=0,
                             color=label_color)
            # text.set_rotation(slope_degrees)

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

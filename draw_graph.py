import numpy as np
import functools
import operator
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import transforms as mtransforms

from utilities import time_to_num

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
            xmean = pd.to_datetime(x_col, errors='coerce', format='%H:%M:%S').mean()

            # Construction of a unit dataframe for each circulation
            data_train = {
                'Heure': x_col,
                'y': pk_col
            }
            df_train = pd.DataFrame(data = data_train)
            df_train['Heure'] = pd.to_datetime(df_train['Heure'], errors='coerce', format='%H:%M:%S').dt.time

            # Mask every NA value
            df_train = df_train.dropna()
            train_color = self.pick_color(label)
            df_train.plot.line(
                x='Heure',
                y='y',
                label=label,
                ax=self.ax,
                color=train_color)
            
            xmean = time_to_num(xmean)
            ymean = df_train['y'].mean()

            if len(df_train['Heure'].index) > 1 and len(df_train['y'].index) > 1:
                x1 = df_train['Heure'].iloc[1]
                x2 = df_train['Heure'].iloc[2]
                y1 = df_train['y'].iloc[1]
                y2 = df_train['y'].iloc[2]

                text = self.ax.annotate(label, xy=(x1, y1), xytext=(0, 0),
                                textcoords='offset points',
                                size=8,
                                horizontalalignment='center',
                                verticalalignment='bottom',
                                color=train_color)

                x1 = time_to_num(x1)
                x2 = time_to_num(x2)
                sp1 = self.ax.transData.transform_point((x1, y1))
                sp2 = self.ax.transData.transform_point((x2, y2))

                rise = (sp2[1] - sp1[1])
                run = (sp2[0] - sp1[0])

                slope_degrees = np.degrees(np.arctan2(rise, run))
                text.set_rotation(slope_degrees)

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
    


# def on_draw(event):
#     bboxes = []
#     for label in labels:
#         bbox = label.get_window_extent()
#         bboxi = bbox.inverse_transformed(fig.transFigure)
#         bboxes.append(bboxi)

#     bbox = mtransforms.Bbox.union(bboxes)


#     if fig.subplotpars.left < bbox.width:
#         fig.subplots_adjust(left=1.1*bbox.width)
#         fig.canvas.draw()
    
#     return False

# fig.canvas.mpl_connect('draw_event', on_draw)


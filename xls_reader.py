"""
Module minimaliste permettant la lecture d'un XLS
dans un dataframe à l'aide de la librairie pandas.
"""
import pandas as pd

class XlsReader:
    """
    Classe permettant de lire des fichiers XLS et
    en renvoyer la représentation sous forme de
    DataFrame pandas.
    """
    def __init__(self, url_file):
        """
        Register the url of the file.
        """
        self.url_file = url_file
    
    def give_df_representation(self, index_column):
        """
        Give the dataframe representation of the given
        XLS file.
        """
        return pd.read_excel(self.url_file, index_col=index_column)

#import Pandas as pd
import pandas
from pandas import DataFrame

def fn_get_data(file_name_in):

    if not file_name_in:

        print("file name is empty")

    else:
        na_values = ['NA', '-9999.000']
        # open the file and return the dataframe
        result_df: DataFrame = pandas.read_csv(file_name_in
                                               , sep = ','
                                               , dtype=str
                                               ,header=1
                                               , na_values = na_values
                                               )

        result_df.dropna(inplace=True
                         ,how='all'
                         ,axis=1)
        return result_df
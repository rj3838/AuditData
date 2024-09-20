import pandas as pd

# data_file_list =

import tkinter as tk
from tkinter import filedialog

from fn_get_data import fn_get_data

#from pandas.core.interchange.dataframe_protocol import DataFrame

root = tk.Tk()
root.withdraw()

file_path_list = filedialog.askopenfilenames()

list_of_frames : list = []

print(type(file_path_list))

for file_name in file_path_list:
    print(file_name)

    #input_df: DataFrame = pd.read_csv(file_name, sep = ',')
    input_df = fn_get_data(file_name)
    #print(input_df)
    #input_df.to_csv("/Users/royj/out.csv")

    # drop the section labels as it's not possible to calculate with the strings !

    input_df.drop(['Section'], axis = 1, inplace = True)
    input_df = input_df.apply(lambda x: x.map(float))

    list_of_frames.append(input_df)


    #input_np_array = input_df.to_numpy()

print(list_of_frames)

    #input_df = pd.read_csv(file_name, sep = ',')

#sum(frame for frame in  list_of_frames.values())/len(list_of_frames)
print(sum(list_of_frames)/len(list_of_frames))


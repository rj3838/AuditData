import pandas as pd

# data_file_list =

import tkinter as tk
from tkinter import filedialog

from fn_get_data import fn_get_data

#from pandas.core.interchange.dataframe_protocol import DataFrame

root = tk.Tk()
root.withdraw()

# TODO : add the request banner to the askopenfilenames to make sure only cht files are supplied

file_path_list = filedialog.askopenfilenames()

list_of_frames : list = []

print(type(file_path_list))

for file_name in file_path_list:
    #print(file_name)
    input_df = fn_get_data(file_name)

    # drop the section labels as it's not possible to calculate with the strings !

    input_df.drop(['Section'], axis = 1, inplace = True)

    # convert all the data to floating point
    input_df = input_df.apply(lambda x: x.map(float))

    # append all the frames so they are a single entity (list)
    list_of_frames.append(input_df)

# show each frame so we can see what we are dealing with

print(list_of_frames)

# average the frames

mean_frame = sum(list_of_frames)/len(list_of_frames)

print(mean_frame)

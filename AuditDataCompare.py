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

# add the section names back into the dataframe and write it to disk.

# take the first file and extract the section column as this will be used to but the sections back in
# the dataframe

section_column_data = pd.read_csv(file_path_list[0], header=1)
#section_column_data = section_column_data.take([0], axis=1)

first_column = section_column_data.iloc[:, 0].tolist()

#section_column_list = section_column_data[0].values.tolist()


#mean_frame.concat([section_column], axis=1, inplace=True, ignore_index=False)
print(first_column)
#full_mean_frame =  mean_frame.insert(0, 'Section', first_column)
mean_frame.insert(0, 'Section', first_column)
#full_mean_frame= (mean_frame.insert(0, "Section", section_column_data['Section'])
#d.concat(pd.Series(section_column_data, index=mean_frame.index, name="Section"),mean_frame],axis=1)
#(0, section_column_data['Section'])

print(mean_frame)






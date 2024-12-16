import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import magicGUImodule

class dataset():

    def __init__(self):
        pass

    def open_dataset(self,file_path=None,choosing_extension=None,func = None):
        
        if func is None:
            choosing_extension = input(str('Please give me an extension of file'))
            match choosing_extension:
                case 'xlsx':
                    df = pd.read_excel(file_path)
                    return df
                case 'csv':
                    df = pd.read_csv(f"{file_path}")
                    return df
                case 'clipboard':
                    df = pd.read_clipboard
                    return df
                case _:
                    raise ValueError ("Couldn't find exact path")
        else:
            def functional():
                if callable(func):
                    return func()
                else:
                    raise TypeError("func must be a callable function that returns a DataFrame or use lamba : instead")    
            return functional()
    def bar_chart(self,df):
         try:
                x = input("Enter the indices of columns to plot, separated by commas (e.g., 0,1,2): ")
                indices = [int(i) for i in x.split(',')]
                if not all(0 <= i < len(df.columns) for i in indices):
                    raise IndexError("One or more column indices are out of range.")

                for idx in indices:
                    plt.figure(figsize=(8, 6))
                    column_name = df.columns[idx]
                    data = df.iloc[:, idx]

                    # Plot bar chart
                    data.value_counts().plot(kind='bar')
                    plt.title(f"Bar Chart for Column: {column_name}")
                    plt.xlabel(column_name)
                    plt.ylabel("Frequency")
                    plt.show()

         except ValueError:
                print("Invalid input! Please enter column indices as integers separated by commas.")
         except IndexError as e:
                print(e)

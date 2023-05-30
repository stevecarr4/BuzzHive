import pandas as pd

def combine_data(data1, data2, data3):
    """
    Combine the data from three different sources into a single dataframe.
    """
    # Concatenate the dataframes vertically
    combined_data = pd.concat([data1, data2, data3], ignore_index=True)
    
    # Return the combined dataframe
    return combined_data

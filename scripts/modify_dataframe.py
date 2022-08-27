# importing libraries

import pandas as pd
import numpy as np


# this class can be called upon to modify the dataframe however is necessary
# contains the more commom ways of modifying the dataframe
class Modify_Df:
    # Function to calculate missing values by column
    def missing_values_table(df):
        # Total missing values
        mis_val = df.isnull().sum()

        # Percentage of missing values
        mis_val_percent = 100 * df.isnull().sum() / len(df)

        # dtype of missing values
        mis_val_dtype = df.dtypes

        # Make a table with the results
        mis_val_table = pd.concat([mis_val, mis_val_percent, mis_val_dtype], axis=1)

        # Rename the columns
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values', 2: 'Dtype'})

        # Sort the table by percentage of missing descending
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)

        # Print some summary information
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"      
            "There are " + str(mis_val_table_ren_columns.shape[0]) +
            " columns that have missing values.")

        # Return the dataframe with missing information
        return mis_val_table_ren_columns

    def format_float(value):
        return f'{value:,.2f}'

    def find_agg(df:pd.DataFrame, agg_column:str, agg_metric:str, col_name:str, top:int, order=False )->pd.DataFrame:
        
        new_df = df.groupby(agg_column)[agg_column].agg(agg_metric).reset_index(name=col_name).\
                            sort_values(by=col_name, ascending=order)[:top]
        
        return new_df

    def convert_bytes_to_megabytes(df, bytes_data):
        """
            This function takes the dataframe and the column which has the bytes values
            returns the megabytesof that value
            
            Args:
            -----
            df: dataframe
            bytes_data: column with bytes values
            
            Returns:
            --------
            A series
        """
        
        megabyte = 1*10e+5
        df[bytes_data] = df[bytes_data] / megabyte
        
        return df[bytes_data]

    def fix_outlier(df, column):
        df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].median(),df[column])
        
        return df[column]
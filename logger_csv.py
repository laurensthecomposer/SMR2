import os
import pandas as pd


class Logger( object ):
    def __init__(self, column_names, save_path_relative, file_name):
        self.column_names = column_names

        self.df = pd.DataFrame( columns=self.column_names )
        csv_path = os.path.join( save_path_relative, file_name )
        self.csv_path = os.path.abspath( csv_path )

        self.save_on_exit = True

    def save_log(self):
        print( 'save_log' )
        try:
            self.csv_df = pd.read_csv( self.csv_path )
            empty_file = False
        except:
            empty_file = True

        if empty_file:
            self.df.to_csv( self.csv_path, mode='w', index=False, header=True )
        else:
            column_names_csv = list( self.csv_df.columns )
            if column_names_csv == self.column_names:
                self.df.to_csv( self.csv_path, mode='a', index=False, header=False )
            else:
                print( 'Not the right header in existing file' )

    def append(self, arr):
        # logging
        # foldername, filename, bolt_type_real, pred, bolt_type_predicted
        # 'foldername', 'filename', 'positive[T/F]', 'real_class', 'pred_class', 'real_no', 'pred_no']
        # [IMG_CLASS_PATH, filename, positive, bolt_type_path, bolt_type,
        #                                          pred]
        data = dict( zip( self.column_names,  arr))  # connect columns with input data into dict
        self.df = self.df.append( data, ignore_index=True )  # append the data to the dataframe

    def print_header(self):
        print( self.df.head( 1 ).to_string().split( "\n", 1 )[0] )

    def print_latest(self):
        print( self.get_last_col() )

    def get_last_col(self):
        return self.df.tail( 1 ).to_string().split( "\n", 1 )[1]

    def __del__(self):
        if self.save_on_exit:
            self.save_log()
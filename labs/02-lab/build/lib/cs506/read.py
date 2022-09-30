import pandas as pd

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    csv_df = pd.read_csv(csv_file_path)
    return csv_df.T   

import gzip
import pandas as pd

def extract_string_data(url : str, desired_fields: list) -> pd.DataFrame:

    """
    
    String data is extracted as gzipped csv which is extraced to a pandas dataframe

    """

    print("Starting load of STRING data")

    try:
        
        # Open and read the gzipped file
        with gzip.open(url, 'rt') as f:
            
            df = pd.read_csv(f, sep=' ')

        # Filter relevant columns
        filtered_df = df[desired_fields]

        print("Finished load of string data")

        return filtered_df

    except FileNotFoundError:
        raise FileNotFoundError(f"The specified file at '{url}' was not found. Please check the file path.")
    
    except gzip.BadGzipFile:
        raise gzip.BadGzipFile(f"The file at '{url}' is not a valid gzip file or is corrupted.")
    
    except KeyError as e:
        raise KeyError(f"The required column '{e.args[0]}' was not found in the file.")
    
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")



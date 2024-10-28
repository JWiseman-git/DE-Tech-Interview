import gzip
import pandas as pd

# Specify the local file path within the subdirectory
# file_path = "string_data/9606.protein.links.v12.0.txt.gz"

def load_string_data(url : str) -> pd.DataFrame:

    print("starting load of string data")

    # Open and read the gzipped file
    with gzip.open(url, 'rt') as f:
    # Load data into DataFrame, assuming it's space-separated
        df = pd.read_csv(f, sep=' ')

    # Filter relevant columns
    columns_of_interest = ['protein1', 'protein2', 'combined_score']
    filtered_df = df[columns_of_interest]

    # Display a sample of the filtered data
    # print(filtered_df.head())

    print("finished load of string data")

    return filtered_df


import ftplib
# import os
import pyarrow.parquet as pq
import pandas as pd
from io import BytesIO


# FTP server details
# ftp_server = "ftp.ebi.ac.uk"
# ftp_path = "/pub/databases/opentargets/platform/24.09/output/etl/parquet/diseases/"

# # # Local path to save files
# local_dir = "downloaded_parquet_files_diseases"
# os.makedirs(local_dir, exist_ok=True)

# # Columns to keep
# desired_columns = ['id', 'name']

# ftp_server = "ftp.ebi.ac.uk"
# ftp_path = "/pub/databases/opentargets/platform/24.09/output/etl/parquet/associationByOverallDirect/"

# # Local path to save files
# local_dir = "downloaded_parquet_files_association"
# os.makedirs(local_dir, exist_ok=True)

# Columns to keep
# desired_columns = ['id', 'name']


def download_and_filter_parquet_files(ftp_server: str, ftp_path: str, desired_columns: list) -> pd.DataFrame: 
    
    df_list = []

    # Connect to FTP server
    with ftplib.FTP(ftp_server) as ftp:
        ftp.login()
        ftp.cwd(ftp_path)
        
        # List files in directory
        files = ftp.nlst()
        
        # Filter for Parquet files only
        parquet_files = [f for f in files if f.endswith('.parquet')]
        
        for filename in parquet_files:
            # Use BytesIO to read the Parquet file directly from FTP
            with BytesIO() as local_file:
                ftp.retrbinary(f"RETR {filename}", local_file.write)
                local_file.seek(0)  # Move to the beginning of the BytesIO buffer
                
                # Read the Parquet file from the BytesIO object
                table = pq.read_table(local_file)

                filtered_table = table.select(desired_columns)
                
                df = filtered_table.to_pandas()

                df_list.append(df)  # Append the DataFrame to the list

    # Combine all DataFrames into a single DataFrame
    combined_df = pd.concat(df_list, ignore_index=True)
    print(f'Completed download of all files from {ftp_server}')
    return combined_df

def download_parquet_files(ftp_server: str, ftp_path: str) -> pd.DataFrame: 
    
    df_list = []

    # Connect to FTP server
    with ftplib.FTP(ftp_server) as ftp:
        ftp.login()
        ftp.cwd(ftp_path)
        
        # List files in directory
        files = ftp.nlst()
        
        # Filter for Parquet files only
        parquet_files = [f for f in files if f.endswith('.parquet')]
        
        for filename in parquet_files:
            # Use BytesIO to read the Parquet file directly from FTP
            with BytesIO() as local_file:
                ftp.retrbinary(f"RETR {filename}", local_file.write)
                local_file.seek(0)  # Move to the beginning of the BytesIO buffer
                
                # Read the Parquet file from the BytesIO object
                table = pq.read_table(local_file)
                
                # df = filtered_table.to_pandas()
                df = table.to_pandas()

                df_list.append(df)  # Append the DataFrame to the list

    # Combine all DataFrames into a single DataFrame
    combined_df = pd.concat(df_list, ignore_index=True)
    print(f'Completed download of all files from {ftp_server}')
    return combined_df

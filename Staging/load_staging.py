from fetch_open_targets import download_and_filter_parquet_files, download_parquet_files
from fetch_string import load_string_data
from fetch_uniprot import download_uniprot_data
from commit_pd_to_sqlite import insert_pandas_data_to_sqlite
import json 

connection_details = 'connection_details.json'

with open(connection_details, 'r') as file:
    con = json.load(file)

def main():

    # Load UniProt
    insert = download_uniprot_data(con['Uniprot']['url'])
    insert_pandas_data_to_sqlite(con['Uniprot']['database'], con['Uniprot']['tablename'], insert)

    # Load String
    insert = load_string_data(con['String']['filepath'])
    insert_pandas_data_to_sqlite(con['String']['database'], con['String']['tablename'],  insert)

     # Load Open Target - Target 
    insert = download_and_filter_parquet_files(con['String']['server'], con['String']['url'], con['String']['desired fields'])
    insert_pandas_data_to_sqlite(con['Targets']['database'], con['Targets']['tablename'],  insert)

     # Load Open Target - Diseases 
    insert = download_and_filter_parquet_files(con['Diseases']['server'], con['Diseases']['url'], con['Diseases']['desired fields'])
    insert_pandas_data_to_sqlite(con['Diseases']['database'], con['Diseases']['tablename'],  insert)

     # Load Open Target - Direct Association 
    insert = download_and_filter_parquet_files(con['directassociation']['server'], con['directassociation']['url'])
    insert_pandas_data_to_sqlite(con['directassociation']['database'], con['directassociation']['tablename'],  insert)

if __name__ == '__main__':
    main() 
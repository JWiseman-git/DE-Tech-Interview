from fetch_open_targets import download_and_filter_parquet_files, download_parquet_files
from fetch_string import extract_string_data
from fetch_uniprot import download_uniprot_data
from load_data_to_database import load_data_database_table
import json 

# Load connection details from JSON
connection_details = 'ETL/connection_details.json'
with open(connection_details, 'r') as file:
    con = json.load(file)

def main():

    """
    Extract and load each source into the equivalent staging table. 
    """

    # Load UniProt
    data_to_load = download_uniprot_data(con['Uniprot']['url'])
    load_data_database_table(con['Uniprot']['database'], con['Uniprot']['tablename'], data_to_load)

    # Load String
    data_to_load = extract_string_data(con['String']['filepath'], con['String']['desired fields'])
    load_data_database_table(con['String']['database'], con['String']['tablename'],  data_to_load)

     # Load Open Target - Target 
    data_to_load = download_and_filter_parquet_files(con['Target']['server'], con['Target']['url'], con['Target']['desired fields'])
    load_data_database_table(con['Targets']['database'], con['Targets']['tablename'],  data_to_load)

     # Load Open Target - Diseases 
    data_to_load = download_and_filter_parquet_files(con['Diseases']['server'], con['Diseases']['url'], con['Diseases']['desired fields'])
    load_data_database_table(con['Diseases']['database'], con['Diseases']['tablename'],  data_to_load)

     # Load Open Target - Direct Association 
    data_to_load = download_parquet_files(con['directassociation']['server'], con['directassociation']['url'])
    load_data_database_table(con['directassociation']['database'], con['directassociation']['tablename'],  data_to_load)

if __name__ == '__main__':
    main() 
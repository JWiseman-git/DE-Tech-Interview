import unittest
import pandas as pd
import json
from ETL.fetch_open_targets import download_and_filter_parquet_files, download_parquet_files


class TestDataFrameOutput(unittest.TestCase):

    def __init__(self, *args, **kwargs):

        super(TestDataFrameOutput, self).__init__(*args, **kwargs)

        # Load JSON file from connection_details
        # Example case provided below for Targets but variables can be updated as needed 

        with open("ETL/connection_details.json", "r") as f:  
            params = json.load(f)
        self.server = params['Targets']['server']
        self.url = params['Targets']['url']
        self.expected_fields = set(params['Targets']['desired fields'])


    def test_dataframe_not_empty(self):

        # Confirm whether a loaded dataframe is empty

        result_df = download_and_filter_parquet_files(self.server, self.url)

        self.assertFalse(result_df.empty, "The DataFrame is empty")
        print('Test Passed: Dataframe was not empty')
    

    def test_return_dataframe_fields(self):

        # Check if expected fields are in the DataFrame columns

        result_df = download_and_filter_parquet_files(self.server, self.url, self.expected_fields)

        self.assertTrue(self.expected_fields.issubset(result_df.columns), "Missing expected fields in DataFrame")
        
        print('Test Passed: All expected fiedls were found in Dataframe')

if __name__ == '__main__':
    unittest.main()
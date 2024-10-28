import unittest
import pandas as pd
import sqlite3
from your_module import load_data_database_table  # Adjust the import according to your file structure

class TestLoadDataDatabaseTable(unittest.TestCase):

    def setUp(self):
        """Create an in-memory SQLite database and a sample DataFrame for testing."""
        self.database = ':memory:'  # Use an in-memory database
        self.tablename = 'test_table'
        self.data = pd.DataFrame({
            'column1': [1, 2, 3],
            'column2': ['a', 'b', 'c']
        })

    def tearDown(self):
        """No need to explicitly close the in-memory database."""
        pass

    def test_load_data(self):
        """Test if data is loaded correctly into the SQLite database."""
        load_data_database_table(self.database, self.tablename, self.data)

        # Verify if data is in the database
        conn = sqlite3.connect(self.database)
        result = pd.read_sql_query(f"SELECT * FROM {self.tablename}", conn)
        conn.close()

        # Check if the loaded data matches the original DataFrame
        pd.testing.assert_frame_equal(result, self.data)

if __name__ == '__main__':
    unittest.main()

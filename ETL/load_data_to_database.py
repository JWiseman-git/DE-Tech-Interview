import pandas as pd
import sqlite3

def load_data_database_table(database:str, tablename: str, data: pd.DataFrame):
    
    """
    Loads a provided pandas dataframe into a sqlite database.

    """

    print(f'Starting insert of table: {tablename} into SQLite database: {database}')

    # Make connection to database 
    conn = sqlite3.connect(f'{database}.db')

    # Add data to the database 
    data.to_sql(f'{tablename}', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

    print(f'Starting insert of table: {tablename} into SQLite database: {database}')

    return None 
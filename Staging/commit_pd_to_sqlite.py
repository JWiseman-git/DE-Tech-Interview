import pandas as pd
import sqlite3

def insert_pandas_data_to_sqlite(database:str, tablename: str, data: pd.DataFrame):
    
    print(f'Starting insert of {tablename} into SQLite table')
    conn = sqlite3.connect(f'{database}.db')

    data.to_sql(f'{tablename}', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

    print(f'Completed insert of {tablename} into SQLite table')

    return None 
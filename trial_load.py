
import sqlite3
def list_tables(database: str):
    conn = sqlite3.connect(f'{database}.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    conn.close()
    
    return [table[0] for table in tables]

# # Example usage
tables = list_tables('staging')
print(tables)

conn = sqlite3.connect('staging.db')
cursor = conn.cursor()
data = cursor.execute("SELECT * FROM uniprot LIMIT 3")
print(data.description)
results = cursor.fetchall()

for row in results:
    print(row)
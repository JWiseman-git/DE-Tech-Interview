# This should be used as alternative if establishing via cmd fails 

import sqlite3

# The DB will be created if it doesn't exist)

connection = sqlite3.connect('Foundation.db')

connection.commit()
connection.close()
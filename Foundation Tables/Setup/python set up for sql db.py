# This should be used as alternative if establishing via cmd fails 

import sqlite3

# The DB will be created if it doesn't exist - Semantic / Presentation layer has been added as an example

connection = sqlite3.connect('Semantic.db')

connection.commit()
connection.close()
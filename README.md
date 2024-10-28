# Overview

A complete ELT pipeline to bring open source data on UNIPROT listed proteins and their associated proteins. 

Pipeline Stages:
- Staging: Extract data from open sources to a SQLite database
- Transform (Foundation): Cleaning and storing data in normalised tables.
- Semantic (Views): Final views containing all Uniprot, Open Target and String data.

## Datasources

### Raw sources can be found here: 
- Open Targets: https://platform.opentargets.org/downloads
- String: https://string-db.org/cgi/download?sessionId=baXq4yzPPB1H&species_text=Homo+sapiens 
- UniProt: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete

## Installation and Setup

### SQLITE
- Installing SQLite - For this specific example data is loaded into locally hosted databases created using SQLite. SQLite can 
- SQLite can be downloaded here: https://www.sqlite.org/download.html - ensure to select the sqlite-tools download which is correct for your operating system.
- [Specific Tip: The SQLite extension for VScode can be used to view files within created databases directly from vscode]

### Using venv to run code and install dependencies

- Below is an example of how to activate the virtual environment from windows cmd.
- Once the virtual environment is activated you can proceed to download all depencies listed in the requirements.txt file.

```bash
# Activate the virtual environment
source env_name/bin/activate

# Install requirements
pip install -r requirements.txt
```

- After activating the virtual environment, you should ensure your chosen IDE is setup to use the corresponding python interpreter saved in the venv. 

## Staging Layer - ETL Scripts

- Staging scripts can be found within the ETL folder.
- Each source has a dedicated fetch_ script which is responsible for extracting source data into a dataframe type format.
- **Specifically, the String Data source should be first downloaded and stored locally as a gzipped file before the correspondong loading script is called. **
- Data is then loaded to the local SQLite database using load_data_to_database. If a table or database did not previously exist, this script will create them.
- MAIN is responsible for coordinating calling and loading each source are interested in.
- For each source the details to establish a connection to the source as well as the save destination are saved within conenction_details.json. 

## Foundation Tables 

- Within foundation table folder open the Table Creation file to view SQL scripts for creating tables for cleansed and normalised data.
- The Foundation database can be created pythonically using the script provided in the setup folder. 
**- Note: When working with running these code snippets with SQLite, it is important to use the following: **

### Enabling Foreign Keys 

- Ensure that foreign keys are enabled for sqlite databases.
```
PRAGMA foreign_keys = ON;
```

### Reference other databases 

- Ensure these code blocks/lines are present when referencing tables from one database in another.
- Separate databases have been created in place schemas, which are not available in SQLite
```
ATTACH DATABASE "C:\Users\jorda\Documents\GitHub\DE-Tech-Interview\staging.db" AS STAGING;
ATTACH DATABASE "C:\Users\jorda\Documents\GitHub\DE-Tech-Interview\Foundation.db" AS Foundation;
```

## Tests

- Unit tests for the staging scripts can be found within Tests in the ETL folder.
- Each unit test points to a specific element of the load process and should be called during: development stages, during CICD usage or before merging changes into the main branch.

## Contact 

For questions, please contact Jordan Wiseman in DE or post a question in the following channels: <Something@Teams>

[Working notes: https://docs.google.com/document/d/1DX4duf8doHBHvmG7oCzPHnItim-ln-RFE-EnaNXDUHw/edit?tab=t.0]



[Working notes: https://docs.google.com/document/d/1DX4duf8doHBHvmG7oCzPHnItim-ln-RFE-EnaNXDUHw/edit?tab=t.0]

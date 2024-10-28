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

- After activating the virtual environment, you should ensure your chosen IDE is setup to use the corresponding interpreter. 


## Datamodel

PRAGMA foreign_keys = ON;

ATTACH DATABASE "C:\Users\jorda\Documents\GitHub\DE-Tech-Interview\staging.db" AS STAGING;

## Contact 

For questions, please contact Jordan Wiseman in DE or post a question in the following channels: <Something@Teams>

[Working notes: https://docs.google.com/document/d/1DX4duf8doHBHvmG7oCzPHnItim-ln-RFE-EnaNXDUHw/edit?tab=t.0]

## Data Freshness 


[Working notes: https://docs.google.com/document/d/1DX4duf8doHBHvmG7oCzPHnItim-ln-RFE-EnaNXDUHw/edit?tab=t.0]

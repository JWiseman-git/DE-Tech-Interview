# Overivew

A complete ELT pipeline to bring open source data on UNIPROT listed proteins and their associated 

## Setup 


SQLite extensiopn 

## Raw sources can be found here: 
Open Targets: https://platform.opentargets.org/downloads

>> FTP server: https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/21.06/output/etl/parquet/

String: https://string-db.org/cgi/download?sessionId=baXq4yzPPB1H&species_text=Homo+sapiens 

UniProt: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete

## Data Freshness 


[Working notes: https://docs.google.com/document/d/1DX4duf8doHBHvmG7oCzPHnItim-ln-RFE-EnaNXDUHw/edit?tab=t.0]

## Datamodel

PRAGMA foreign_keys = ON;

ATTACH DATABASE "C:\Users\jorda\Documents\GitHub\DE-Tech-Interview\staging.db" AS STAGING;

## Contact 

For questions, please contact Jordan Wiseman in DE or post a question in the following channels: <Something@Teams>

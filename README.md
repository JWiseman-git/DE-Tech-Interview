# Overivew
ELT pipeline to combine open targets to UniProt Data.

Include explanation for first time setup if needed - SQLite download etc 

## Table of Contents
- [Installation](#Requirements for first time startup:)

## Requirements for first time startup: 


SQLite extensiopn 

## Raw sources can be found here: 
Open Targets: https://platform.opentargets.org/downloads

>> FTP server: https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/21.06/output/etl/parquet/

String: https://string-db.org/cgi/download?sessionId=baXq4yzPPB1H&species_text=Homo+sapiens 

UniProt: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete


[Working notes: https://docs.google.com/document/d/1DX4duf8doHBHvmG7oCzPHnItim-ln-RFE-EnaNXDUHw/edit?tab=t.0]

## Datamodel

PRAGMA foreign_keys = ON;

ATTACH DATABASE "C:\Users\jorda\Documents\GitHub\DE-Tech-Interview\staging.db" AS STAGING;

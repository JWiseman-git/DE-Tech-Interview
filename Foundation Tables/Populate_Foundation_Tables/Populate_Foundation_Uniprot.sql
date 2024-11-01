ATTACH DATABASE "C:\Users\jorda\Documents\GitHub\DE-Tech-Interview\staging.db" AS STAGING;

INSERT INTO UNIPROT 
    (DW_DISEASE_ID,
     DW_TARGET_ID,
     DW_PROTEIN_ID,
    PRIMARY_ACCESSION,          
    RECOMMENDED_PROTEIN_NAME,   
    SPECIES_COMMON_NAME,        
    SEQUENCE_LENGTH,            
    PRIMARY_GENE_NAME,         
SELECT 
    T.DW_DISEASE_ID, 
    T.DW_TARGET_ID,
    P.DW_PROTEIN_ID
    U."Primary Accession",
    U."Recommended Protein Name",
    U."Species Common Name",
    U."Sequence Length",
    U."Sequence Mass",
    U."Primary Gene Name"
FROM STAGING.UNIPROT U
LEFT JOIN PROTEIN P ON P.PROTEIN_1 = T."Open Targets dbReference"
LEFT JOIN FOUNDATION.TARGET T ON T."OpenTargets dbReference" = T.TARGET_ID
CREATE TABLE UNIPROT (
    DW_UNIPROT_ID           NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    DW_DISEASES_ID          FOREIGN KEY,
    DW_PROTEINS_ID          FOREIGN KEY,
    DW_TARGETS_ID           FOREIGN KEY,
    PRIMARY_ACCESSION       TEXT,
);


-- select 
--     "Primary Accession",
--     "Recommended Protein Name",
--     u."OpenTargets dbReference",
--     t."id"
-- from uniprot u 
-- inner join targets t on u."OpenTargets dbReference" = t."id"

select 
    "Primary Accession",
    "Recommended Protein Name",
    u."OpenTargets dbReference",
    t."id"
from uniprot u 
inner join  t on u."OpenTargets dbReference" = t."id"
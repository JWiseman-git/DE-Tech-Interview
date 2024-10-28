ATTACH DATABASE "C:\Users\jorda\Documents\GitHub\DE-Tech-Interview\staging.db" AS STAGING;

INSERT INTO PROTEIN  
    (PROTEIN_1,
     PROTEIN_2, 
     COMBINED_SCORE)
SELECT 
    S.PROTEIN1, 
    S.PROTEIN2,
    S.COMBINED_SCORE
FROM string s;
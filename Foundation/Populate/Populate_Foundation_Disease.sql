ATTACH DATABASE "C:\Users\jorda\Documents\GitHub\DE-Tech-Interview\staging.db" AS STAGING;

INSERT INTO DISEASE  
    (DISEASE_ID,
     DISEASE_NAME)
SELECT 
    D.ID, 
    D.NAME
FROM DISEASES d;
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE (NAME LIKE 'Ella') OR (NAME LIKE 'Lucy') OR (NAME LIKE 'Pickle') OR (NAME LIKE 'Rogan') OR (NAME LIKE 'Sabrina') OR (NAME LIKE 'Mitty')

# 너무 길고 이상한거같아서 검색.. -> IN 발견
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Ella', 'Lucy', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
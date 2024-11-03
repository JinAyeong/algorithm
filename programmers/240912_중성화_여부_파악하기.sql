-- 코드를 입력하세요
SELECT ANIMAL_ID,
       NAME,
       # WHERE : 특정 절 만족하는 행 선택, CASE : 조건에 따라 다른 값 반환
       CASE
            WHEN (SEX_UPON_INTAKE LIKE '%Neutered%') THEN 'O'
            WHEN (SEX_UPON_INTAKE LIKE '%Spayed%') THEN 'O'
            ELSE 'X'
        END AS 중성화
FROM ANIMAL_INS
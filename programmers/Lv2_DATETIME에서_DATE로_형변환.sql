-- 코드를 입력하세요
-- SELECT ANIMAL_ID, NAME, FORMAT(DATETIME, 'yyyy-mm-dd') AS 날짜
-- FROM ANIMAL_INS
# 헐랭 FORMAT 하면 될줄알았는데 안됨 -> 왜?!

# 날짜는 DATE_FORMAT 사용해야함
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
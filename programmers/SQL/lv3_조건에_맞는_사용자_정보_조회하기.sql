-- SUBSTR(문자열, 시작위치, 길이) : 문자열에서 특정 위치부터 지정한 길이만큼의 문자열을 추출하는 함수
-- CONCAT(A, B, C, ...) : 여러 문자열을 하나로 합치는 함수

SELECT
    UGU.USER_ID,
    UGU.NICKNAME,
    CONCAT(
        UGU.CITY, ' ',
        UGU.STREET_ADDRESS1, ' ',
        UGU.STREET_ADDRESS2
    ) AS 전체주소,
    CONCAT(
        SUBSTR(UGU.TLNO, 1, 3), '-',
        SUBSTR(UGU.TLNO, 4, 4), '-',
        SUBSTR(UGU.TLNO, 8, 4)
    ) AS 전화번호
FROM USED_GOODS_USER UGU
JOIN USED_GOODS_BOARD UGB
    ON UGU.USER_ID = UGB.WRITER_ID
GROUP BY
    UGU.USER_ID,
    UGU.NICKNAME,
    UGU.CITY,
    UGU.STREET_ADDRESS1,
    UGU.STREET_ADDRESS2,
    UGU.TLNO
HAVING COUNT(*) >= 3
ORDER BY UGU.USER_ID DESC;
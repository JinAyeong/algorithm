SELECT 
  YEAR(E1.DIFFERENTIATION_DATE) AS YEAR,     -- 분화 연도 추출
  (E2.SIZE - E1.SIZE_OF_COLONY) AS YEAR_DEV, -- 연도별 최대 크기에서 개체 크기를 빼서 편차 계산
  ID                                         -- 대장균 개체의 ID
FROM ECOLI_DATA E1                           -- 메인 테이블: 대장균 개체 정보
JOIN (
  SELECT 
    MAX(SIZE_OF_COLONY) AS SIZE,             -- 연도별 최대 대장균 크기 계산
    YEAR(DIFFERENTIATION_DATE) AS YEAR       -- 분화 연도 추출
  FROM ECOLI_DATA
  GROUP BY YEAR(DIFFERENTIATION_DATE)        -- 연도별로 그룹화
) AS E2
ON YEAR(E1.DIFFERENTIATION_DATE) = E2.YEAR   -- 메인 테이블과 서브 쿼리를 연도 기준으로 조인
ORDER BY YEAR, YEAR_DEV;

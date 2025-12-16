-- 기본 구조
SELECT
    SUM(G.SCORE) AS SCORE,   -- 한 사원의 상/하반기 점수를 합산한 총점
    E.EMP_NO,                -- 사원번호
    E.EMP_NAME,              -- 이름
    E.POSITION,              -- 직급
    E.EMAIL                  -- 이메일
FROM HR_EMPLOYEES AS E       -- 사원 정보 테이블
JOIN HR_GRADE AS G           -- 점수 테이블
    ON E.EMP_NO = G.EMP_NO   -- 사원번호로 두 테이블 연결(사원 - 점수)
WHERE G.YEAR = '2022'        -- 2022년 점수만 사용
GROUP BY E.EMP_NO            -- 사원별로 점수를 합치기 위해 사원번호로 그룹화
ORDER BY SCORE DESC          -- 총점 기준으로 가장 높은 사람부터 정렬
LIMIT 1;                     -- 그중 1명(1등)만 출력


-- 서브쿼리
SELECT
    M.SCORE,                 -- 미리 계산해둔 2022년 총점
    M.EMP_NO,                -- 사원번호
    E.EMP_NAME,              -- 이름
    E.POSITION,              -- 직급
    E.EMAIL                  -- 이메일
FROM HR_EMPLOYEES AS E       -- 사원 테이블
JOIN (
    SELECT
        EMP_NO,              -- 사원번호 기준으로
        SUM(SCORE) AS SCORE  -- 2022년 점수를 미리 합쳐놓음
    FROM HR_GRADE
    WHERE YEAR = '2022'
    GROUP BY EMP_NO          -- 사원번호로 묶어 점수 합산
) AS M
ON E.EMP_NO = M.EMP_NO       -- 합산된 점수를 가진 M과 다시 사원 정보 조인
ORDER BY M.SCORE DESC         -- 가장 높은 점수 순 정렬
LIMIT 1;                      -- 가장 높은 사람 1명만 출력
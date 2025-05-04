-- 업그레이드된 아이템의 ID, 이름, 희귀도
SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY
FROM ITEM_INFO I

-- ITEM_TREE 테이블과 조인: I.ITEM_ID가 업그레이드된(자식) 아이템이므로 T.ITEM_ID와 연결
JOIN ITEM_TREE T ON I.ITEM_ID = T.ITEM_ID

-- 부모 아이템 정보를 가져오기 위해 ITEM_INFO 테이블을 한 번 더 조인
-- T.PARENT_ITEM_ID가 P.ITEM_ID (부모 아이템의 정보)
JOIN ITEM_INFO P ON T.PARENT_ITEM_ID = P.ITEM_ID

-- 부모 아이템의 희귀도가 'RARE'인 경우만 선택
WHERE P.RARITY = 'RARE'

-- 결과는 업그레이드된 아이템의 ITEM_ID 기준으로 내림차순 정렬
ORDER BY I.ITEM_ID DESC;

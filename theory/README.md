# theory

자료구조와 알고리즘 이론 정리

## 목차

### 자료구조

- [배열 · 연결 리스트](data-structures/array-list.md)
- [스택 · 큐 · 덱](data-structures/stack-queue.md)
- [트리](data-structures/tree.md)
- [이진 탐색 트리 · 균형 트리](data-structures/bst-balanced.md)
- [힙 · 우선순위 큐](data-structures/heap-pq.md)
- [해시](data-structures/hash.md)
- [그래프](data-structures/graph.md)

### 알고리즘

- [시간복잡도](algorithms/complexity.md)
- [정렬](algorithms/sorting.md)
- [이분 탐색](algorithms/binary-search.md)
- [그래프 탐색 (BFS · DFS)](algorithms/graph-traversal.md)
- [백트래킹 · 완전 탐색](algorithms/backtracking.md)
- [최단 경로](algorithms/shortest-path.md)
- [유니온 파인드 · 최소 신장 트리](algorithms/union-find-mst.md)
- [동적 계획법](algorithms/dp.md)
- [그리디](algorithms/greedy.md)
- [분할 정복](algorithms/divide-and-conquer.md)
- [투 포인터 · 슬라이딩 윈도우 · 누적 합](algorithms/two-pointer.md)
- [문자열 패턴 매칭](algorithms/string.md)

## 시간복잡도 요약

### 자료구조

| 자료구조 | 접근 | 탐색 | 삽입 | 삭제 | 비고 |
| --- | --- | --- | --- | --- | --- |
| 배열 | `O(1)` | `O(n)` | `O(n)` | `O(n)` | 정렬돼 있으면 탐색 `O(log n)`, 끝 삽입은 동적 배열 분할상환 `O(1)` |
| 연결 리스트 | `O(n)` | `O(n)` | `O(1)` | `O(1)` | 위치(이전 노드)를 알 때 |
| 스택 | `O(n)` | `O(n)` | `O(1)` | `O(1)` | top에서만 |
| 큐 | `O(n)` | `O(n)` | `O(1)` | `O(1)` | rear 삽입, front 삭제 |
| 덱 | `O(n)` | `O(n)` | `O(1)` | `O(1)` | 양끝 |
| 해시 테이블 | — | `O(1)` | `O(1)` | `O(1)` | 평균. 최악 `O(n)`, 순서 없음 |
| 이진 탐색 트리 | — | `O(log n)` | `O(log n)` | `O(log n)` | 평균. 편향 시 최악 `O(n)` |
| AVL 트리 | — | `O(log n)` | `O(log n)` | `O(log n)` | 높이 ≤ 1.44 log n, 삽입 회전 최대 1번(단일/이중) |
| 2-3 트리 | — | `O(log n)` | `O(log n)` | `O(log n)` | 모든 리프 같은 레벨, 차수 3 B-트리 |
| 2-3-4 트리 | — | `O(log n)` | `O(log n)` | `O(log n)` | 하향식 분할, 레드-블랙과 대응 |
| 레드-블랙 트리 | — | `O(log n)` | `O(log n)` | `O(log n)` | 높이 ≤ 2 log(n+1), 회전 삽입 ≤ 2, 삭제 ≤ 3 |
| 스플레이 트리 | — | `O(log n)` | `O(log n)` | `O(log n)` | 분할상환. 1회 최악 `O(n)` |
| B-트리 | — | `O(log n)` | `O(log n)` | `O(log n)` | 높이 `O(log_m n)`, 디스크 접근 최소 |
| B+트리 | — | `O(log n)` | `O(log n)` | `O(log n)` | 데이터는 리프에만, 범위 검색 `O(log n + k)` |

### 힙

| 힙 | 최솟값 조회 | 삽입 | 최솟값 삭제 | 키 감소 | 합병 |
| --- | --- | --- | --- | --- | --- |
| 이진 힙 | `O(1)` | `O(log n)` | `O(log n)` | `O(log n)` | `O(n)` |
| 최소-최대 힙 | `O(1)` | `O(log n)` | `O(log n)` | `O(log n)` | `O(n)` |
| 좌향 트리 | `O(1)` | `O(log n)` | `O(log n)` | `O(log n)` | `O(log n)` |
| 이항 힙 | `O(1)` | `O(log n)` (분할상환 `O(1)`) | `O(log n)` | `O(log n)` | `O(log n)` |
| 피보나치 힙 | `O(1)` | `O(1)` | 분할상환 `O(log n)` | 분할상환 `O(1)` | `O(1)` |

### 정렬

| 정렬 | 최선 | 평균 | 최악 | 공간 | 안정 | 제자리 |
| --- | --- | --- | --- | --- | --- | --- |
| 버블 | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | O | O |
| 선택 | `O(n²)` | `O(n²)` | `O(n²)` | `O(1)` | X | O |
| 삽입 | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | O | O |
| 셸 | `O(n log n)` | `O(n^1.3~1.5)` | `O(n²)` | `O(1)` | X | O |
| 병합 | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(n)` | O | X |
| 퀵 | `O(n log n)` | `O(n log n)` | `O(n²)` | `O(log n)` | X | O |
| 힙 | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(1)` | X | O |
| 계수 | `O(n + k)` | `O(n + k)` | `O(n + k)` | `O(n + k)` | O | X |
| 기수 | `O(d(n + k))` | `O(d(n + k))` | `O(d(n + k))` | `O(n + k)` | O | X |

### 그래프

| 알고리즘 | 시간복잡도 | 음수 가중치 | 비고 |
| --- | --- | --- | --- |
| BFS / DFS | `O(V + E)`, 인접 행렬 `O(V²)` | — | BFS는 가중치 없는 최단 거리 |
| 다익스트라 | `O(E log V)`, 배열 `O(V²)` | X | 단일 출발 |
| 벨만-포드 | `O(VE)` | O | 음수 사이클 검출 |
| 플로이드-워셜 | `O(V³)` | O | 모든 쌍, 음수 사이클 불가 |
| 크루스칼 | `O(E log E)` | 상관없음 | MST, 희소 그래프 |
| 프림 | `O(E log V)`, 배열 `O(V²)` | 상관없음 | MST, 밀집 그래프 |
| 위상 정렬 | `O(V + E)` | — | DAG만 |
| 임계 경로 | `O(V + E)` | — | AOE 네트워크, 위상 정렬 2번 |
| 단절점 | `O(V + E)` | — | DFS + low |
| 강한 연결 요소 | `O(V + E)` | — | 코사라주, 타잔 |

### 문자열 패턴 매칭

| 알고리즘 | 전처리 | 매칭(평균) | 매칭(최악) | 비고 |
| --- | --- | --- | --- | --- |
| 단순 매칭 | 없음 | `O(n)` 근처 | `O(nm)` | |
| KMP | `O(m)` | `O(n)` | `O(n)` | 실패 함수 |
| 보이어-무어 | `O(m + σ)` | `O(n/m)` ~ `O(n)` | `O(nm)` | 기본형 기준 |
| 라빈-카프 | `O(m)` | `O(n + m)` | `O(nm)` | 롤링 해시 |

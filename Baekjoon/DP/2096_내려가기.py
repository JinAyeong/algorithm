N = int(input())
m_one, m_two, m_three = 0, 0, 0
n_one, n_two, n_three = 0, 0, 0

for i in range(N):
    c_one, c_two, c_three = map(int, input().split())

    m_one, m_two, m_three = max(c_one+m_one, c_one+m_two), max(c_two+m_one, c_two+m_two, c_two+m_three), max(c_three+m_two, c_three+m_three)

    n_one, n_two, n_three = min(c_one + n_one, c_one + n_two), min(c_two + n_one, c_two + n_two, c_two + n_three), min(c_three + n_two, c_three + n_three)

print(max(m_one, m_two, m_three), min(n_one, n_two, n_three))